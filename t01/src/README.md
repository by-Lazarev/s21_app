# RPG Game Project
---

## Описание
Этот проект представляет собой текстовую ролевую игру с пошаговой механикой, где игрок может исследовать мир, взаимодействовать с неигровыми персонажами (NPC), сражаться с врагами и управлять своим инвентарём. Игра реализована как Telegram-бот.

## Структура проекта
Проект имеет следующую структуру:

```

src/
│
├── data/                        # JSON файлы с данными игры
│   ├── enemy_data.json          # Данные врагов
│   ├── locations.json           # Данные локаций
│   ├── npc_data.json            # Данные NPC
│   └── player_profile.json      # Данные профиля игрока
│
├── game/                        # Основные игровые модули
│   ├── __init__.py
│   ├── bot.py                   # Логика Telegram-бота
│   ├── enemy.py                 # Класс Enemy (враги)
│   ├── load_all.py              # Скрипт для инициализации всех данных
│   ├── load_data.py             # Функции для загрузки данных NPC и врагов
│   ├── load_map.py              # Функции для загрузки карты игры
│   ├── locations.py             # Классы для представления локаций
│   ├── npc.py                   # Класс NPC (неигровые персонажи)
│   └── protagonist.py           # Класс Protagonist (главный герой)
│
├── tests/                       # Тесты для проекта
│   ├── __init__.py
│   ├── test_bot.py              # Тесты для Telegram-бота
│   ├── test_enemy.py            # Тесты для класса Enemy
│   ├── test_locations.py        # Тесты для локаций
│   ├── test_npc.py              # Тесты для класса NPC
│   └── test_protagonist.py      # Тесты для класса Protagonist
│
├── main.py                      # Точка входа для запуска бота
├── pytest.ini                   # Конфигурация для pytest
└── requirements.txt             # Зависимости проекта
```


## Установка и настройка

### Клонирование репозитория

```
git clone https://github.com/username/rpg-game-project.git
cd rpg-game-project/src
```

### Создание и активация виртуального окружения

```
python3 -m venv venv
source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
```

### Установка зависимостей

```
pip install -r requirements.txt
```

## Запуск тестов

Для запуска всех тестов выполните команду:

```
pytest -vv
```

## Использование

### Запуск Telegram-бота

Перед запуском убедитесь, что у вас есть токен Telegram-бота. Создайте файл .env в корневом каталоге проекта и добавьте в него строку:

```
TELEGRAM_TOKEN=your_telegram_bot_token
```

### Запустите бота командой:

```
python main.py
```

### Взаимодействие с ботом

Откройте Telegram и найдите вашего бота по имени, затем начните с командой /start. Далее используйте меню бота для перемещения, общения с NPC, сражений и управления инвентарём.

## Дополнительная информация
Проект поддерживает следующие функции:

- Исследование мира: Игрок может перемещаться между различными локациями.
- Взаимодействие с NPC: Игрок может общаться с неигровыми персонажами.
- Сражения с врагами: Игрок может сражаться с врагами.
- Управление инвентарём: Игрок может просматривать и управлять своим инвентарём.

## Тестирование
Проект покрыт тестами с использованием pytest. Тесты расположены в папке tests/ и охватывают следующие аспекты:

- Логика работы Telegram-бота
- Функциональность классов Protagonist, NPC и Enemy
- Работа с локациями

## Для запуска тестов используйте команду:

```
pytest
```

## Поддержка и вклад
Если у вас есть предложения по улучшению или вы нашли ошибку, пожалуйста, создайте issue или отправьте pull request на GitHub/GitLab. Мы всегда рады вашей помощи!
