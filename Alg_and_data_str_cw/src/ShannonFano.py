import Heap
from functools import reduce

class Letter:
    def __init__(self, char, count):
        self.char = char
        self.count = count
        self.code = ""
    def __gt__(self, other):
        if isinstance(other, Letter): 
            if self.count != other.count: return self.count > other.count

def countLetters(string):
    alphabet = list(set(string))
    occurances = [0]*len(alphabet)

    for char in string:
        occurances[alphabet.index(char)] += 1

    letters = []
    for ch in range(len(alphabet)):
        letters.append(Letter(alphabet[ch], occurances[ch]))
    return letters

def heapSort(letters):
    heapSortedArr = []
    heap = Heap.Heap(letters, None)
    while heap.size():
        heapSortedArr.append(heap.pop())
    return heapSortedArr

def listReducer(sum, letter):
    return sum + letter.count

def encode(letters, dictionary, code = ''):
    if len(letters) == 1:
        dictionary[letters[0].char] = code
        return
    if len(letters) == 2:
        dictionary[letters[0].char] = code + '0'
        dictionary[letters[1].char] = code + '1'
        return
    
    indexLeft, indexRight = 0, len(letters)-1
    leftSum, rightSum = 0, 0
    left, right = [], []
    while indexLeft <= indexRight: 
        if(leftSum + letters[indexLeft].count < rightSum or not leftSum):
            leftSum += letters[indexLeft].count
            left.append(letters[indexLeft])
            indexLeft += 1
        else: 
            rightSum += letters[indexRight].count
            right.insert(0, letters[indexRight])
            indexRight -= 1
    encode(left, dictionary, code + '0')
    encode(right, dictionary, code + '1')

def ShannonFanoEncode(string, dictionary):
    letters = heapSort(countLetters(string))
    encode(letters, dictionary)

    code = ''
    for ch in string: code += dictionary[ch]
    return code

if(__name__=="__main__"):
    string = input()

    codes = dict()
    output = ShannonFanoEncode(string, codes)
    for ch in codes.keys():
        print(f'{ch}: {codes[ch]}')

    print(output, len(output))