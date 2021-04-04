# 연결 리스트의 맨 앞에다가 데이터 원소를 담고 있지 않은, 그냥 자리만 차지하는 노드를 추가한, 조금 모습이 달라진 연결 리스트를 정의
# 이렇게 맨 앞에 추가된, 데이터 원소를 담고 있지 않은 노드를 더미 노드(dummy node)라고 함

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

    # 특정 원소 참조(pos 번째 노드 얻어내기)
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        i = 0
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
