from node import Node

class LinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0
    def __init__(self):
        self.nodeTail = Node(Tail = True)
        self.nodeHead = Node(Head = True, nodeNext = self.nodeTail)
        
    def insert(self, objInsert, idxInsert):
        nodeNew = Node(objValue = objInsert)
        nodePrev = self.get(idxInsert-1)
        nodeNext = nodePrev.getNext()
        # 새로운 노드 삽입으로 재 연결
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size += 1
        
    def delete(self, idxDelete):
        nodePrev = self.get(idxDelete - 1)
        nodeDelete= nodePrev.getNext()
        nodeNext = nodeDelete.getNext()
        nodePrev.setNext(nodeNext)
        self.size -= 1
        return nodeDelete.getValue()
    
    def get(self, idx):
        nodeReturn = self.nodeHead
        # search는 insert와 delete에 비해 오래 걸린다.
        for i in range(idx + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn
    
    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(), end = " ")
        print()
        
    def getSize(self):
        return self.size

    
        
        