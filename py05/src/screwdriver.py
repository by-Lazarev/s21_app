import requests
import sys
import os

DEFAULT_SERVER_URL = "http://127.0.0.1:8888"

def upload_file(file_path, server_url=DEFAULT_SERVER_URL):
    if not os.path.isfile(file_path):
        print(f"File '{file_path}' does not exist.")
        return

    file_name = os.path.basename(file_path)
    with open(file_path, "rb") as file:
        files = {"file": (file_name, file)}
        response = requests.post(f"{server_url}/upload", files=files)

    if response.status_code == 200:
        print(f"File '{file_name}' uploaded successfully.")
    else:
        print(f"Failed to upload file: {response.json()['detail']}")

def list_files(server_url=DEFAULT_SERVER_URL):
    response = requests.get(server_url)
    if response.status_code == 200:
        print("Files on server:")
        print(response.text)
    else:
        print(f"Failed to retrieve file list: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python screwdriver.py [upload /path/to/file | list]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "upload" and len(sys.argv) == 3:
        upload_file(sys.argv[2])
    elif command == "list":
        list_files()
    else:
        print("Invalid command or missing parameters.")

