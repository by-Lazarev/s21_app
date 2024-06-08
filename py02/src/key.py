class Key(list):
    def __init__(self, *args, **kwargs):
        pass

    def __len__(self):
        return 0

    def __eq__(self, other):
        return isinstance(other, list)

    def __lt__(self, other):
        if isinstance(other, list):
            return True
        return False

    def __gt__(self, other):
        return False

    def __le__(self, other):
        if isinstance(other, list):
            return True
        return False

    def __ge__(self, other):
        return False

    def __getitem__(self, index):
        raise TypeError("Key не поддерживает доступ по индексу")

    def append(self, value):
        raise AttributeError("Key не поддерживает добавление элементов")

