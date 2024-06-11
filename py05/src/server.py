from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from typing import List
import os
import shutil
from pathlib import Path
import mimetypes

app = FastAPI()

# Определите директорию для загрузки файлов
UPLOAD_DIRECTORY = "uploaded_files"
app.state.upload_directory = UPLOAD_DIRECTORY
Path(app.state.upload_directory).mkdir(parents=True, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def main_page():
    # Список всех файлов в директории UPLOAD_DIRECTORY
    files = os.listdir(app.state.upload_directory)
    files_list = "".join(f"<li><a href='/files/{file}'>{file}</a> - <audio controls><source src='/files/{file}' type='{mimetypes.guess_type(file)[0]}'></audio></li>" for file in files)
    html_content = f"""
    <html>
        <body>
            <h1>Uploaded Sound Files</h1>
            <ul>{files_list}</ul>
            <form action="/upload" enctype="multipart/form-data" method="post">
                <input name="file" type="file" accept=".mp3,.ogg,.wav">
                <input type="submit" value="Upload">
            </form>
            <p id="message"></p>
        </body>
    </html>
    """
    return html_content

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Проверка MIME-типа
    mime_type, _ = mimetypes.guess_type(file.filename)
    if mime_type not in ["audio/mpeg", "audio/ogg", "audio/wav"]:
        raise HTTPException(status_code=400, detail="Non-audio file detected")

    # Сохранение файла
    file_path = os.path.join(app.state.upload_directory, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}

@app.get("/files/{filename}", response_class=FileResponse)
async def get_file(filename: str):
    file_path = os.path.join(app.state.upload_directory, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return file_path

