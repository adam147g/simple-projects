from random import randint
from time import time


def print_matrix(matrix):
    i = 0
    print("      ", end="")
    while i < len(matrix):
        print(i, end="   ")
        i += 1
    print()
    print("     ", end="")
    i = 0
    while i < len(matrix):
        print("--- ", end="")
        i += 1
    print()
    i = 0
    while i < len(matrix):
        print(i, end="|\t")
        for col in range(len(matrix)):
            if matrix[i][col][1]:
                print("|", matrix[i][col][0], end="\t")
            else:
                print("| ", end="\t")
        print("|", end="\n")
        print("     ", end="")
        x = 0
        while x < len(matrix):
            print("--- ", end="")
            x += 1
        print()
        i += 1
    print()


def make_matrix(N, bombs):
    matrix = [[[0, False]] * N for _ in range(N)]
    i = 0
    while i < bombs:
        row = randint(0, N - 1)
        col = randint(0, N - 1)
        if matrix[row][col][0] != 'X':
            matrix[row][col] = ['X', False]
            i += 1

    def sum(matrix, row, col):
        count = 0
        n = len(matrix)
        if row - 1 > -1:
            if matrix[row - 1][col][0] == 'X':
                count += 1
        if row - 1 > -1 and col - 1 > -1:
            if matrix[row - 1][col - 1][0] == 'X':
                count += 1
        if col - 1 > -1:
            if matrix[row][col - 1][0] == 'X':
                count += 1
        if row + 1 < n and col - 1 > -1:
            if matrix[row + 1][col - 1][0] == 'X':
                count += 1
        if row + 1 < n:
            if matrix[row + 1][col][0] == 'X':
                count += 1
        if row + 1 < n and col + 1 < n:
            if matrix[row + 1][col + 1][0] == 'X':
                count += 1
        if col + 1 < n:
            if matrix[row][col + 1][0] == 'X':
                count += 1
        if row - 1 > -1 and col + 1 < n:
            if matrix[row - 1][col + 1][0] == 'X':
                count += 1
        return count

    for row in range(N):
        for col in range(N):
            if matrix[row][col][0] != 'X':
                matrix[row][col] = [sum(matrix, row, col), False]
    return matrix


def check(matrix, bombs):
    falces = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if not matrix[row][col][1]:
                falces += 1
    if falces == bombs:
        return False
    return True


def show_zeros(matrix, row, col):
    if matrix[row][col][0] == 0:
        matrix[row][col][1] = True
        new_row = [row - 1, row + 1, row, row]
        new_col = [col, col, col - 1, col + 1]
        for i in range(len(new_row)):
            if 0 <= new_row[i] < len(matrix) and 0 <= new_col[i] < len(matrix):
                x = matrix[new_row[i]][new_col[i]]
                if not x[1]:
                    show_zeros(matrix, new_row[i], new_col[i])


def after_showing_zeros(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col][0] == 0 and matrix[row][col][1]:
                for add_row in range(-1, 2):
                    for add_col in range(-1, 2):
                        if len(matrix) > row + add_row > -1 and len(matrix) > col + add_col > -1:
                            matrix[row + add_row][col + add_col][1] = True



N = int(input(">> Rozmiar tablicy: "))
bombs = int(input(">> Ilość bomb: "))
if bombs >= N ** 2:
    exit("Złe dane")
print("Szanse na trafienie bomby: ", 10 * round(bombs / (N * N), 3), "%")
matrix = make_matrix(N, bombs)
print_matrix(matrix)
start = time()

while check(matrix, bombs):
    row = int(input("row: "))
    col = int(input("col: "))
    if not matrix[row][col][1]:
        if matrix[row][col][0] == 'X':
            matrix[row][col][1] = True
            print_matrix(matrix)
            stop = time()
            print("No niestety", stop - start, "s")
            exit(-1)
        elif matrix[row][col][0]:
            matrix[row][col][1] = True
        else:
            show_zeros(matrix, row, col)
            after_showing_zeros(matrix)
        print_matrix(matrix)
    else:
        print("Change move, there was this move")
stop = time()
print("Gratulacje!!!", stop - start, "s")
