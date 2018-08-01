def get_index(x, last_answer, n):
    """
    This method returns the index based on the formula from the problem.
    :return:
    """
    return (x ^ last_answer) % n


def dynamic_array(n, queries):
    sequences = {}
    printed = []
    last_answer = 0

    for i in range(0, len(queries)):
        type, x, value = queries[i]
        if type == 1:
            # handle_type_1_query(n, x, last_answer, value, result)
            index = get_index(x, last_answer, n)
            if index not in sequences:
                sequences[index] = []
            sequences[index].append(value)
        elif type == 2:
            index = get_index(x, last_answer, n)
            seq = sequences[index]
            # last_answer = value % len(seq)
            last_answer = seq[value % len(seq)]
            printed.append(last_answer)

    # return [values[-1] for (key, values) in sequences.items()]
    return printed


if __name__ == '__main__':
    print(dynamic_array(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]))
