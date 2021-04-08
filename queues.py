# 큐(Queues): 데이터 원소를 한 줄로 늘어세우는 자료 구조, 즉 선형(linear)구조이며 스택의 반대인 특성을 가지고 있습니다.
# 어느 시점에서 큐에 들어 있는 데이터 원소를 꺼내면 큐에 들어 있는 원소들 중 가장 먼저 넣었던 것이 꺼내집니다.
# 따라서 큐를 선입선출(FIFO: First-in First-Out)이라고 부릅니다.
# 데이터 원소를 큐에 넣는 동작을 인큐(enqueue)연산이라고 부르고
# 반대로 큐로부터 데이터 원소를 꺼내는 동작을 디큐(dequeue)연산이라고 부릅니다.

# 연산의 정의
'''
size() - 현재 큐에 들어 있는 데이터 원소의 수를 구함
is Empty() - 현재 큐가 비어 있는지를 판단
enqueue(x) - 데이터 원소 x 를 큐에 추가
dequeue() - 큐의 맨 앞에 저장된 데이터 원소를 제거(또는 반환)
peek() - 큐의 맨 앞에 저장된 데이터 원소를 반환(제거하지는 않음)
'''


class ArrayQueue:
    # constructor 메서드
    def __init__(self):
        self.data = []

    # 큐의 크기를 리턴
    # 배열로 구현할시 복잡도: O(1)
    def size(self):
        return len(self.data)

    # 큐가 비어 있는지 판단
    # 배열로 구현할시 복잡도: O(1)
    def isEmpty(self):
        return self.size() == 0

    # 데이터 원소를 추가
    # 배열로 구현할시 복잡도: O(1)
    def enqueue(self, item):
        self.data.append(item)

    # 데이터 원소를 삭제(리턴)
    # 배열로 구현할시 복잡도: O(n)
    # 맨 앞의 원소를 꺼낼시 나머지 원소들이 전부 한칸 앞으로 당겨야 하므로 복잡도는 O(n)
    def dequeue(self):
        return self.data.pop(0)

    # 큐의 맨 앞 원소 반환
    # 배열로 구현할시 복잡도: O(1)
    def peek(self):
        return self.data[0]


# 양방향 연결 리스트로 구현한 큐
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
            raise IndexError('Index out of range')

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.nodeCount += L.nodeCount


class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def dequeue(self):
        return self.data.popAt(1)

    def peek(self):
        return self.data.getAt(1).data
