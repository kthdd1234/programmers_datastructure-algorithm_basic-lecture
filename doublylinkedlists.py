# 양방향 연결 리스트(Doubly Linked Lists)
# 말 그대로, 양방향 연결 리스트에서는 노드들이 앞/뒤로 연결되어 있습니다.
# 인접한 두 개의 노드들은 앞의 노드로부터 뒤의 노드가 연결되어 있을 뿐만 아니라, 뒤의 노드로부터 앞의 노드도 연결되어 있습니다.
# 한 노드의 입장에서 보자면, 자신보다 앞에 오는 노드를 연결하는 링크와 자신보다 뒤에 오는 노드를 연결하는 링크를 둘 다 가집니다.
# 따라서 모든 연결은 양방향으로 이루어져 있으며, 그러한 이유로 이런 구조의 연결 리스트를 "양방향 연결 리스트" 라고 부릅니다.
# 양방향 연결 리스트의 맨 앞과 맨 뒤에 더미 노드(dummy node) 를 하나씩 추가합니다.

class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, item):
        self.nodeCount = 0
        self.head = Node(None)  # dummy node
        self.tail = Node(None)  # dummy node
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:  # 시간 복잡도: O(logN)
            i = 0
            node = self.tail
            while i < self.nodeCount - pos + 1:
                node = node.prev
                i += 1
        else:
            i = 0
            node = self.head
            while i < pos:
                node = node.next
                i += 1

        return node

    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertBefore(self, next, newNode):
        prev = next.prev
        newNode.next = next
        newNode.prev = prev
        next.prev = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        next = prev.next
        prev.next = next.next
        return self.popBefore(next.next)

    def popBefore(self, next):
        prev = next.prev  # 삭제할 노드
        if prev.prev.next is not next:
            prev.prev.next = next
        next.prev = prev.prev
        self.nodeCount -= 1
        return prev.data

    def popAt(self, pos):
        try:
            if pos < 1 or pos > self.nodeCount:
                raise IndexError
            node = self.getAt(pos)
            return self.popAfter(node.prev)
        except IndexError:
            return False

    def concat(self, L):
        if L.nodeCount != 0:
            L1_lastNode = self.tail.prev
            L2_firstNode = L.head.next
            L2_lastNode = L.tail.prev

            L1_lastNode.next = L2_firstNode
            L2_firstNode.prev = L1_lastNode

            self.tail.prev = L2_lastNode
            L2_lastNode.next = self.tail

            self.nodeCount += L.nodeCount
