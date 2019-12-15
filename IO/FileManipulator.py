from Encoder.encode import *


class FileManipulator:
    def __init__(self,inputpath=None, outputpath=None):
        self.inputpath = inputpath
        self.outputpath = outputpath
        self.input_text = ""
        self.output_text = ""

    def read_file(self):
        try:
            f = open(self.inputpath, "r")
            open(self.outputpath, "w").close()
        except IOError:
            print("Invalid Input/Output File Path...Please Try again")
            return
        self.input_text = f.read()

    def write_file(self, x):
        try:
            f = open(self.outputpath, "ab")
        except IOError:
            print("Invalid Output File Path...Please Try again")
            return
        f.write(x)





