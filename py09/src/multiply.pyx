# multiply.pyx

def mul(list a, list b):
    cdef int i, j, k
    cdef int rows_a = len(a)
    cdef int cols_a = len(a[0])
    cdef int cols_b = len(b[0])
    
    # Создаем пустую результирующую матрицу
    cdef list result = [[0] * cols_b for _ in range(rows_a)]
    
    # Умножение матриц
    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = 0
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    
    return result

