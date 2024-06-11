# test_mul_perf.py

import time
from matrix import mul as cython_mul

def py_mul(a, b):
    b_iter = zip(*b)
    return [
        [
            sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
            for col_b in b_iter
        ] for row_a in a
    ]

# Пример матриц для тестирования
x = [[i for i in range(100)] for _ in range(100)]
y = [[i for i in range(100)] for _ in range(100)]

# Тестируем производительность Python реализации
start_time = time.time()
py_result = py_mul(x, y)
py_duration = time.time() - start_time
print(f"Python implementation took {py_duration:.6f} seconds.")

# Тестируем производительность Cython реализации
start_time = time.time()
cython_result = cython_mul(x, y)
cython_duration = time.time() - start_time
print(f"Cython implementation took {cython_duration:.6f} seconds.")

# Проверка, что результаты одинаковы
assert py_result == cython_result, "Results are not the same!"

