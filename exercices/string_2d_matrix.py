"""
Given 2d matrix and a string. Write a function to check if string is contained in the 2d matrix.
"""


def axis_correct(val, val_includes: []) -> bool:
    return val in val_includes if len(val_includes) != 0 else True


def within_bounds(matrix, start: int, offset: int, axis: str):
    if matrix is None:
        return False

    if axis == 'x':
        return 0 <= start + offset < len(matrix[0])
    elif axis == 'y':
        return 0 <= start + offset < len(matrix)
    else:
        return False


def check_up(matrix, sequence, start_x, start_y):
    if within_bounds(matrix, start_y, -len(sequence) + 1, 'y'):
        okey = True
        for i in range(0, len(sequence)):
            if matrix[start_y - i][start_x] != sequence[i]:
                okey = False
        return okey
    else:
        return False


def check_down(matrix, sequence, start_x, start_y):
    if within_bounds(matrix, start_y, len(sequence) - 1, 'y'):
        okey = True
        for i in range(0, len(sequence)):
            if matrix[start_y + i][start_x] != sequence[i]:
                okey = False
        return okey
    else:
        return False


def check_left(matrix, sequence, start_x, start_y):
    if within_bounds(matrix, start_x, -len(sequence) + 1, 'x'):
        okey = True
        for i in range(0, len(sequence)):
            if matrix[start_y][start_x - i] != sequence[i]:
                okey = False
        return okey
    else:
        return False


def check_right(matrix, sequence, start_x, start_y):
    if within_bounds(matrix, start_x, len(sequence) - 1, 'x'):
        okey = True
        for i in range(0, len(sequence)):
            if matrix[start_y][start_x + i] != sequence[i]:
                okey = False
        return okey
    else:
        return False


def search_sequence(matrix, sequence: str, x_includes: [], y_includes: []):
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
            if axis_correct(row, x_includes) and axis_correct(col, y_includes):
                if matrix[row][col] == sequence[0] and \
                   (check_up(matrix, sequence, col, row) or check_down(matrix, sequence, col, row) or
                   check_left(matrix, sequence, col, row) or check_right(matrix, sequence, col, row)):
                    return True
    return False


if __name__ == '__main__':
    matrix = [
        ['w', 'x', 'a', 'a', ],
        ['w', 'e', 'a', 'a', ],
        ['e', 'l', 'a', 'a', ],
        ['x', 'a', 'a', 'a', ],
    ]
    sequence = 'alex'

    print('Up: ' + str(search_sequence(matrix, sequence, [], [0, 2])))

    matrix = [
        ['a', 'w', 'a', 'a', ],
        ['l', 'w', 'a', 'a', ],
        ['e', 'w', 'a', 'a', ],
        ['x', 'a', 'a', 'a', ],
    ]
    sequence = 'alex'

    print('Down: ' + str(search_sequence(matrix, sequence, [], [])))

    matrix = [
        ['x', 'e', 'l', 'a', ],
        ['l', 'e', 'a', 'a', ],
        ['e', 'l', 'a', 'a', ],
        ['x', 'a', 'a', 'a', ],
    ]
    sequence = 'alex'

    print('Left: ' + str(search_sequence(matrix, sequence, [0, 1, 3], [])))

    matrix = [
        ['a', 'w', 'a', 'a', ],
        ['l', 'w', 'a', 'a', ],
        ['a', 'l', 'e', 'x', ],
        ['x', 'a', 'a', 'a', ],
    ]
    sequence = 'alex'

    print('Right: ' + str(search_sequence(matrix, sequence, [], [])))
