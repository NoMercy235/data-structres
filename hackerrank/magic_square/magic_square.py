from pprint import pprint as pp

import math


def print_matrix(matrix: [[int]]):
    for row in matrix:
        pp(row)


# def get_heat(position: (int, int), matrix: [[int]]):
#     (i, j) = position
#
#     col_sum = 0
#     for (row_i, row) in enumerate(matrix):
#         if row_i is not i:
#             col_sum += matrix[row_i][j]
#
#     row_sum = 0
#     for (col_j, col) in enumerate(matrix[i]):
#         if col_j is not j:
#             row_sum += matrix[i][col_j]
#
#     return row_sum - col_sum


def get_magic_constant(matrix: [[int]]):
    n = len(matrix)
    return n * math.floor((math.pow(n, 2) + 1)/2)


def get_next_up(current: int, n: int):
    return current - 1 if current - 1 >=0 else n - 1

def get_next_right(current: int, n: int):
    return current + 1 if current + 1 < n else 0

def get_next_left(current: int, n: int):
    return current - 1 if current - 1 >= 0 else n - 1

def get_next_down(current: int, n: int):
    return current + 1 if current + 1 < n else 0


def get_right(position: (int, int), n):
    return position[0], get_next_right(position[1], n)


def get_left(position: (int, int), n):
    return position[0], get_next_left(position[1], n)


def get_up(position: (int, int), n):
    return get_next_up(position[0], n), position[1]


def get_down(position: (int, int), n):
    return get_next_down(position[0], n), position[1]


def get_right_up(position: (int, int), n):
    return get_next_up(position[0], n), get_next_right(position[1], n)


def get_left_up(position: (int, int), n):
    return get_next_up(position[0], n), get_next_left(position[1], n)


def get_right_down(position: (int, int), n):
    return get_next_down(position[0], n), get_next_right(position[1], n)


def get_left_down(position: (int, int), n):
    return get_next_down(position[0], n), get_next_left(position[1], n)



# def check_right_up(expected_digit: int, position: (int, int), matrix: [[int]]):
#     n = len(matrix)
#     (i, j) = (get_next_up(position[0], n), get_next_right(position[1], n))
#     return matrix[i][j] == expected_digit
#
#
# def check_left_up(expected_digit: int, position: (int, int), matrix: [[int]]):
#     n = len(matrix)
#     (i, j) = (get_next_up(position[0], n), get_next_left(position[1], n))
#     return matrix[i][j] == expected_digit
#
#
# def check_right_down(expected_digit: int, position: (int, int), matrix: [[int]]):
#     n = len(matrix)
#     (i, j) = (get_next_down(position[0], n), get_next_right(position[1], n))
#     return matrix[i][j] == expected_digit
#
#
# def check_left_down(expected_digit: int, position: (int, int), matrix: [[int]]):
#     n = len(matrix)
#     (i, j) = (get_next_down(position[0], n), get_next_left(position[1], n))
#     return matrix[i][j] == expected_digit


def get_pos_of_digit(digit, matrix: [[int]]):
    for (i, row) in enumerate(matrix):
        for (j, col) in enumerate(matrix[i]):
            if col == digit:
                return i, j


def create_magic_matrix(position: (int, int), n, action, anti_action):
    matrix = [[0 for _ in range(0, n)] for _ in range(0, n)]
    matrix[position[0]][position[1]] = 1

    for i in range(1, int(math.pow(n, 2))):
        new_position = action(position, n)
        if matrix[new_position[0]][new_position[1]] != 0:
            position = anti_action(position, n)
        else:
            position = new_position
        matrix[position[0]][position[1]] = i + 1

    return matrix


def generate_heat_map(m, matrix):
    result = []
    n = len(m)
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.append(abs(m[i][j] - matrix[i][j]))
        result.append(row)
    return result


def get_matrix_abs_sum(matrix):
    result = 0
    n = len(matrix)
    for i in range(0, n):
        for j in range(0, n):
            result += abs(matrix[i][j])
    return result


def create_magic_square(matrix: [[int]]):
    n = len(matrix)
    actions = [get_left_up, get_left_up, get_right_up, get_right_up, get_right_down, get_right_down, get_left_down, get_left_down]
    anti_actions = [get_right, get_down, get_left, get_down, get_up, get_left, get_up, get_right]
    min_sum = 1000

    for (action_index, action) in enumerate(actions):
        for i in range(0, n):
            for j in range(0, n):
                m = create_magic_matrix((i, j), n, action, anti_actions[action_index])
                heat_map = generate_heat_map(m, matrix)
                sum = get_matrix_abs_sum(heat_map)
                if sum == 18:
                    heat_map = generate_heat_map(m, matrix)
                    sum = get_matrix_abs_sum(heat_map)
                min_sum = min_sum if sum > min_sum else sum
                if sum == 18:
                    print_matrix(m)
                    print('\n')

    return min_sum


if __name__ == '__main__':
    matrix = []
    # matrix.append([4, 8, 2])   # 4, 9, 2
    # matrix.append([4, 5, 7])   # 3, 5, 7
    # matrix.append([6, 1, 6])   # 8, 1, 6

    # matrix.append([5, 3, 4])
    # matrix.append([1, 5, 8])
    # matrix.append([6, 4, 2])

    # matrix.append([4, 9, 2])
    # matrix.append([3, 5, 7])
    # matrix.append([8, 1, 5])

    # matrix.append([5, 3, 4])
    # matrix.append([1, 5, 8])
    # matrix.append([6, 4, 2])

    matrix.append([4, 4, 7])
    matrix.append([3, 1, 5])
    matrix.append([1, 7, 9])
    print(create_magic_square(matrix))
