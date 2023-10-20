import random, time

def create_matrix(size):
    matrix =[]
    for i in range(size):
        list_row = []
        for j in range(size):
            val = random.randint(1, 50)
            list_row.append(val)
        matrix.append(list_row)
    return matrix


def zero_matrix(size):
    matrix =[]
    for i in range(size):
        list_row = []
        for j in range(size):
            list_row.append(0)
        matrix.append(list_row)
    return matrix


def matrix_multi(n):
    start = time.time()
    A = create_matrix(n)
    B = create_matrix(n)
    matrix = zero_matrix(n)
    for row_a in range(len(A)):
        for col_b in range(len(B[0])):
            for col_a in range(len(A[0])):
                matrix[row_a][col_b] += A[row_a][col_a]*B[col_a][col_b]
    end = time.time()
    execution_time = end - start
    return "Execution time: " + str(execution_time) +"s"
    
print(matrix_multi(5))