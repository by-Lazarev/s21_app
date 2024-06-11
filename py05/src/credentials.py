from wsgiref.simple_server import make_server
from urllib.parse import parse_qs, urlparse
import json

# Словарь с известными типами
credentials_dict = {
    "Time Lord": "Rassilon",
    "Human": "Doctor",
    "Dalek": "Exterminate"
}

def application(environ, start_response):
    # Извлекаем параметры запроса
    query_string = environ['QUERY_STRING']
    params = parse_qs(query_string)
    
    # Получаем значение параметра "species"
    species = params.get('species', [None])[0]
    
    # Определяем ответ в зависимости от значения species
    if species and species in credentials_dict:
        response_body = json.dumps({"credentials": credentials_dict[species]})
        status = '200 OK'
        headers = [('Content-Type', 'application/json')]
    else:
        response_body = json.dumps({"credentials": "Unknown"})
        status = '404 Not Found'
        headers = [('Content-Type', 'application/json')]

    # Возвращаем ответ
    start_response(status, headers)
    return [response_body.encode('utf-8')]

if __name__ == '__main__':
    # Запускаем сервер на порту 8888
    httpd = make_server('127.0.0.1', 8888, application)
    print("Serving on port 8888...")
    httpd.serve_forever()
