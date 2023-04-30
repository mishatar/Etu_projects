# Letter is node in Bin FGK tree
# Letter containing char is leaf
class Letter:
    def __init__(self, char="", left = None, right = None, parent = None):
        self.char = char
        self.count = 0
        self.code = ""
        self.left = left
        self.right = right
        self.parent = parent
    def __lt__(self, other):
        if isinstance(other, Letter): 
            return self.count < other.count

# Bin FGK tree for Dynamic Huffman
class FGKTree:
    def __init__(self):
        self.arr = [Letter(),]
    def rebuild(self, element):
        current = element
        while True:
            if not current: break
            parents, childs = [self.arr[0]], []
            end = False
            while not end:
                for letter in parents:
                    if letter.left: childs.append(letter.left)
                    if letter.right: childs.append(letter.right)

                    if letter == current:
                        end = True
                        break
                    if letter.count == current.count:
                        if(current.char and not letter.char): continue
                        if(letter.parent and letter.parent.right == letter): letter.parent.right = current
                        elif letter.parent: letter.parent.left = current
                        if(current.parent.right == current): current.parent.right = letter
                        else: current.parent.left = letter
                        current.parent, letter.parent = letter.parent, current.parent
                        end = True
                        break
                parents = childs
                childs = []
            current.count += 1
            current = current.parent
    def add(self, char):
        charNode = None
        for letter in self.arr:
            if letter.char == char:
                charNode = letter
                break

        if not charNode:
            nullNode = self.arr.pop()
            charNode = Letter(char)
            node = Letter("", charNode, nullNode)
            
            if nullNode.parent:
                nullNode.parent.left = node
                node.parent = nullNode.parent
            charNode.parent, nullNode.parent = node, node
            node.right, node.left = charNode, nullNode
            self.arr.extend([node, charNode, nullNode])           
        self.rebuild(charNode)
    def getCodes(self, dict, top = None, branch =''):
        current = top if top else self.arr[0]
        right, left = current.right, current.left
        current.code += branch
        if right:
            right.code = current.code
            self.getCodes(dict, right, '0')
        if left:
            left.code = current.code
            self.getCodes(dict, left, '1')
        if current.char:
            if(current.parent.left and not current.parent.left.count):
                dict[current.char] = current.parent.code
            else: dict[current.char] = current.code