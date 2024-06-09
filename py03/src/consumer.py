import argparse
import json
import logging
import redis

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def process_message(message, bad_accounts):
    try:
        data = json.loads(message["data"])
        from_acc = data["metadata"]["from"]
        to_acc = data["metadata"]["to"]
        amount = data["amount"]

        # Проверка, является ли получатель "плохим" аккаунтом и сумма не отрицательная
        if to_acc in bad_accounts and amount >= 0:
            # Меняем местами отправителя и получателя
            data["metadata"]["from"], data["metadata"]["to"] = to_acc, from_acc

        return data
    except json.JSONDecodeError:
        logging.error("Received invalid JSON message")
        return None

def main():
    parser = argparse.ArgumentParser(description="Process messages from a Redis queue.")
    parser.add_argument("-e", "--evil", required=True, help="Comma-separated list of bad guy account numbers.")
    args = parser.parse_args()

    # Разбиваем строку аргументов на список аккаунтов
    bad_accounts = args.evil.split(',')

    # Подключение к Redis
    r = redis.Redis(host='localhost', port=6379, db=0)
    pubsub = r.pubsub()
    pubsub.subscribe("transactions")

    logging.info("Consumer started and subscribed to 'transactions' channel")

    for message in pubsub.listen():
        if message["type"] == "message":
            processed_message = process_message(message, bad_accounts)
            if processed_message:
                logging.info(f"Processed message: {json.dumps(processed_message)}")

if __name__ == "__main__":
    main()

