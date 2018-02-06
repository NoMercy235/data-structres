"""
Reverse words in a sentence.
"""
import re


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def reverse_words(sentence: str):
    words = clean_sentence(sentence).split(' ')
    words.reverse()
    return ' '.join(words)


def clean_sentence(sentence: str) -> str:
    return re.sub('[^0-9a-zA-Z\s]+', '', sentence)


def reverse_with_stack(sentence: str, separator: str) -> Stack:
    words = Stack()
    characters = []

    for ch in sentence:
        if ch != separator:
            characters.append(ch)
        else:
            words.push(''.join(characters))
            characters = []
    words.push(''.join(characters))

    return words


if __name__ == '__main__':
    print(reverse_words('Ana are mere'))
    print(reverse_words('Ana are mere!!!'))

    words = reverse_with_stack('Ana are mere!!!', ' ')
    while not words.isEmpty():
        print(words.pop() + (' ' if not words.isEmpty() else ''), end='')
    print()
