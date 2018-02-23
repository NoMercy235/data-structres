class HashTable:

    def __init__(self):
        self.table = dict()

    def insert(self, value):
        key = HashTable._generate_key(value)
        if key not in self.table:
            self.table[key] = [value]
        else:
            self.table[key].append(value)

    def lookup(self, value):
        key = HashTable._generate_key(value)
        for el in self.table[key]:
            if value == el:
                return el
        return None

    def remove(self, value):
        key = HashTable._generate_key(value)
        self.table[key].remove(value)

    @staticmethod
    def _generate_key(value):
        key = 0
        prev = 'a'
        for ch in value:
            key += ord(ch) % len(value) + ord(prev)
            prev = ch
        return key


if __name__ == '__main__':
    ht = HashTable()
    ht.insert('hello')
    ht.insert('world')
    print(ht.lookup('hello'))
    ht.remove('hello')
    ht.lookup('hello')
