def pick_numbers(arr: [int]):
    sorted = arr
    sorted.sort()

    res_stack = []
    prev_el = sorted[0]
    count = 1
    for el in sorted[1:]:
        if el is prev_el:
            count += 1
        elif el is not prev_el:
            can_link = abs(el - prev_el) <= 1
            res_stack.append(dict(key=prev_el, count=count, can_link=can_link))
            count = 1
        prev_el = el

    found = False
    for el in res_stack:
        if prev_el == el.get('key'):
            res_stack['key'] += 1
            found = True
    if not found:
        res_stack.append(dict(key=prev_el, count=count, can_link=False))

    if len(res_stack) == 1:
        return res_stack[0].get('count')

    max_sum = 0
    prev_el = res_stack[0]
    for el in res_stack[1:]:
        current_sum = prev_el.get('count') if prev_el.get('can_link') is False else prev_el.get('count') + el.get('count')
        max_sum = max(max_sum, current_sum)
        prev_el = el
    return max_sum


if __name__ == '__main__':
    # print(pick_numbers([1, 2, 2, 3, 4, 1]))
    print(pick_numbers([66, 66, 66, 66, 66]))
