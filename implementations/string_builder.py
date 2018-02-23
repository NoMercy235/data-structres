class StringBuilder:

    def __init__(self):
        self.strings = []

    def append(self, string):
        self.strings.append(string)

    def to_string(self):
        return ' '.join(self.strings)


if __name__ == '__main__':
    sb = StringBuilder()
    sb.append('Hello,')
    sb.append('world!')
    print(sb.to_string())
