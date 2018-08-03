from pprint import pprint as pp


def shift_left(array: [int], shift: int = 1):
    return array[shift:] + array[:shift]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    arr = shift_left(arr)
    pp(arr)
    arr = shift_left(arr)
    pp(arr)