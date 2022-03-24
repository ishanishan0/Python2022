from ntpath import realpath
import os
from os import path

# set current path and results folder path
dir = os.getcwd()
folderDir = dir + "/results"

# setting up other variables
bytes = 0

# check if results folder already exists, if not create it. also open results.txt (create if needed)
resultsPath = os.path.join(folderDir, "results.txt")
if not os.path.exists(folderDir):
    os.makedirs("results")
resultsFile = open(resultsPath, "w+")

# put all file names into a list
fileList = os.listdir()
print(fileList)

# getting file sizes in bytes
for i in fileList:
    if os.path.isfile(i):
        currentSize = os.path.getsize(i)
        bytes += currentSize
        print("Current amount of bytes is ", str(bytes))

# writing the top of results.txt
resultsFile.write("Total bytecount: " + str(bytes) + "\n")
resultsFile.write("File list:\n")
resultsFile.write("-----------------\n")

# write file names to results.txt
for i in fileList:
    resultsFile.write(str(i) + "\n")