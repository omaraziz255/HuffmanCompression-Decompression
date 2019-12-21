from HuffmanCode.Huffman import *


class HuffmanCode:
    def __init__(self,inputpath):
        self.codes = dict()
        self.reversecodes = dict()
        self. frequencies = dict()
        self.huffman = None
        self.inputtext = open(inputpath, "r").read()

    def encoder(self, huffman_tree, code=''):
        if huffman_tree is None:
            return

        if huffman_tree.char is not None:
            self.codes[huffman_tree.char] = code
            return

        self.encoder(huffman_tree.left, code+'0')
        self.encoder(huffman_tree.right, code+'1')

    def encode(self):
        self.frequencies = hasher(self.inputtext)
        chars = []
        for k,v in self.frequencies.items():
            temp = HeapNode(k, v)
            chars.append(temp)
        self.huffman = huffman(chars)
        self.encoder(self.huffman)
        codePrinter(self.codes)
        self.reversecodes = {v: k for k, v in self.codes.items()}


def hasher(string):
    hash_map = dict()
    for c in string:
        if c in hash_map.keys():
            hash_map[c] += 1
        else:
            hash_map[c] = 1
    return hash_map


def codePrinter(codes):
    print("Byte          Code          New Code")
    print("------------------------------------")
    for k,v in codes.items():
        print(str(ord(k)).zfill(4)+"          "+bin(ord(k))[2:].zfill(8) + "      " + v + "\n")

