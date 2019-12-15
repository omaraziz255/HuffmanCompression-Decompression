from Encoder.encode import *
from IO.BitWriter import *
from Encoder.HeaderEncoder import *


def generateCodes(huffman, codes, code=''):
    if huffman is None:
        return

    if huffman.char is not None:
        codes[huffman.char] = code
        return

    generateCodes(huffman.left,codes, code + '0')
    generateCodes(huffman.right,codes, code + '1')

def compress(inputpath, outputpath):
    c = HuffmanCode(inputpath)
    c.encode()
    headerWrite(c.huffman,outputpath)
    b = BitWriter(outputpath)
    for char in c.inputtext:
        for bit in c.codes[char]:
            b.writeBit(bit)
    b.dumpBuffer()



def decompress(inputpath,outputpath):
    f = open(inputpath, "rb")
    codes = dict()
    huffman = headerReader(f)
    generateCodes(huffman,codes)
    codes = {v:k for k,v in codes.items()}
    list = []
    while 1:
        text = f.read(1)
        if not text:
            break
        list.append(ord(text))
    bS = ""
    for i in list:
        bS += '{0:08b}'.format(i)
    code = bS[0]
    f = open(outputpath, "w")
    f = open(outputpath, "a")
    for char in bS[1:]:
        if code in codes.keys():
            f.write(codes[code])
            code = ""
        code += char




