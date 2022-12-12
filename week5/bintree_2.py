# Adding remove and searchSmallest methods to the bintree_1.py     

class Node:

    def __init__(self, key: int):
        self.data = key
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    # Inserts a new key to the search tree without duplicates
    def insert(self, key):
        nodeNew = Node(key) 
    
        if self.root == None:
            self.root = nodeNew
            return

        nodeCurrent = self.root
        nodePrevious = None

        while (nodeCurrent != None):            # If the next number is smaller than current node's number, 
            if (nodeCurrent.data < key):        # we will put the new number on the left side of the previous number
                nodePrevious = nodeCurrent
                nodeCurrent = nodeCurrent.right

            elif (nodeCurrent.data > key):      # same as above but the new number goes left. 
                nodePrevious = nodeCurrent
                nodeCurrent = nodeCurrent.left  # this while -loop searches the right place/node for the key value
        
        if (nodePrevious.data < key):           # Inserting the number at it's right node
            nodePrevious.right = nodeNew
        
        else: 
            nodePrevious.left = nodeNew

    
    # I've used the lecture materials in help of creating the search functions. 
    # Searches the key from the search tree and returns True/False if the value is found/not found.      
    def search(self, key):
        return self.searchHelp(self.root, key)
    
    def searchHelp(self, node, key):
        if node == None:                                
            return False

        if node.data > key:
            if (node.data == key):                      # If the number in the node is same as the value searched
                return                                  # it returns from the loop and returns True as wanted
            return self.searchHelp(node.left, key)

        elif node.data < key:
            if (node.data == key):
                return
            return self.searchHelp(node.right, key)
        return True


    # In preorder we visit the left branch of the root node until the leaf (until the nodes are null), then we change the 
    # branch to the right one and so on. 

    def preorder(self):
        self.preorderHelp(self.root)         # root = node
        print("")

    def preorderHelp(self, node):
        if (node == None):
            return

        print(node.data, end=" ")   	    # printing every number

        self.preorderHelp(node.left)            
        self.preorderHelp(node.right)
            
    # Removes the node wich has the given key value while maintaining the binary search tree 
    def remove(self, key, node=-1): 
        if (node == -1):                    # set default value if no second argument is given
            node = self.root
        
        if (node == None):
            return node
        
        if (node.data == key):              # finds the node to be removed

            if (node.left == None):         # Checks if the left child exists
                node = node.right
            
            elif (node.right == None):      # Checks if the right child exists
                node = node.left

            else:                           # Otherwise it has children
                smallest = self.searchSmallest(node.left)        # Checks which of the two is smaller
                node.left = self.remove(smallest.data, node.left)
                node.data = smallest.data
        
        elif (node.data > key):                         # if it doesn't find the right node it calls itself and goes to the next node
            node.left = self.remove(key, node.left)
        
        else: 
            node.right = self.remove(key, node.right)
        return node

    def searchSmallest(self, node):     
        while(node.right != None):
            node = node.right
        return node

if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 4, 6, 2]
    for key in keys:
        Tree.insert(key)

    Tree.preorder()     # 5 1 3 2 4 9 7 6 
    Tree.remove(1)
    Tree.preorder()     # 5 3 2 4 9 7 6 
    Tree.remove(9)
    Tree.preorder()     # 5 3 2 4 7 6
    Tree.remove(3)
    Tree.preorder()     # 5 2 4 7 6
        