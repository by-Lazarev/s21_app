# FastAPI Sound File Manager

## Описание

Этот проект представляет собой простое клиент-серверное приложение на основе FastAPI для управления звуковыми файлами. Серверная часть позволяет загружать и хранить аудиофайлы на сервере, а также предоставляет веб-интерфейс для просмотра и воспроизведения загруженных файлов. Клиентская часть позволяет загружать файлы на сервер и получать список загруженных файлов через командную строку.

## Запуск сервера

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Запустите сервер:
   ```bash
   uvicorn server:app --reload --host 127.0.0.1 --port 8888
   ```

3. Перейдите по адресу `http://127.0.0.1:8888/` в браузере для управления файлами.

## Клиентская часть

### Установка зависимостей

Для работы клиентской части установите библиотеку `requests`:
```bash
pip install requests
```

### Команды

1. **Загрузка файла**:
   ```bash
   python screwdriver.py upload /path/to/file.mp3
   ```
   Эта команда загружает указанный аудиофайл на сервер.

2. **Получение списка файлов**:
   ```bash
   python screwdriver.py list
   ```
   Эта команда получает и выводит список всех файлов, хранящихся на сервере.

### Примеры использования

- Чтобы загрузить файл `song.mp3` на сервер:
  ```bash
  python screwdriver.py upload /path/to/song.mp3
  ```

- Чтобы получить список всех файлов на сервере:
  ```bash
  python screwdriver.py list
  ```

## Примечания

- Сервер принимает только аудиофайлы с расширениями .mp3, .ogg, и .wav. При попытке загрузить файл другого типа будет отображаться сообщение "Non-audio file detected".
- Загруженные файлы сохраняются в директорию `uploaded_files`.
- На веб-странице можно воспроизводить загруженные звуковые файлы непосредственно из браузера.

## Требования

- Python 3.7 или выше
- Установленные зависимости из `requirements.txt`

## Файлы проекта

- `server.py`: Основной серверный скрипт с FastAPI.
- `screwdriver.py`: Клиентский скрипт для загрузки и получения списка файлов.
- `requirements.txt`: Файл с зависимостями для установки.
- `README.md`: Этот файл с инструкциями по использованию.

## Лицензия

Этот проект распространяется под лицензией MIT.

