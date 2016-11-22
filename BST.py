  #=====================================================================
  # Author: Isai Damier
  # Title: Add
  # Project: geekviewpoint
  # Package: algorithms
  #
  # Statement:
  #   Add an element to a Binary Search Tree.
  #
  # Time Complexity of Solution:
  #   Best = const; Average = O(log(n)); Worst = O(n).
  #
  # Description:
  #   This function does not admit duplicate data into the BST.
  #
  #=====================================================================
class Node:
    def __init__(self,Data):
        self.data=Data
        self.left=None
        self.right=None

  
class BST( object ):
 
    def __init__( self ):
        self.root = None


    def getRoot( self ):
        return self.root

    def add( self, el ):
        n, p = self.root, None

        while n is not None and n.data != el:
          p = n
          if el < n.data:
            n = n.left
          else:
            n = n.right

        if n is None: # not duplicate
          if p is None:
            self.root = Node( el )
          elif el < p.data:
            p.left = Node( el )
          else:
            p.right = Node( el )

    def preOrder(self,root):
        l=[]    
        s=""
        def sup(root):        
            if root!=None:
                l.append(root.data)
                sup(root.left)
                sup(root.right)
        sup(root)
        for i in l:
            s+=str(i)+" "
        print s

    def inOrder(self,root):
        l=[]    
        s=""
        def sup(root):       
            if root!=None:
                sup(root.left)
                l.append(root.data)
                sup(root.right)

        sup(root)
        for i in l:
            s+=str(i)+" "
        print s

    def postOrder(self,root):
        l=[]    
        s=""
        def sup(root):       
            if root!=None:
                
                sup(root.left)
                sup(root.right)
                l.append(root.data)

        sup(root)
        for i in l:
            s+=str(i)+" "
        print s

t=BST()
l=[10,5,15,4,3,25,20,12]
for i in l:
    t.add(i)
t.preOrder(t.root)
t.inOrder(t.root)
t.postOrder(t.root)


