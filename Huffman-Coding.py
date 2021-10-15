import copy


def isLeaf(root):
    return root.left is None and root.right is None


class node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq  # eg 1 / 2 / 3
        self.char = char  # eg 'a' , 'b'
        self.left = left
        self.right = right
        self.huffcode = ''  # 0/1 part


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def MinHeapify(A, i, n):
    left = 2*i + 1
    right = 2*i + 2

    if(left <= n and A[left].freq < A[i].freq):
        smallest = left
    else:
        smallest = i

    if (right <= n and A[right].freq < A[smallest].freq):
        smallest = right

    if (smallest != i):
        swap(A, i, smallest)
        MinHeapify(A, smallest, n)
        return smallest

    return None


def buildMinHeap(A):
    n = len(A)-1
    nonLeaf = n//2
    for i in range(nonLeaf, -1, -1):
        MinHeapify(A, i, n)


def extractMin(A):
    i = len(A)-1

    swap(A, i, 0)     # Min is the first element

    min = A.pop(i)

    MinHeapify(A, 0, len(A)-1)

    return min


def HeapifyUp(A, i):
    parent = (i-1)//2
    if(A[parent].freq > A[i].freq):
        swap(A, i, parent)
        HeapifyUp(A, parent)


def Insert(A, val):

    A.append(val)

    HeapifyUp(A, len(A)-1)  # len(A)-1 will be the index of the last element

    return A


def Huffman_code_table(Node, huffman_table, val=''):
    # huffman code for current node
    newVal = val + str(Node.huffcode)

    # if node is not an edge node
    # then traverse inside it
    if(Node.left):
        Huffman_code_table(Node.left, huffman_table, newVal)
    if(Node.right):
        Huffman_code_table(Node.right, huffman_table, newVal)

    if(isLeaf(Node)):
        char = Node.char
        huffman_table[char] = newVal
        # Adding values to the dict


def Huffman(text):
    if len(text) == 0:
        return

    # Making a set of the text - set holds only unique elements
    char = set(text)
    freq = {}
    for i in char:
        freq[i] = text.count(i)

    Nodes = []

    for char, frequency in freq.items():
        # Here we are appending every char and their frequency as a node in a list called Nodes
        Nodes.append(node(frequency, char))

    buildMinHeap(Nodes)

    # till the time there is more than one node in the queue (to be extracted)
    while len(Nodes) != 1:

        # Removing the nodes with the lowest frequency in the queue

        left = extractMin(Nodes)
        right = extractMin(Nodes)

        left.huffcode = '0'
        # left node is marked 0
        right.huffcode = '1'
        # right node is marked 1

        # create a new internal node with these two nodes as children and
        # with a frequency equal to the sum of the two nodes' frequencies.
        # Push the node to the heap (and heapify) = Insert()

        total = left.freq + right.freq
        NewNode = node(total, None, left, right)
        Insert(Nodes, NewNode)

    # root will hold the root node of the tree
    root = Nodes[0]

    # Huffman codes will be stored in a dictionary
    huffman_table = dict()

    # Using this function we will get huffman codes in the dictionary for every character
    Huffman_code_table(root, huffman_table)

    Binary_Huffman_code = ""
    # This variable will hold the encoded text - in Huffman codes

    for i in text:
        Binary_Huffman_code += huffman_table.get(i)
    # Adding binary code for every character in the given text

    Compression_ratio = (len(text)*8)/len(Binary_Huffman_code)

    Binary_Huffman_code = int(Binary_Huffman_code, base=2)

    print("Huffman Table : ")
    print(huffman_table)

    print("Binary Huffman Code: ")
    print(Binary_Huffman_code)

    print("Compression Ratio = ", Compression_ratio)

    return Binary_Huffman_code, huffman_table, root


def Decoding(Binary_Huffman_code, root):

    # There is a special case where every single character is the same
    # Hence there is no tree
    # Eg. ccccc
    # For that special case - if the root is only a leaf node (no tree)
    # Decoded String will hold the final answer
    Decoded = ""
    if(isLeaf(root)):
        while(root.freq > 0):
            print(root.ch, end="")
            Decoded += root.ch
            root.freq -= 1

    else:
        # traversing the entire huffman tree to decode the encoded string
        # Creating a copy of the Binary code (Encoded in Huffman)

        Binary_Huffman_codeCopy = copy.copy(Binary_Huffman_code)

        # Creating a copy of the root node (as the traversal node)
        # This node will be used to traverse the entire tree to find the correct character
        rootCopy = copy.copy(root)

        # If the traversal node is become a leaf node,
        # we add the char value of the leaf node to the decoded string
        # After adding the character - traversal node = root node

        while(len(Binary_Huffman_codeCopy) != 0):
            if(isLeaf(rootCopy)):
                Decoded += rootCopy.char
                rootCopy = copy.copy(root)

            # If the next number in the code is 0 - then Check Left part in the tree
            # After changing the traversal node - we remove the first element from the String

            elif(Binary_Huffman_codeCopy[0] == '0'):
                rootCopy = rootCopy.left
                Binary_Huffman_codeCopy = Binary_Huffman_codeCopy[1:]
                continue

            # If the next number in the code is 1 - then Check right part in the tree
            # After changing the traversal node - we remove the first element from the String
            elif(Binary_Huffman_codeCopy[0] == '1'):
                rootCopy = rootCopy.right
                Binary_Huffman_codeCopy = Binary_Huffman_codeCopy[1:]
                continue

        Decoded += rootCopy.char
        # Since the last iteration for addition of the last character is missed out

    return Decoded


if __name__ == "__main__":
    myInput = input("Enter text: ")
    # myInput = "AB CDBCD ABBAB E"
    Binary, Table, root = Huffman(myInput)
    # print("Decoded String is: ", Decoding(Binary, root))
