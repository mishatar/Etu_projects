from FGKTree import FGKTree

def HuffmanEncode(string, codes):
    tree = FGKTree()
    for char in string:
        tree.add(char)

    tree.getCodes(codes)

    code = ''
    for ch in string: code += codes[ch]
    return code

if(__name__ == "__main__"):
    string = input()

    codes = dict()
    output = HuffmanEncode(string, codes)

    for ch in codes.keys():
        print(f'{ch}: {codes[ch]}')
    print(output, len(output))
