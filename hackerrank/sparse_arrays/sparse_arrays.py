from pprint import pprint as pp


def matching_strings(strings: [str], queries: [str]):
    # str_map = {key:value for key in strings for value in queries}
    str_map = {key: 0 for key in queries}
    for el in strings:
        if el not in str_map:
            str_map[el] = 0
        str_map[el] += 1

    return [str_map[el] for el in queries]


if __name__ == '__main__':
    strings = ['aba', 'baba', 'aba', 'xzxb']
    queries = ['aba', 'xzxb', 'ab']
    pp(matching_strings(strings, queries))
