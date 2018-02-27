import re


def has_unique_chars(string: str):
    """
    Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data
    structures?
    :param string: the string to check for uniqueness
    :return: boolean
    """

    chars = list(string)
    chars.sort()
    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            return False
    return True


def is_permutation(str1, str2):
    """
    Write a function which checks if a string is a permutation of another
    :param str1: first word
    :param str2: second word
    :return: boolean
    """

    chars = dict()

    def check_chars(ch, can_add, word_index):
        """

        :param ch: the character we're looking for
        :param can_add: boolean which states if we can add more items to the dict
        :param word_index: int to identify the word
        :return: void
        """
        if ch not in chars and can_add:
            chars[ch] = [False, word_index]
        else:
            chars[ch] = [True, word_index]

    n1 = len(str1)
    n2 = len(str2)
    for i in range(0, max(n1, n2)):
        if i < n1:
            check_chars(str1[i], i < n1, 1)
        if i < n2:
            check_chars(str2[i], i < n2, 2)

    word = None
    for ch in chars:
        if not chars[ch][0]:
            if word is None:
                word = chars[ch][1]
            elif word is not chars[ch][1]:
                return False
    return True


def palindrom_permutation(string: str):
    """
    Given a string, check if it is a permutation of a palindrom string.
    :param string: the string to check
    :return: boolean
    """
    string = re.sub(r'\W+', '', string.lower())

    chars = dict()
    for c in string:
        chars[c] = chars[c] + 1 if c in chars else 1

    almost_not_okey = False
    for val in chars.values():
        if val % 2 == 1:
            if not almost_not_okey:
                almost_not_okey = True
            else:
                return False

    if almost_not_okey:
        return len(string) % 2 == 1
    return True


def one_edit(str1: str, str2: str):
    """
    Write a function which checks if two string are 0 or 1 edit away
    :param str1: first string
    :param str2: second string
    :return: boolean
    """
    chars = dict()
    for i in range(max(len(str1), len(str2))):
        if i < len(str1):
            chars[str1[i]] = True if str1[i] in chars else False
        if i < len(str2):
            chars[str2[i]] = True if str2[i] in chars else False

    almost_not_okey = False
    for val in chars.values():
        if not val:
            if not almost_not_okey:
                almost_not_okey = True
            else:
                return False
    return True


def string_compression(string: str):
    """
    Compress a string like so: aabbbcccc -> a2b3c4; aaabc -> a3bc
    :param string: string to compress
    :return: str
    """
    def char_count(string: str, start_pos: int):
        c = string[start_pos]
        pos = start_pos + 1
        count = 1
        while pos < len(string):
            if string[pos] == c:
                count += 1
            else:
                break
            pos += 1
        return c, count, pos

    pos = 0
    final_string = ''
    has_changed = False
    while pos < len(string):
        char, found, tmp_pos = char_count(string, pos)
        final_string += char + str(found)
        pos = tmp_pos - 1
        if found > 1:
            has_changed = True
        pos += 1

    return final_string if has_changed else string


def zero_matrix(matrix):
    """
    If an element is 0, its entire row and column will be 0
    :param matrix: the matrix to check
    :return: int[][] result matrix
    """
    cols = []
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == 0:
                cols.append(col)
                matrix[row] = [0 for _ in range(0, len(matrix[row]))]
                break
    for col in cols:
        for row in range(0, len(matrix)):
            matrix[row][col] = 0
    return matrix


if __name__ == '__main__':
    print('======================== 1 ===============================')
    print('Not unique (this will not be unique): ' + str(has_unique_chars('this will not be unique')))
    print('Unique (this one): ' + str(has_unique_chars('this one')))

    print('======================== 2 ===============================')
    print('is permutation (ana, alina): ' + str(is_permutation('ana', 'alina')))
    print('is not permutation (animal, caramida): ' + str(is_permutation('animal', 'caramida')))

    print('======================== 4 ===============================')
    print('is a palindrome string (Tact CoA): ' + str(palindrom_permutation('Tact Coa')))
    print('is not a palindrom string (This cannot possibly be one): ' + str(palindrom_permutation('This cannot possibly be one')))

    print('======================== 5 ===============================')
    print('is one edit (pale, ple): ' + str(one_edit('pale', 'ple')))
    print('is one edit (pale, pales): ' + str(one_edit('pale', 'pales')))
    print('is one edit (paleX, pale): ' + str(one_edit('paleX', 'pale')))
    print('is not one edit (pale, bake): ' + str(one_edit('pale', 'bake')))

    print('======================== 6 ===============================')
    print('string compression (aabcccccaaa): ' + string_compression('aabcccccaaa'))
    print('string compression (abcd): ' + string_compression('abcd'))

    print('======================== 8 ===============================')
    print('zero matrix ([[1, 2, 3], [4, 0, 6], [7, 8, 9]]): ')
    print(zero_matrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))
    print('zero matrix ([[0, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 0]]): ')
    print(zero_matrix([[0, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 0]]))
