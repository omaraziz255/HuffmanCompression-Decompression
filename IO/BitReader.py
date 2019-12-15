class BitReader:
    def __init__(self, filepath):
        self.file = open(filepath, "rb")
        self.value = ""
        self.bitcount = 0

    def readBit(self):
        if self.bitcount == 0:
            buffer = self.file.read(1)
            if not buffer:
                return None
            else:
                self.value = bin(ord(buffer))[2:]
        bit = self.value[self.bitcount]
        self.bitcount = (self.bitcount + 1) % 8
        return int(bit)

    def dumpBuffer(self):
        self.bitcount = 0
        self.value = ""
