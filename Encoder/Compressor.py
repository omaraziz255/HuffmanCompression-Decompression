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
        if c.binary:
            char = str(chr(char))
        for bit in c.codes[char]:
            b.writeBit(bit)
    b.dumpBuffer()
    f = open(outputpath, "a")
    f.write("EOF")
    f.close()


def decompress(inputpath):
    f = open(inputpath, "rb")
    extension = inputpath[inputpath.find("."):]
    if extension != ".txt":
        binary = True
    else:
        binary = False
    counter = 0
    while 1:
        counter += 1
        outputpath = "Output/decompressedFile" + str(counter) + extension
        huffman = headerReader(f)
        if huffman is None:
            break
        codes = dict()
        generateCodes(huffman, codes)
        codes = {v: k for k, v in codes.items()}
        list = []
        while 1:
            text = f.read(1)
            if not text:
                break
            list.append(ord(text))
            if list[-3:] == [ord("E"), ord("O"), ord("F")]:
                print("Decompression of " + outputpath + " is done")
                list = list[:-3]
                break
        bS = ""
        for i in list:
            bS += '{0:08b}'.format(i)
        code = bS[0]
        open(outputpath, "w").close()
        if binary:
            file = open(outputpath, "ab")
            for char in bS[1:]:
                if code in codes.keys():
                    byte = ord(codes[code]).to_bytes(1, byteorder='big', signed=False)
                    file.write(byte)
                    code = ""
                code += char
        else:
            file = open(outputpath, "a")
            for char in bS[1:]:
                if code in codes.keys():
                    file.write(codes[code])
                    code = ""
                code += char




