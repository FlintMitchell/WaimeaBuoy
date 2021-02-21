import numpy as np
from matplotlib import pyplot as plt

# My first python program in a long while, aimed at re-establishing
# a couple python and signal processing concepts in my mind.
# Before starting I will use pyenv to create a python environment for the most recent python version
# and I will use virtualenv to create this project in it's own virtual environment.
# The first project will be to create a series of methods that:
# 1) Reads from a series of .txt files containing meteorological data from the Waimea Buoy. Use Numpy.
# 2) Concatenates each column of the csv into its own list
# 3) Plots the significant wave height data over time
# 4) Takes the Fourier transform of the significant wave height data both
#    as a whole and for each individual year and plots it

# ---------------- Start ----------------

# 1) Reads from a series of .txt files containing meteorological data from the Waimea Buoy. Use Numpy.

def readData(path):
    with open(path, 'r') as f:
        f.readline() # skip first line
        dataStart = len(f.readline()) # find starting point of data and point to it
        linelength = int(len(f.readline()))*2 # find length of the .txt file lines
        f.seek(dataStart) # point back to beginning of data
        numEntries = int(len(f.readlines()))# find number of entries
        f.seek(linelength)
        data = np.empty((numEntries,18)) # create data container with 17 rows and numEntries length
        columncounter = 0 # used to store in numpy array
        rowcounter = 0 # used to store in numpy array
        entryBuffer = '' # appends digits as they're read until they are ready to be added to the numpy array
        lastletter = '' # used to find out if a number has finished being ready
        for i in f.readlines():
            i = i.rstrip("\n") + ' '
            for ch in i:
                if ch != ' ':
                    entryBuffer = entryBuffer + ch
                elif ch == ' ' and lastletter ==' ':
                    continue
                elif ch == ' ' and lastletter != ' ':
                    data[rowcounter,columncounter] = float(entryBuffer) # add number to the array
                    entryBuffer = '' # reset the number stack
                    columncounter = columncounter + 1
                lastletter = ch
            columncounter = 0
            rowcounter = rowcounter + 1
    return data # return numpy array with all the buoy associated data

# 2) Concatenates each column of the csv into its own list
def concatData(listOfArrays):
    finalArray = listOfArrays[0]
    for i in listOfArrays[1:]:
        finalArray = np.concatenate((finalArray,i))
    return finalArray

# 3) Plots the significant wave height data over time
def plotThatShit(x,y):
    plt.title("Signigicant Wave Height from 2007-2019 at the Waimea Buoy")
    plt.xlabel("Date")
    plt.ylabel("Significant Wave Height (m)")
    plt.plot(x,y)
    plt.show()

def main():
    # iterate through all .txt files, append returned numpy array to a list
    listOfArrays = list()
    # for i in [7,8,9]:
    #     listOfArrays.append(readData('/Users/flintmitchell/python-projects/waimea-buoy/NDBC_data/51201h200' + str(i) + '.txt'))
    for i in range(13,20,1):
        listOfArrays.append(readData('/Users/flintmitchell/python-projects/waimea-buoy/NDBC_data/51201h20' + str(i) + '.txt'))
    allData = concatData(listOfArrays)
    #clean up step
    plotThatShit(x = range(0,len(allData[:,8])),y = allData[:,8])
    # pass list of arrays to concatData() to return one concatenated array

if __name__ == "__main__":
    main()

# 4) Takes the Fourier transform of the significant wave height data both
#    as a whole and for each individual year and plots it
