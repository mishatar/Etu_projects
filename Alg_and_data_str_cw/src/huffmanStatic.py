import Heap

# Letter is node in bin Huffman tree
# Letter containing char is leaf 
class Letter:
    def __init__(self, char, count, left = None, right = None):
        self.char = char
        self.count = count
        self.code = ""
        self.left, self.right = left, right
    def __lt__(self, other):
        if isinstance(other, Letter): 
            if self.count != other.count: return self.count < other.count
            else:
                if other.char == "": return True
                elif self.char == "": return False
                else: return self.char < other.char

def countLetters(string):
    alphabet = list(set(string))
    occurances = [0]*len(alphabet)

    for char in string:
        occurances[alphabet.index(char)] += 1

    letters = []
    for ch in range(len(alphabet)):
        letters.append(Letter(alphabet[ch], occurances[ch]))
    return letters

def buildHuffmanTree(table):
    heap = Heap.Heap(table)
    while heap.size() > 1:
        left = heap.pop()
        right = heap.pop()
        heap.insert(Letter('', left.count + right.count, left, right))
    return heap.pop()

def buildCodes(top, chars, branch = ''):
    current = top
    right, left = current.right, current.left

    current.code += branch
    if right:
        right.code = current.code
        buildCodes(right, chars, '0')
    if left:
        left.code = current.code
        buildCodes(left, chars, '1')
    if current.char:
        chars[current.char] = current.code

def HuffmanEncode(string, dictionary):
    top = buildHuffmanTree(countLetters(string))
    buildCodes(top, dictionary)

    code = ''
    for ch in string: code += dictionary[ch]
    return code


if(__name__=="__main__"):
    string = input()

    codes = dict()
    output = HuffmanEncode(string, codes)
    for ch in codes.keys():
        print(f'{ch}: {codes[ch]}')

    print(output, len(output))
