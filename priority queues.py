# 우선순위 큐(Priority Queues)
# 큐에 원소를 추가하는 연산은 다른 점이 없되, 큐에서 원소를 꺼내는 원칙은 원소들 사이의 우선순위에 따르는 자료구조로서 우선순위 큐(priority queue)라는 것을 소개합니다.
# 큐가 FIFO(First-In First-Out)방식을 따르지 않고 원소들의 우선순위에 따라 큐에서 빠져나오는 방식입니다.
# 대표적인 응용 예를 들다면, 운영체제에서 CPU 스케줄러를 구현할 때, 현재 실행할 수 있는 작업들 중 가장 우선순위가 높은 것을 골라 실행하는 알고리즘이 있습니다.

# 우선순위 큐를 구현하는 데에는 두 가지의 서로 다른 접근 방법을 생각할 수 있습니다.
'''
    1. 큐에 원소를 넣을 때(enqueue 할 때) 우선순위 순서대로 정렬해 두는 방법
    2. 큐에서 원소를 꺼낼 때(dequeue 할 때) 우선순위가 가장 높은 것을 선택하는 방법
'''
# 우선순위 큐 코드 구현


class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s

    def getLength(self):
        return self.nodeCount

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr

    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.nodeCount += L.nodeCount


class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()

    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head

        while curr.next.data != None and curr.next.data < x:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data
