  #=======================================================================
  # Author: Isai Damier
  # Title: DSW Algorithm
  # Project: geekviewpoint
  # Package: algorithms
  #
  # Statement:
  #   Transform the given BST into a perfectly balanced BST so that its
  #   height is log n, where n is the number of nodes on the tree.
  #
  #  Time Complexity: O(n)
  #  Space Complexity: O(1)
  #
  # Details:
  #   While trees are great at depicting hierarchy among objects, the most
  #   important aspect of a binary search tree (BST) is the blazing search
  #   speed that a perfectly balanced BST provides. If a perfectly balanced
  #   BST contains 10,000 objects, it takes at most 14 comparisons to find
  #   an object; a linked list would require 10,000 comparisons: O(n). Does
  #   your BST contain one million objects? Then it would take at most 20
  #   comparisons. One billion objects? Then 30 comparisons. This is because
  #   in a perfectly balanced BST, height = log2(n).
  #
  #   Imagine having to spend $20 to get a million dollars worth of gold;
  #   while everyone else has to spend one million dollars for the same
  #   amount of gold. What would you not do to get that kind of buying power?!
  #   That same mindset has fueled a slew of research in Balancing BSTs.
  #   (The members of the US Congress almost had that kind of power: they
  #   used to be allowed to do insider trading; a crime for everyone else.)
  #
  #   The following algorithm was invented by Colin Day and later refined
  #   by Quentin F. Stout and Bette L. Warren: hence, DSW. It takes an
  #   ordinary BST and transforms it into a perfectly balanced BST. A BST
  #   is perfectly balanced if the leaves are on the same level or one
  #   level apart. The algorithm goes as follows:
  #
  #   1] Using right-rotation operations, turn the tree into a linked list
  #      (a.k.a. backbone or vine)
  #   2] Rotate every second node of the backbone about its parent to turn
  #      the backbone into a perfectly balanced BST. Voila!
  #
  #=======================================================================
  
  
class BST( object ):
 
  def __init__( self ):
      self.root = None
 
 
  def getRoot( self ):
    return self.root
 
  def DSW( self ):
    if None != self.root:
      self.createBackbone() #  effectively: createBackbone( self.root)
      self.createPerfectBST() # effectively: createPerfectBST( self.root)
 
  #=====================================================================
  # Time complexity: O(n)
  #=====================================================================
  def createBackbone( self ):
    grandParent = None
    parent = self.root
    leftChild = None
 
    while None != parent:
      leftChild = parent.left
      if None != leftChild:
        grandParent = self.rotateRight( grandParent, parent, leftChild )
        parent = leftChild
      else:
        grandParent = parent
        parent = parent.right
 
 
  #=======================================================================
  #   Before      After
  #    Gr          Gr
  #     \           \
  #     Par         Ch
  #    /  \        /  \
  #   Ch   Z      X   Par
  #  /  \            /  \
  # X    Y          Y    Z
  #=======================================================================
  def rotateRight( self, grandParent, parent, leftChild ):
    if None != grandParent:
      grandParent.right = leftChild
    else:
      self.root = leftChild
 
    parent.left = leftChild.right
    leftChild.right = parent
    return grandParent
 
  #=======================================================================
  # Time complexity: O(n)
  #=======================================================================
  def createPerfectBST( self ):
    n = self.size()
 
    # m = 2^floor[lg(n+1)]-1, ie the greatest power of 2 less than n: minus 1
    m = self.greatestPowerOf2LessThanN( n + 1 ) - 1
    self.makeRotations( n - m )
 
    while m > 1:
      m /= 2
      self.makeRotations( m )
 
 
  #=======================================================================
  # Time complexity: log(n)
  #=======================================================================
  def greatestPowerOf2LessThanN( self, n ):
    x = self.MSB( n ) # MSB
    return ( 1 << x ) # 2^x
 
 
  #=======================================================================
  # Time complexity: log(n)
  # return the index of most significant set bit: index of
  # least significant bit is 0
  #=======================================================================
  def MSB( self, n ):
    ndx = 0
    while 1 < n:
      n = ( n >> 1 )
      ndx += 1
    return ndx
 
 
  def makeRotations( self, bound ):
    grandParent = None
    parent = self.root
    child = self.root.right
    while bound > 0:
      try:
        if None != child:
          self.rotateLeft( grandParent, parent, child );
          grandParent = child;
          parent = grandParent.right;
          child = parent.right;
        else:
          break
      except AttributeError: # TypeError
        break
      bound -= 1
 
 
  def rotateLeft( self, grandParent, parent, rightChild ):
    if None != grandParent:
      grandParent.right = rightChild
    else:
      self.root = rightChild
 
    parent.right = rightChild.left
    rightChild.left = parent
