class node:
    def __init__(self , val):
        self.left = None
        self.right = None
        self.value = val

def inorder(node):
    if node:
        inorder(node.left)

        print(node.value)

        inorder(node.right)

def preorder(node):
    if node:
        print(node.value)

        preorder(node.left)

        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)

        postorder(node.right)

        print(node.value)
    



# code = input("Enter a string: ")
code = "ABCDBCDABBABE"                                       # For testing only
char = []                                                    # This list will hold distinct elements from the given string
for i in code:
    if i not in char:
        char.append(i) 
        
charCount = []                                               # This list will hold Frequency of each element in the char list
for i in char:
    charCount.append(code.count(i))

print(char , "\t" , charCount) 

while(len(charCount)>1):                                     # While there are atleast two elements in the list - we can continue finding the two minimum elements

    min1Index = charCount.index(min(charCount))              #Take Minimum Element from the frequency list and get the Index of the minimum element (first occurence)

    Node4 = None
    Node5 = None

    if (type(char[min1Index])==str):                         # This denotes that the character is not a Node
        min1 = charCount.pop(min1Index)                      # Popout the frequency of the element

        Node1 = node(char[min1Index])                        # Make min1 a node with value = char[min1Index] Eg. 'A'
        char.pop(min1Index)                                  # popping the element from characters out as well
    
    else:                                                    # if the item in the list is a node
        Node4 = char[min1Index]                              # Assigning that node to Node4
        min1 = charCount.pop(min1Index)                      # Popout the frequency of the element
        char.pop(min1Index)                                  # popping the element from characters out as well


    #Similarly for the second largest element 

    min2Index = charCount.index(min(charCount))

    if (type(char[min2Index])==str): 
        min2 = charCount.pop(min2Index)

        Node2 = node(char[min2Index])
        char.pop(min2Index)

    else:                                                    
        Node5 = char[min2Index]                              
        min2 = charCount.pop(min2Index)                      
        char.pop(min2Index)

    # Make a new node with value = min1 + min2

    Sum = min1 + min2

    Node3 = node(Sum)

    if (Node4 == None):                     
        Node3.left = Node1

    else:                                   # This signifies that min1 was a node and hence we add Node4 as the left of the new node
        Node3.left = Node4

    if (Node5 == None):
        Node3.right = Node2 
    
    else: 
        Node3.right = Node5                 # This signifies that min2 was a node and hence we add Node5 as the left of the new node
        
    charCount.append(Sum)
    char.append(Node3)

    print(char , "\t" , charCount) 


# At the end of the while loop we have the root node only in the char list

print("Inorder : " , inorder(char[0]))
print("Preorder: " , preorder(char[0]))
print("Postorder: " , postorder(char[0]))
