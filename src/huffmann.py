class Node:
  def __init__(self, value, numberOfOcurence):
    self.value = value
    self.numberOfOcurence = numberOfOcurence
    self.left = None
    self.right = None

  def updateLeftNode(self, node):
    self.left = node

  def updateRightNode(self, node):
    self.right = node

  def updateNumberOfOcurence(self, value):
    self.numberOfOcurence += value

class Huffmann:
  def __init__(self):
    self.tree = Node(None, 0)
    self.dictionary = {}

  
  def findItem(self, item, arrayOfChars):
    result = False
    for index, node in enumerate(arrayOfChars):
      if (node.value == item):
        result = index
        break
    return result
   
  def mountBaseArray(self, symbols):
    arrayOfChars = []
    for char in list(symbols):
      index = self.findItem(char, arrayOfChars)
      if(index != False or str(index) == str(0)):
        arrayOfChars[index].updateNumberOfOcurence(1)
      else:
        arrayOfChars.append(Node(char, 1))
    return sorted(arrayOfChars, key=lambda node: node.numberOfOcurence, reverse=True)

  def mountTree(self, charNode, rootNode):
    nodeToReturn = None
    if (rootNode.right and rootNode.left == None):
      rootNode.updateLeftNode(charNode)
      rootNode.updateNumberOfOcurence(charNode.numberOfOcurence)
      nodeToReturn = Node(None, 0)
      nodeToReturn.updateRightNode(rootNode)
      nodeToReturn.updateNumberOfOcurence(rootNode.numberOfOcurence)
    else:
      rootNode.updateRightNode(charNode)
      rootNode.updateNumberOfOcurence(charNode.numberOfOcurence)
      nodeToReturn = rootNode
    return nodeToReturn

  def printTree(self, root, level=0):
    if root == None: return
    if root.right:
      self.printTree(root.right, level+1)
    identacao = ''
    for x in range(level):
      identacao += '     '
    print (identacao + str(root.value)+str(root.numberOfOcurence))
    if root.left:
      self.printTree(root.left, level+1)

  def mountCodeword(self, root, charToFind):
    codeWord = ''
    if root.value == None:
      if root.left != None and root.left.value == charToFind:
        codeWord += '0'
      elif root.right != None and root.right.value == charToFind:
        codeWord += '1'
      else:
        codeWord += '1' + self.mountCodeword(root.right, charToFind)
    
      
    return codeWord
        
  def encode(self, symbols):
    arrayOfSymbols = self.mountBaseArray(symbols)
    rootNode = self.tree
    for charNode in reversed(arrayOfSymbols):
      rootNode = self.mountTree(charNode, rootNode)
    self.tree = rootNode.right
    self.printTree(self.tree)
    for charNode in arrayOfSymbols:
      self.dictionary.update({ charNode.value: self.mountCodeword(self.tree, charNode.value) })
    print(self.dictionary)

