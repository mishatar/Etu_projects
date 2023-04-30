from numpy import log2
from ShannonFano import ShannonFanoEncode
from huffmanStatic import HuffmanEncode as HuffmanEncodeStatic
from huffmanDynamic import HuffmanEncode as HuffmanEncodeDynamic
from time import time_ns as time
import matplotlib.pyplot as plt

string = "☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz"
length = 500

def measureTime(func, string, codes):
    start = time()
    func(string, codes)
    end = time()
    return (end - start)/(10**9)

if __name__ == "__main__":
    print("Time measurements")
    print("Initial string:", string)
    print("Number of repetitions:", length)
    timings = [[],[],[]]
    codes = dict()
    for n in range(1, len(string)):
        print("Step:", n+1, "\tSymbols:", (n+1)*length)
        strToEncode = string[:n]*length
        timings[0].append(measureTime(ShannonFanoEncode, strToEncode, codes))
        timings[1].append(measureTime(HuffmanEncodeStatic, strToEncode, codes))
        timings[2].append(measureTime(HuffmanEncodeDynamic, strToEncode, codes))

    xCoord = range(1, len(string))
    yCoord = timings[0]
    plt.scatter(xCoord, yCoord)
    plt.plot(xCoord, yCoord)
    a = (yCoord[-1]+yCoord[-2])/2/xCoord[-1]/log2(xCoord[-1])
    yCoord = [a*x*log2(x) for x in xCoord]
    plt.plot(xCoord, yCoord)
    plt.savefig("SF.png")
    plt.clf()

    yCoord = timings[1]
    plt.scatter(xCoord, yCoord)
    plt.plot(xCoord, yCoord)
    a = (yCoord[-1]+yCoord[-2])/2/xCoord[-1]/log2(xCoord[-1])
    yCoord = [a*x*log2(x) for x in xCoord]
    plt.plot(xCoord, yCoord)
    plt.savefig("HS.png")
    plt.clf()

    yCoord = timings[2]
    plt.scatter(xCoord, yCoord)
    plt.plot(xCoord, yCoord)
    a = yCoord[-1]/xCoord[-1]**2
    yCoord = [a*x**2 for x in xCoord]
    plt.plot(xCoord, yCoord)
    plt.savefig("HD.png")
    plt.clf()

    print("Finished")
