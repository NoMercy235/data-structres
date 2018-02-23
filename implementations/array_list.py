class ArrayList:

    def __init__(self):
        self.list = []

    def insert(self, value):
        self.list.append(value)

    def remove(self, value):
        self.list.remove(value)

    def lookup(self, value):
        for el in self.list:
            if el == value:
                return el
        return None

    def to_string(self):
        return ' '.join(self.list)


if __name__ == '__main__':
    array = ArrayList()
    array.insert('ana')
    array.insert('are')
    array.insert('mere')
    print(array.to_string())
    print(array.lookup('are'))
    array.remove('are')
    print(array.to_string())
