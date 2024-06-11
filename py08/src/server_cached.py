# server_cached.py

import uuid
import asyncio
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Dict
import httpx
import redis.asyncio as aioredis

app = FastAPI()
redis = None

tasks: Dict[str, Dict] = {}

class TaskCreate(BaseModel):
    urls: List[str]

class TaskResult(BaseModel):
    url: str
    status_code: str

class TaskStatus(BaseModel):
    id: str
    status: str
    result: List[TaskResult] = None

@app.on_event("startup")
async def startup_event():
    global redis
    redis = await aioredis.create_redis_pool("redis://localhost")

@app.on_event("shutdown")
async def shutdown_event():
    redis.close()
    await redis.wait_closed()

@app.post("/api/v1/tasks/", response_model=TaskStatus, status_code=201)
async def create_task(task: TaskCreate, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    tasks[task_id] = {"status": "running", "result": []}
    background_tasks.add_task(process_urls, task_id, task.urls)
    return TaskStatus(id=task_id, status="running")

async def process_urls(task_id: str, urls: List[str]):
    results = []
    async with httpx.AsyncClient() as client:
        for url in urls:
            domain = url.split('/')[2]
            # Увеличиваем счетчик запросов к домену
            await redis.incr(f"domain:{domain}")

            # Проверяем кэш
            cached_status = await redis.get(f"url:{url}")
            if cached_status:
                print(f"Cache hit for {url} with status {cached_status.decode()}")
                results.append({"url": url, "status_code": cached_status.decode()})
            else:
                try:
                    response = await client.get(url)
                    status_code = str(response.status_code)
                    print(f"Fetched {url} with status {status_code}")
                    results.append({"url": url, "status_code": status_code})
                    # Сохраняем результат в кэш
                    await redis.setex(f"url:{url}", 60 * 5, status_code)  # Кэш на 5 минут
                except httpx.HTTPError as e:
                    print(f"Failed to fetch {url}: {e}")
                    results.append({"url": url, "status_code": "error"})
    tasks[task_id] = {"status": "ready", "result": results}

@app.get("/api/v1/tasks/{task_id}", response_model=TaskStatus)
async def get_task_status(task_id: str):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskStatus(id=task_id, status=task["status"], result=task["result"] or [])

# Корутиина для очистки кэша
async def cleanup_cache():
    while True:
        keys = await redis.keys('url:*')
        for key in keys:
            ttl = await redis.ttl(key)
            if ttl == -1:  # Устанавливаем TTL для ключей без срока жизни
                await redis.expire(key, 60 * 5)  # Устанавливаем срок жизни 5 минут
        await asyncio.sleep(60)  # Проверка каждые 60 секунд

@app.on_event("startup")
async def schedule_cache_cleanup():
    asyncio.create_task(cleanup_cache())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)

