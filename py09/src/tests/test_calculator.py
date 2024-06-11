import calculator

# Примеры использования
print(calculator.add(14, 21))  # Ожидается: 35
print(calculator.sub(14, 21))  # Ожидается: -7
print(calculator.mul(14, 21))  # Ожидается: 294
print(calculator.div(14, 7))   # Ожидается: 2

# Проверка ошибок
try:
    print(calculator.add(14.5, 21.87))  # Ожидается: TypeError
except TypeError as e:
    print(e)

try:
    print(calculator.div(14, 0))  # Ожидается: ZeroDivisionError
except ZeroDivisionError as e:
    print(e)

