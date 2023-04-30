from ShannonFano import ShannonFanoEncode
from huffmanStatic import HuffmanEncode as HuffmanEncodeStatic
from huffmanDynamic import HuffmanEncode as HuffmanEncodeDynamic

from time import time_ns as time
from functools import reduce
def countReducer(sum, code):
    return sum + len(code)

def decode(string, codes):
    outputString = ''
    codedChar = ''
    for char in string:
        codedChar += char
        if codedChar in codes.values():
            outputString += list(codes.keys())[list(codes.values()).index(codedChar)]
            codedChar = ''
    return outputString

if(__name__ == "__main__"):
    string = input()

    start = time()
    codesSF = dict()
    outputSF = ShannonFanoEncode(string, codesSF)
    decodeSF = decode(outputSF, codesSF)
    end = time()
    timeSF = (end - start)/(10**9)

    start = time()
    codesHS = dict()
    outputHS = HuffmanEncodeStatic(string, codesHS)
    decodeHS = decode(outputHS, codesHS)
    end = time()
    timeHS = (end - start)/(10**9)

    start = time()
    codesHD = dict()
    outputHD = HuffmanEncodeDynamic(string, codesHD)
    decodeHD = decode(outputHD, codesHD)
    end = time()
    timeHD = (end - start)/(10**9)

    tableLayout = "{:<8}| {:<15}| {:<15}| {:<15}"
    headers = tableLayout.format("Char", "SF", "HS", "HD")
    print("_"*len(headers))
    print(headers)
    print("_"*len(headers))

    for ch in codesSF.keys():
        print(tableLayout.format(ch, codesSF[ch], codesHS[ch], codesHD[ch]))

    print("_"*len(headers))
    print(tableLayout.format(
        "Total", 
        reduce(countReducer, codesSF.items(), 0), 
        reduce(countReducer, codesHS.items(), 0), 
        reduce(countReducer, codesHD.items(), 0))
    )
    print('')
    
    print("Shannon-Fano encoding:\n\tencoded:", outputSF, "\n\tlength:", len(outputSF), "\n\ttime:", timeSF, "\n\tdecoded:", decodeSF)
    print("Static Huffman encoding:\n\tencoded:", outputHS, "\n\tlength:", len(outputHS), "\n\ttime:", timeHS, "\n\tdecoded:", decodeHS)
    print("Dynamic Huffman encoding:\n\tencoded:", outputHD, "\n\tlength:", len(outputHD), "\n\ttime:", timeHD, "\n\tdecoded:", decodeHD)