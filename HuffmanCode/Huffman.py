from HuffmanCode.PriorityQueue import *


class HuffmanNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


def huffman(map):
    Q = PriorityQueue(map)
    for i in range(map.__len__() - 1):
        x = Q.heap_extract_min()
        y = Q.heap_extract_min()
        z = HuffmanNode(x.freq + y.freq, None)
        z.left = x
        z.right = y
        Q.insert(z)
    return Q.heap_extract_min()
