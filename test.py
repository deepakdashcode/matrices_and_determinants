from matrices import matrix
A = matrix([[1, 2, 3]])
B = matrix([[1],
            [2],
            [3]])

C = matrix([[2, 2],
            [2, 2]])
D = matrix([[2, 2, 3],
            [2, 2, 1]])
print(D)
print(D.Transpose())
print(C * D)
print(A * B)

ide = matrix([[1, 0],
              [0, 1]])

ide1 = matrix([[5, 0],
              [0, 7]])

p = matrix([[1],
            [1],
            [2]])
print(p)
print(ide1.trace())
m1 = matrix([[1, 2],
             [2, 3],
             [3, 6]])

m2 = matrix([[3, 4],
             [3, 4],
             [5, 6]])

print(m1 + m2)
print(m1 - m2)
print(ide.is_idempotent())
print(ide.is_involutory())
a=matrix.null(2,3)
print(a)
print(matrix.identity(5))
print(A.is_row_matrix())
print(B.is_column_matrix())
print(A.is_vertical_matrix())
print(B.is_vertical_matrix())
print(B.is_horizontal_matrix())
