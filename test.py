class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    # 특정 원소 참조(pos 번째)
    def getAt(self, pos):
        if pos <= 0 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    # 원소 삽입
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        result = None
        try:
            if pos < 1 or pos > self.nodeCount:
                raise IndexError

            if pos == 1:
                if self.nodeCount == 1:
                    node = self.head or self.tail
                    self.head = None
                    self.tail = None
                    result = node.data
                else:
                    node = self.head
                    self.head = node.next
                    result = node.data
            else:
                prev = self.getAt(pos - 1)
                node = prev.next
                result = node.data
                if pos == self.nodeCount:
                    self.tail = prev
                    prev.next = None
                else:
                    prev.next = node.next
            self.nodeCount -= 1
            return result
        except IndexError:
            return False

    # 길이 얻어내기
    def getLength(self):
        return self.nodeCount

    # 리스트 순회
    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result

    # 두 리스트 합치기
    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount


'''
A = Node(67)
B = Node(34)
C = Node(28)
D = Node(12)
E = Node(90)
F = Node(50)

L1 = LinkedList()

L1.insertAt(1, A)
L1.insertAt(2, B)
L1.insertAt(3, C)
L1.insertAt(1, D)
L1.insertAt(2, E)
L1.insertAt(6, F)

print('Linked lists:', L1)

result1 = L1.popAt(1)
print('result1:', result1)
print('Linked lists:', L1)

result2 = L1.popAt(5)
print('result2:', result2)
print('Linked lists:', L1)
'''
