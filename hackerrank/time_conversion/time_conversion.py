def time_conversion(s):
    offset = 12 if s[-2:] == 'PM' else 0
    time_parts = s[:-2].split(':')
    # if offset:
    new_hour = int(time_parts[0]) + offset
    new_hour = new_hour if new_hour not in [12, 24] else 0 if new_hour == 12 else 12
    # new_hour = new_hour if new_hour < 24 else 0
    time_parts[0] = str(new_hour) if new_hour > 9 else '0' + str(new_hour)
    return ':'.join(time_parts)


if __name__ == '__main__':
    time_conversion('12:00:00AM')
