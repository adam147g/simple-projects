from time import time
from random import randint


def printing(tic_tac_toe):
    for i in range(len(tic_tac_toe)):
        print(" ---", end="")
    print()
    for row in tic_tac_toe:
        print("|", end="")
        for col in row:
            if col == -1:
                print("   ", end="|")
            elif col == 0:
                print(" X ", end="|")
            else:
                print(" O ", end="|")
        print()

        for i in range(len(tic_tac_toe)):
            print(" ---", end="")
        print()


def check_win(tic_tac_toe, finish):
    n = len(tic_tac_toe)
    flag = False
    for row in range(n):
        count = 1
        if not flag:
            for col in range(n):
                if not flag:
                    if col + 1 < n and tic_tac_toe[row][col] == tic_tac_toe[row][col + 1] != -1:
                        count += 1
                    if count == finish:
                        flag = True

    if not flag:
        for col in range(n):
            count = 1
            if not flag:
                for row in range(n):
                    if not flag:
                        if row + 1 < n and tic_tac_toe[row][col] == tic_tac_toe[row + 1][col] != -1:
                            count += 1
                        if count == finish:
                            flag = True
    if not flag:
        for row in range(n):
            if not flag:
                for col in range(n):
                    count = 1
                    row_copy = row
                    col_copy = col
                    while row_copy + 1 < n and col_copy + 1 < n and not flag and tic_tac_toe[row_copy][col_copy] == \
                            tic_tac_toe[row_copy + 1][col_copy + 1] != -1:
                        row_copy += 1
                        col_copy += 1
                        count += 1
                        if count == finish:
                            flag = True
    if not flag:
        for row in range(n):
            if not flag:
                for col in range(n):
                    count = 1
                    row_copy = row
                    col_copy = col
                    while row_copy + 1 < n and col_copy - 1 > -1 and not flag and tic_tac_toe[row_copy][col_copy] == \
                            tic_tac_toe[row_copy + 1][col_copy - 1] != -1:
                        row_copy += 1
                        col_copy -= 1
                        count += 1
                        if count == finish:
                            flag = True
    if flag:
        return True
    return False


# N = int(input("N: "))
N = 3
tic_tac_toe = [[-1 for _ in range(N)] for _ in range(N)]
move = 0
printing(tic_tac_toe)
while not check_win(tic_tac_toe, N):
    row = int(input("row: "))
    col = int(input("col: "))
    if N > row > -1 and N > col > -1 and tic_tac_toe[row][col] == -1:
        if move % 2 == 0:
            tic_tac_toe[row][col] = 0
        else:
            tic_tac_toe[row][col] = 1
        move += 1
        printing(tic_tac_toe)
    else:
        print("Wrong data", end="\n\n")
if move % 2 == 1:
    print("First player won")
else:
    print("Second player won")
