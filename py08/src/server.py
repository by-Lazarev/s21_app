# server.py

import uuid
import asyncio
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Dict, Union
import httpx

app = FastAPI()

tasks: Dict[str, Dict] = {}

class TaskCreate(BaseModel):
    urls: List[str]

class TaskResult(BaseModel):
    url: str
    status_code: str  # Изменяем на строку

class TaskStatus(BaseModel):
    id: str
    status: str
    result: List[TaskResult] = None  # Используем TaskResult для результатов

@app.post("/api/v1/tasks/", response_model=TaskStatus, status_code=201)
async def create_task(task: TaskCreate, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    tasks[task_id] = {"status": "running", "result": []}  # Инициализация result как пустого списка
    background_tasks.add_task(process_urls, task_id, task.urls)
    print(f"Created task: {task_id} with URLs: {task.urls}")
    return TaskStatus(id=task_id, status="running")

async def process_urls(task_id: str, urls: List[str]):
    results = []
    async with httpx.AsyncClient() as client:
        for url in urls:
            try:
                response = await client.get(url)
                print(f"Fetched {url} with status {response.status_code}")
                results.append({"url": url, "status_code": str(response.status_code)})  # Приводим status_code к строке
            except httpx.HTTPError as e:
                print(f"Failed to fetch {url}: {e}")
                results.append({"url": url, "status_code": "error"})
    tasks[task_id] = {"status": "ready", "result": results}
    print(f"Task {task_id} completed with results: {results}")

@app.get("/api/v1/tasks/{task_id}", response_model=TaskStatus)
async def get_task_status(task_id: str):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    print(f"Status request for task {task_id}: {task}")
    return TaskStatus(id=task_id, status=task["status"], result=task["result"] or [])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)

