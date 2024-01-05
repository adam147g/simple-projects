from time import perf_counter
def find_square_for_4x4(row, col, sudoku):
    n = len(sudoku)             # 4
    divide = n ** (1 / 2)       # 2
    if n / divide > row > -1:
        if n / divide > col > -1:
            return 0
        else:
            return 1
    else:
        if n / divide > col > -1:
            return 2
        else:
            return 3


def find_square_for_9x9(row, col, sudoku):
    n = len(sudoku)         # 9
    divide = n ** (1 / 2)   # 3
    if n / divide > row > -1:
        if n / divide > col > -1:
            return 0
        elif 2 * n / divide > col >= n / divide :
            return 1
        else:
            return 2
    elif 2 * n / divide > row >= n / divide:
        if n / divide > col > -1:
            return 3
        elif 2 * n / divide > col >= n / divide:
            return 4
        else:
            return 5
    else:
        if n / divide > col > -1:
            return 6
        elif 2 * n / divide > col >= n / divide:
            return 7
        else:
            return 8


def find_square(row, col, sudoku):
    n = len(sudoku)
    divide = n ** (1 / 2)
    for i in range(n):
        if (i + 1) * n / divide > row >= divide * i:
            row = i
            break
    for i in range(n):
        if (i + 1) * n / divide > col >= divide * i:
            return int(row * divide + i)



def fill_lists(sudoku, rows, cols, squares):
    for i_rows in range(len(sudoku)):
        for x in range(1, len(sudoku) + 1):
            if x not in sudoku[i_rows]:
                rows[i_rows].append(x)

    for i_cols in range(len(sudoku)):
        for x in range(1, len(sudoku) + 1):
            was = False
            for helping in range(len(sudoku)):
                if sudoku[helping][i_cols] == x:
                    was = True
            if not was:
                cols[i_cols].append(x)

    for i in range(len(sudoku)):
        for x in range(1, len(sudoku) + 1):
            squares[i].append(x)
    for row in range(len(sudoku)):
        for col in range(len(sudoku)):
            finded = find_square(row, col, sudoku)
            if sudoku[row][col] in squares[finded]:
                squares[finded].remove(sudoku[row][col])


def check(sudoku, rows, cols, squares):
    for i in range(len(rows)):
        if len(rows[i]) != 0 or len(cols[i]) != 0 or len(squares[i]) != 0:
            return False
    '''for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j]==0:
                return False
    '''
    return True


def sudoku_solver_backtracking(sudoku):
    rows = [[] for _ in range(len(sudoku))]  # możliwe do wpsania w wierszu
    cols = [[] for _ in range(len(sudoku))]  # możliwe do wpsania w kolumnie
    squares = [[] for _ in range(len(sudoku))]  # możliwe do wpsania w kwadratach

    # kwadraty w 4x4:
    # 0 1
    # 2 3
    #
    # kwadraty w 9x9:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    stop = False

    def make_magic(rows, cols, squares, sudoku, my_row, my_col, x, finded):
        nonlocal stop
        rows[my_row].remove(x)
        cols[my_col].remove(x)
        squares[finded].remove(x)
        sudoku[my_row][my_col] = x
        if check(sudoku, rows, cols, squares):
            stop = True
        if not stop:
            break_ = False
            new_row = my_row
            while new_row < (len(sudoku)):
                for new_col in range(len(sudoku)):
                    if sudoku[new_row][new_col] == 0 and not stop:
                        solve(sudoku, rows, cols, squares, new_row, new_col)
                        break_ = True
                    if break_:
                        break
                if break_:
                    break
                new_row+=1
        if not stop:
            rows[my_row].insert(0, x)
            cols[my_col].insert(0, x)
            squares[finded].insert(0, x)
            sudoku[my_row][my_col] = 0



    def solve(sudoku, rows, cols, squares, my_row, my_col):
        nonlocal stop
        if not stop:
            if not stop:
                finded = find_square(my_row, my_col, sudoku)
                if len(rows[my_row]) <= len(cols[my_col]) and len(rows[my_row]) <= len(squares[finded]):
                    for x in rows[my_row]:
                        if x in cols[my_col] and x in squares[finded]:
                            make_magic(rows, cols, squares, sudoku, my_row, my_col, x,finded)
                else:
                    if  len(cols[my_col]) <= len(squares[finded]):
                        for x in cols[my_col]:
                            if x in rows[my_row] and x in squares[finded]:
                                make_magic(rows, cols, squares, sudoku, my_row, my_col, x,finded)
                    else:
                        for x in squares[finded]:
                            if x in rows[my_row] and x in cols[my_col]:
                                make_magic(rows, cols, squares, sudoku, my_row, my_col, x,finded)

    fill_lists(sudoku, rows, cols, squares)
    for x in range(len(sudoku)):
        for y in range(len(sudoku)):
            if sudoku[x][y] == 0 and not stop:
                solve(sudoku, rows, cols, squares, x, y)



def if_is_solved(sudoku):
    n = len(sudoku)
    finish = 0
    for i in range(1, n + 1):
        finish += i
    for i in range(n):
        check = 0
        for j in sudoku[i]:
            check += j
        if finish != check:
            return False
    for i in range(n):
        check = 0
        for j in range(n):
            check += sudoku[j][i]
        if finish != check:
            return False

    return True


'''
N = 4
sudoku_1 = [[4, 3, 0, 0],
            [2, 1, 4, 3],
            [3, 4, 0, 2],
            [1, 2, 3, 4]]

sudoku_solver_backtracking(sudoku_1)
for i in range(N):
    print(sudoku_1[i])
print(if_is_solved(sudoku_1))
print()
sudoku_2 = [[0, 2, 0, 1],
            [0, 0, 0, 3],
            [0, 0, 3, 0],
            [4, 0, 0, 0]]
sudoku_solver_backtracking(sudoku_2)
for i in range(N):
    print(sudoku_2[i])
print(if_is_solved(sudoku_2))
print()

sudoku_4x4 = [[0] * 4 for _ in range(4)]
for row in range(4):
    for col in range(4):
        sudoku_4x4[row][col] = find_square_for_4x4(row,col,sudoku_4x4)
    print(sudoku_4x4[row])

print()



sudoku_9x9 = [[0] * 9 for _ in range(9)]
for row in range(9):
    for col in range(9):
        sudoku_9x9[row][col] = find_square_for_9x9(row,col,sudoku_9x9)
    print(sudoku_9x9[row])


print()

sudoku_4x4_generally = [[0] * 4 for _ in range(4)]
for row in range(4):
    for col in range(4):
        sudoku_4x4_generally[row][col] = find_square(row,col,sudoku_4x4_generally)
    print(sudoku_4x4_generally[row])

print()


sudoku_9x9_generally = [[0] * 9 for _ in range(9)]
for row in range(9):
    for col in range(9):
        sudoku_9x9_generally[row][col] = find_square(row,col,sudoku_9x9_generally)
    print(sudoku_9x9_generally[row])
'''


kluczowe=[
    [0,0,8,6,0,0,0,1,0],
[0,0,4,2,1,0,7,0,0],
[9,2,0,0,5,7,0,0,0],
[0,6,7,0,9,0,5,8,1],
[2,0,5,0,0,0,6,0,3],
[8,1,9,0,6,0,4,2,0],
[0,0,0,9,3,0,0,7,4],
[0,0,2,0,7,6,8,0,0],
[0,8,0,0,0,4,1,0,0],
    ]
start=perf_counter()
sudoku_solver_backtracking(kluczowe)
for i in range(len(kluczowe)):
    print(kluczowe[i])
print(if_is_solved(kluczowe))
print()
stop=perf_counter()
print(stop-start,"s")

'''
t = [[0] * 9 for _ in range(9)]
sudoku_solver_backtracking(t)
for i in range(len(t)):
    print(t[i])
print(if_is_solved(t))
print()


# poniższy trwa dwie i pół minuty - wpisując po kolei - nie zważając na to, czy w którymś kwadracie/kolumnie/wierszu
# nie brakuje np. tylko jednego - prawdopodobna możliwość optymalizacji

trudny_przypadek_z_neta = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,0,8,5],
    [0,0,1,0,2,0,0,0,0],
    [0,0,0,5,0,7,0,0,0],
    [0,0,4,0,0,0,1,0,0],
    [0,9,0,0,0,0,0,0,0],
    [5,0,0,0,0,0,0,7,3],
    [0,0,2,0,1,0,0,0,0],
    [0,0,0,0,4,0,0,0,9]
]
x = perf_counter()
sudoku_solver_backtracking(trudny_przypadek_z_neta)
for i in range(len(trudny_przypadek_z_neta)):
    print(trudny_przypadek_z_neta[i])
print(if_is_solved(trudny_przypadek_z_neta))
print()
y = perf_counter()
print(y - x,"s")'''