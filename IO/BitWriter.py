class BitWriter:
    def __init__(self, filepath):
        # open(filepath, "w").close()
        self.file = open(filepath, "ab")
        self.buffer = 0
        self.bitcount = 0

    def writeBit(self, bit):
        if self.bitcount == 0:
            self.buffer = (self.buffer | (int(bit) << 7))
        else:
            self.buffer = (ord(chr(self.buffer)) | int(bit) << (7 - (self.bitcount % 8)))
        self.bitcount += 1
        if self.bitcount == 8:
            self.bitcount = 0
            binary = self.buffer.to_bytes(1, byteorder='big', signed=False)
            self.file.write(binary)
            self.buffer = 0

    def dumpBuffer(self):
        self.file.write(self.buffer.to_bytes(1, byteorder='big', signed=False))
        self.buffer = self.bitcount = 0
