from Encoder.Compressor import *
import os
import time


def compressFile(inputpath):
    extension = inputpath[inputpath.find("."):]
    outputpath = "Output/compressedFile" + extension
    open(outputpath, "w").close()
    compress(inputpath,outputpath)
    print("Compression Ratio = " + str(os.path.getsize(outputpath) / os.path.getsize(inputpath)))


def compressFolder(inputpath):
    directory = os.fsencode(inputpath)
    outputpath = "Output/compressedFolder.txt"
    open(outputpath, "w").close()
    inputsize = 0
    for file in os.listdir(directory):
        filename = inputpath + "/" + os.fsdecode(file)
        inputsize += os.path.getsize(filename)
        compress(filename,outputpath)
    print("Compression Ratio = " + str(os.path.getsize(outputpath) / inputsize))


def compressor(inputpath):
    if os.path.isdir(inputpath):
        compressFolder(inputpath)
    else:
        try:
            f = open(inputpath, "r")
            f.close()
        except IOError:
            print("Invalid Input/Output File Path...Please Try again\n")
            prompt()
            return
        compressFile(inputpath)


def prompt():
    inputpath = input("Please Enter A Full File Path:\n")
    choice = input("Would You Like To Compress Or Decompress This File: 1-Compress 2-Decompress\n")
    if choice == "1":
        start = time.time()
        compressor(inputpath)
        end = time.time()
        print("Execution time = " + str(end-start))
    elif choice == "2":
        start = time.time()
        decompress(inputpath)
        end = time.time()
        print("Execution time = " + str(end-start))
    else:
        print("Please read instructions carefully and try again")
        prompt()




prompt()
# decompressBinary("Output/compressed_output.txt", "Output/decompressed_output.txt")