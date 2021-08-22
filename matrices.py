import sys


def minor_matrix(A: list, row: int, column: int):
    new_ls = []
    for i in range(0, len(A)):
        current_ls = []
        for j in range(0, len(A)):
            if row == i or column == j:
                pass
            else:
                current_ls.append(A[i][j])
        if len(current_ls) != 0:
            new_ls.append(current_ls)
    return new_ls


def det(A: list):
    if len(A) == 1:
        return A[0][0]

    if len(A) == 2:
        return (A[0][0] * A[1][1]) - (A[1][0] * A[0][1])
    s = 0
    for i in range(0, len(A)):
        if i % 2 != 0:
            s = s + -(A[0][i] * det(minor_matrix(A, 0, i)))
        else:
            s = s + (A[0][i] * det(minor_matrix(A, 0, i)))
    return s


def minor(A: list, row: int, column: int):
    return det(minor_matrix(A, row, column))


def multiply(ls1, ls2):
    s = 0
    for i in range(0, len(ls1)):
        s = s + (ls1[i] * ls2[i])

    return s


def add(ls1, ls2):
    ls = []
    for i in range(0, len(ls1)):
        ls.append(ls1[i] + ls2[i])
    return ls


def sub(ls1, ls2):
    ls = []
    for i in range(0, len(ls1)):
        ls.append(ls1[i] - ls2[i])
    return ls


def transpose(ls):
    new_ls = []
    for i in range(0, len(ls[0])):
        current_ls = []
        for j in range(0, len(ls)):
            current_ls.append(ls[j][i])
        new_ls.append(current_ls)
    return new_ls


class matrix:
    def __init__(self, ls):
        self.matrix = ls
        self.row = len(ls)
        self.column = len(ls[0])
        self.transpose = transpose(ls)


    def order(self):
        ls = self.matrix
        row = len(ls)
        column = len(ls[0])
        s = f'{row} X {column}'
        return s

    def __eq__(self, other):
        if self.matrix == other.matrix:
            return True
        else:
            return False

    def Transpose(self):
        return matrix(self.transpose)

    def __add__(self, other):
        """
        :type other: matrix
        """
        if (self.row == other.row) and (self.column == other.column):
            new_ls = []
            for i in range(self.row):
                new_ls.append(add(self.matrix[i], other.matrix[i]))
            return matrix(new_ls)

    def __sub__(self, other):
        """
        :type other: matrix
        """
        if (self.row == other.row) and (self.column == other.column):
            new_ls = []
            for i in range(self.row):
                new_ls.append(sub(self.matrix[i], other.matrix[i]))
            return matrix(new_ls)

    def __mul__(self, other):
        """
        :type other: matrix
        """
        if self.column != other.row:
            sys.stderr.write('Multiplication not possible\n')
            sys.stderr.write(
                f'Tried to multiply a matrix of order {self.order()} with a matrix of order {other.order()}\n')
        else:
            A = self.matrix
            B = other.transpose
            new_ls = []
            for i in range(0, self.row):
                current_ls = []
                for j in range(other.column):
                    current_ls.append(multiply(A[i], B[j]))
                new_ls.append(current_ls)
            return matrix(new_ls)

    def __str__(self):
        if self.column == 1:
            s = ''
            for i in self.matrix:
                s = s + f'|{i[0]}|\n'
            return s
        s = ''
        for i in range(0, self.row):
            for j in range(0, self.column):
                if j == 0:
                    s = s + '|' + str(self.matrix[i][j]) + '\t'
                elif j == (self.column - 1):
                    s = s + str(self.matrix[i][j]) + '|'

                else:
                    s = s + str(self.matrix[i][j]) + '\t'

            s = s + '\n'
        return s

    def null(n: int, m: int):
        ls = []
        for i in range(m):
            ls.append(0)
        new_ls = []  # First making all the elements zero
        for i in range(n):
            new_ls.append(ls)
        return matrix(new_ls)

    def __len__(self):
        return len(self.matrix)

    def identity(n: int):
        new_ls = []
        for i in range(n):
            current_ls = []
            for j in range(n):
                if i == j:
                    current_ls.append(1)
                else:
                    current_ls.append(0)
            new_ls.append(current_ls)
        return matrix(new_ls)

    def is_row_matrix(self):
        if self.row == 1:
            return True
        else:
            return False

    def is_column_matrix(self):
        if self.column == 1:
            return True
        else:
            return False

    def is_horizontal_matrix(self):
        if self.column > self.row:
            return True
        else:
            return False

    def is_vertical_matrix(self):
        if self.column < self.row:
            return True
        else:
            return False

    def is_null_matrix(self):
        for i in range(0, self.row):
            for j in range(0, self.column):
                if self.matrix[i][j] != 0:
                    return False

        return True

    def is_square_matrix(self):
        if self.row == self.column:
            return True
        else:
            return False

    def is_idempotent(self):
        if self.is_square_matrix():

            if self * self == self:
                return True
            else:
                return False
        else:
            return False

    def is_involutory(self):
        if self * self == matrix.identity(self.row):
            return True
        else:
            return False

    def trace(self):
        if self.is_square_matrix():
            s = 0
            for i in range(0, self.row):
                s = s + self.matrix[i][i]
            return s
        else:
            sys.stderr.write('Trace not defined for a square matrix\n')

    def det(self):
        return det(self.matrix)

    def minor(self, row, column):
        row -= 1
        column -= 1
        return minor(self.matrix, row, column)

    def cofactor(self, row, column):
        return ((-1) ** (row + column)) * self.minor(row, column)

    def cofactor_matrix(self):
        matrix1 = matrix(list(self.matrix))
        cof_matrix = []
        for i in range(0, len(matrix1)):
            current_row = []
            for j in range(0, len(matrix1)):
                r = i + 1
                c = j + 1
                current_row.append(matrix1.cofactor(r, c))
            cof_matrix.append(current_row)

        return matrix(cof_matrix)

    def adjoint(self):
        return matrix(self.cofactor_matrix().transpose)

    def inverse(self):
        determinant=self.det()
        new_ls=[]
        for i in range(0,len(self.matrix)):
            current_ls=[]
            for j in range(0,len(self.matrix)):
                current_ls.append(self.adjoint().matrix[i][j]/determinant)
            new_ls.append(current_ls)

        return matrix(new_ls)






# # ls = [[2, 3],
# #       [4, 5]]
# # a = matrix(ls)
# # # print(a.matrix)
# # # print(a.cofactor(2,1))
# # print(a.cofactor_matrix())
# # # for i in range(0,len(ls)):
# # #     for j in range(len(ls)):
# # #         print(f'r,c = ({i+1},{j+1})')
# # #         print(a.cofactor(i+1,j+1))
#
# A=matrix([[1,2,3],[3,1,2],[4,1,4]])
# print(A.adjoint())
# print(A.det())
# print()
# print(A.inverse())