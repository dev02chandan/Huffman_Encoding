import copy,pickle,os

class node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq  # eg 1 / 2 / 3
        self.char = char  # eg 'a' , 'b'
        self.left = left
        self.right = right
        self.huffcode = ''  # 0/1 part


class huff:

    def isLeaf(root):
        return root.left is None and root.right is None

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
            huff.swap(A, i, smallest)
            huff.MinHeapify(A, smallest, n)
            return smallest

        return None

    def buildMinHeap(A):
        n = len(A)-1
        nonLeaf = n//2
        for i in range(nonLeaf, -1, -1):
            huff.MinHeapify(A, i, n)

    def extractMin(A):
        i = len(A)-1

        huff.swap(A, i, 0)     # Min is the first element

        min = A.pop(i)

        huff.MinHeapify(A, 0, len(A)-1)

        return min

    def HeapifyUp(A, i):

        if i == 0:
            return
        parent = (i-1)//2
        if(A[parent].freq > A[i].freq):
            huff.swap(A, i, parent)
            huff.HeapifyUp(A, parent)

    def Insert(A, val):

        A.append(val)

        # len(A)-1 will be the index of the last element
        huff.HeapifyUp(A, len(A)-1)

        return A

    def Huffman_code_table(Node, huffman_table, val=''):
        # huffman code for current node
        newVal = val + str(Node.huffcode)

        # if node is not an edge node
        # then traverse inside it
        if(Node.left):
            huff.Huffman_code_table(Node.left, huffman_table, newVal)
        if(Node.right):
            huff.Huffman_code_table(Node.right, huffman_table, newVal)

        if(huff.isLeaf(Node)):
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

        huff.buildMinHeap(Nodes)

        # till the time there is more than one node in the queue (to be extracted)
        while len(Nodes) != 1:

            # Removing the nodes with the lowest frequency in the queue

            left = huff.extractMin(Nodes)
            right = huff.extractMin(Nodes)

            left.huffcode = '0'
            # left node is marked 0
            right.huffcode = '1'
            # right node is marked 1

            # create a new internal node with these two nodes as children and
            # with a frequency equal to the sum of the two nodes' frequencies.
            # Push the node to the heap (and heapify) = Insert()

            total = left.freq + right.freq
            NewNode = node(total, None, left, right)
            huff.Insert(Nodes, NewNode)

        # root will hold the root node of the tree
        root = Nodes[0]

        # Huffman codes will be stored in a dictionary
        huffman_table = dict()

        # Using this function we will get huffman codes in the dictionary for every character
        huff.Huffman_code_table(root, huffman_table)

        Binary_Huffman_code = ""
        # This variable will hold the encoded text - in Huffman codes

        for i in text:
            Binary_Huffman_code += huffman_table.get(i)
        # Adding binary code for every character in the given text

        Compression_ratio = (len(text)*8)/len(Binary_Huffman_code)
        print("Compression Ratio = ", Compression_ratio)

        print("Huffman Table : ")
        print(huffman_table)

        return Binary_Huffman_code, huffman_table

    def Decoding_withTable(Binary_Huffman_Code, Table):
        # Binary Huffman Code is the Binary string
        # Table is a dictionary

        Decoded = ""

        Binary_Huffman_Code_Copy = copy.copy(Binary_Huffman_Code)

        Keys = Table.keys()
        Keys = list(Keys)
        Values = Table.values()
        Values = list(Values)

        char = ""

        while(len(Binary_Huffman_Code_Copy) != 0):

            if(char in Values):
                index = Values.index(char)
                Decoded += Keys[index]
                char = ""
                # If char is present in values - we get the index of char and check its key
                # That key is the char decoded
                # char is set back to 1

            else:
                char += Binary_Huffman_Code_Copy[0]
                Binary_Huffman_Code_Copy = Binary_Huffman_Code_Copy[1:]
                # char holds the binary code to compare in the values list
                # Binary Huffman Code copy gets first character sliced every time

        index = Values.index(char)
        Decoded += Keys[index]
        # Last character gets added to decoded

        return Decoded

    def read_file(file_path):
        file = open(file_path)
        file_text = file.read().replace("\n", " ")
        return file_text

    def make_output(filename, bin_data, huff_table):
        if not os.path.exists('output'):
            os.makedirs('output')

        output_path: str = 'output/' + filename + ".bin"

        with open(output_path, 'wb') as output:
            b = bytearray()
            for i in range(0, len(bin_data), 8):
                byte = bin_data[i:i + 8]
                b.append(int(byte, 2))

            output.write(bytes(b))
        print('Binary output created')

        # Storing dict as pkl file (best choice)
        with open('output'+"/" + filename + "_"+"Decompress_key.pkl", 'wb') as f:
            pickle.dump(huff_table, f, pickle.HIGHEST_PROTOCOL)

        print("decomp key done")

    def decompress(bin_path, pkl_path):
        with open(pkl_path, 'rb') as f:
            decomp_table = pickle.load(f)
        with open(bin_path, 'rb') as file:
            bit_string = ""
            byte = file.read(1)
            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

        return huff.Decoding_withTable(bit_string, decomp_table)
