class Node:
     # None is not same as 0, False, or empty string. None is data type of its own (NoneType) and only None can be None.
    nodeNext = None
    nodePrev = ''
    objValue = ''
    Head = False
    Tail = False
    def __init__(self, nodeNext = None, objValue = '', Head = False, Tail = False):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.Haed = Head
        self.Tail = Tail
    
    def getValue(self):
        return self.objValue
    
    def setValue(self, objValue):
        self.objValue = objValue
    
    def getNext(self):
        return self.nodeNext
    
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext
    
    def isHead(self):
        return self.Head
    
    def isTail(self):
        return self.Tail
    
    
    