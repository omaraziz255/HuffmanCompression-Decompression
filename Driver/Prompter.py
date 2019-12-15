from Encoder.Compressor import *
import os
import time


def prompt():
    inputpath = input("Please Enter A Full File Path:\n")
    try:
        f = open(inputpath, "r")
        f.close()
    except IOError:
        print("Invalid Input/Output File Path...Please Try again\n")
        prompt()
    choice = input("Would You Like To Compress Or Decompress This File: 1-Compress 2-Decompress\n")
    if choice == "1":
        start = time.time()
        compress(inputpath, "IO/compressed_output.txt")
        end = time.time()
        print("Compression Ratio = " + str(os.path.getsize("IO/compressed_output.txt")/os.path.getsize(inputpath)))
        print("Execution time = " + str(end-start))
    elif choice == "2":
        start = time.time()
        decompress(inputpath, "IO/decompressed_output.txt")
        end = time.time()
        print("Execution time = " + str(end-start))
    else:
        print("Please read instructions carefully and try again")
        prompt()


prompt()

