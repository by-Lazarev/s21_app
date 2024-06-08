import sys

def decypher(message):
    # Разделяем сообщение на слова
    words = message.split()
    # Извлекаем первую букву каждого слова и приводим её к верхнему регистру
    result = ''.join(word[0].upper() for word in words)
    return result

if __name__ == "__main__":
    # Получаем сообщение из аргументов командной строки
    if len(sys.argv) < 2:
        print("Usage: python decypher.py \"Your message here\"")
    else:
        message = sys.argv[1]
        print(decypher(message))

