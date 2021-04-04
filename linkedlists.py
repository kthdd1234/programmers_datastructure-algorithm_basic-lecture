# 연결 리스트(Linked Lists)
# 데이터 원소들을 순서를 지어 늘어놓는다는 점에서 연결 리스트(linked list) 는 선형 배열(linear array) 과 비슷한 면이 있음
# 데이터 원소들을 늘어놓는 방식에서 두 가지의 큰 차이가 있음
# 선형 배열(linear array): 번호가 붙여진 칸에 원소들을 채워놓는 방식
# 연결 리스트(Linked list): 각 원소들을 줄줄이 엮어서 관리하는 방식

# 배열과 비교한 연결 리스트

# 배열 저장 공간: 연속한 위치
# 연결 리스트 저장 공간: 임의의 위치

# 배열 특정 원소 지칭: 매우 간편 / O(1)
# 연결 리스트 특정 원소 지칭: 선형탐색과 유사 / O(n)

# 연결 리스트 자료 구조 정의
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

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

    # 길이 얻어내기
    def getLength(self):
        return self.nodeCount

    # 리스트 순회
    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    # 두 리스트 합치기
    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount


# 연결 리스트에 나열된 데이터 원소들의 사이에 새로운 데이터 원소를 삽입하려면, 앞/뒤의 원소들을 연결하고 있는 링크를 끊어 내고, 그 자리에 새로운 원소를 집어넣기 위해서 링크들을 조정해줘야 합니다.

# 연결 리스트 - 원소의 삽입(명세 정의)
# pos 가 가리키는 위치에 (1 <= pos <= nodeCount + 1)
# newNode 를 삽입하고
# 성공/실패에 따라 True/False 를 리턴

# 맨 앞에 삽입하는 경우: O(1)
# 중간에 삽입하는 경우: O(n)
# 맨 끝에 삽입하는 경우: O(1)

# 연결 리스트 연산 - 원소의 삭제(명세 정의)
# pos 가 가리키는 위치의 (1 <= pos <= nodeCount)
# node 를 삭제하고
# 그 node 의 데이터를 리턴

# 맨 앞에서 삭제하느 경우: O(1)
# 중간에서 삭제하는 경우: O(n)
# 맨 끝에서 삭제한는 경우: O(n)
