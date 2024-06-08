from typing import Dict, Tuple

def squeaky(func):
    def wrapper(*args, **kwargs):
        print("SQUEAK")
        return func(*args, **kwargs)
    return wrapper

@squeaky
def add_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    # Создаем копию кошелька, чтобы не изменять исходный объект
    new_purse = purse.copy()
    # Добавляем один слиток
    if "gold_ingots" in new_purse:
        new_purse["gold_ingots"] += 1
    else:
        new_purse["gold_ingots"] = 1
    return new_purse

@squeaky
def get_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    # Создаем копию кошелька, чтобы не изменять исходный объект
    new_purse = purse.copy()
    # Убираем один слиток, если он есть
    if "gold_ingots" in new_purse:
        if new_purse["gold_ingots"] > 1:
            new_purse["gold_ingots"] -= 1
        else:
            del new_purse["gold_ingots"]
    return new_purse

@squeaky
def empty(purse: Dict[str, int]) -> Dict[str, int]:
    # Возвращаем пустой словарь
    return {}

def split_booty(*purses: Dict[str, int]) -> Tuple[Dict[str, int], Dict[str, int], Dict[str, int]]:
    # Подсчет общего количества золотых слитков
    total_gold_ingots = sum(purse.get("gold_ingots", 0) for purse in purses)

    # Распределение слитков
    share1 = total_gold_ingots // 3
    share2 = (total_gold_ingots // 3) + (1 if total_gold_ingots % 3 > 0 else 0)
    share3 = (total_gold_ingots // 3) + (1 if total_gold_ingots % 3 == 2 else 0)

    # Создание новых кошельков
    purse1 = {"gold_ingots": share1}
    purse2 = {"gold_ingots": share2}
    purse3 = {"gold_ingots": share3}

    return purse1, purse2, purse3

# Примеры использования:
if __name__ == "__main__":
    purse = {"gold_ingots": 2, "stones": 3}
    print(add_ingot(purse))  # {'gold_ingots': 3, 'stones': 3}
    print(get_ingot(purse))  # {'gold_ingots': 1, 'stones': 3}
    print(empty(purse))      # {}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))  # {'gold_ingots': 1}
    purse1 = {"gold_ingots": 3, "apples": 5}
    purse2 = {"gold_ingots": 2}
    purse3 = {"oranges": 7}

    result = split_booty(purse1, purse2, purse3)
    print(result)  # ({'gold_ingots': 2}, {'gold_ingots': 2}, {'gold_ingots': 1})

