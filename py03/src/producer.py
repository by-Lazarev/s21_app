import json
import random
import logging
import redis
import time

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Подключение к Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def generate_message():
    message = {
        "metadata": {
            "from": str(random.randint(1000000000, 9999999999)),
            "to": str(random.randint(1000000000, 9999999999))
        },
        "amount": random.randint(-10000, 10000)
    }
    return message

def main():
    channel = "transactions"
    while True:
        message = generate_message()
        r.publish(channel, json.dumps(message))
        logging.info(f"Published message: {message}")
        time.sleep(1)  # Генерация сообщения каждую секунду

if __name__ == "__main__":
    main()

