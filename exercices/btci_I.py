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
