from Encoder.Compressor import *
import os
import time


def compressFile(inputpath, outputpath):
    open(outputpath, "w").close()
    compress(inputpath, outputpath)


def compressFolder(inputpath, outputpath):
    directory = os.fsencode(inputpath)
    open(outputpath, "w").close()
    for file in os.listdir(directory):
        filename = inputpath + "/" + os.fsdecode(file)
        compress(filename, outputpath)


def compressor(inputpath,outputpath):
    if os.path.isdir(inputpath):
        compressFolder(inputpath, outputpath)
    else:
        try:
            f = open(inputpath, "r")
            f.close()
        except IOError:
            print("Invalid Input/Output File Path...Please Try again\n")
            prompt()
        compressFile(inputpath, outputpath)


def prompt():
    inputpath = input("Please Enter A Full File Path:\n")
    choice = input("Would You Like To Compress Or Decompress This File: 1-Compress 2-Decompress\n")
    if choice == "1":
        start = time.time()
        compressor(inputpath, "Output/compressed_output.txt")
        end = time.time()
        print("Compression Ratio = " + str(os.path.getsize("Output/compressed_output.txt")/os.path.getsize(inputpath)))
        print("Execution time = " + str(end-start))
    elif choice == "2":
        start = time.time()
        decompress(inputpath, "Output/decompressed_output.txt")
        end = time.time()
        print("Execution time = " + str(end-start))
    else:
        print("Please read instructions carefully and try again")
        prompt()


prompt()
