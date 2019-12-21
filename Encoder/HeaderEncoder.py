from HuffmanCode.Huffman import *
import math


def headerWrite(huffmanTree,outputpath):
    code, headerSize = headerEncode(huffmanTree, "")
    header = int(code,2)
    f = open(outputpath,"ab")
    headerSize = math.ceil(headerSize / 8)
    byte = header.to_bytes(headerSize, byteorder='big', signed=False)
    f.write(byte)
    f.close()
    f = open(outputpath, "a")
    f.write("header")
    f.close()


def headerReader(f):
    r = bytes()
    test = f.read(1)
    if test is None:
        return None
    else:
        r += test
    while True:
        r += f.read(1)
        if len(r) == 0:
            return None
        try:
            if r[-6:].decode() == "header":
                break
        except UnicodeDecodeError:
            continue

    r = r[:-6]
    r = int.from_bytes(r, byteorder='big', signed=False)
    binary = bin(r)[2:]
    tree, i = headerDecode(binary)
    return tree





def headerEncode(huffmanTree, code, size = 0):
    if huffmanTree is None:
        return
    if huffmanTree.char is not None:
        code += "0"
        code += bin(ord(huffmanTree.char))[2:].zfill(8)
        size += 9
    else:
        code += "1"
        size += 1
        code, size = headerEncode(huffmanTree.left,code, size)
        code, size = headerEncode(huffmanTree.right,code, size)
    return code, size


#

def headerDecode(binary, i=0):
    if i >= len(binary):
        return None, i
    if binary[i] == "0":
        char = int(binary[i+1:i+9],2)
        char = str(chr(char))
        return HuffmanNode(0, char), i+9
    else:
        left, i = headerDecode(binary, i+1)
        right, i = headerDecode(binary, i)
        return HuffmanNode(0, None, left, right), i


