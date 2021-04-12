# 이진 트리의 넓이 우선 순회(breadth first traversal)
# 이 순회 방식은 재귀적으로 구현할 수 없습니다.
# 하나의 노드를 방문했을 때, 나중에 그 노드의 자식노드들을 방문하기로 해 두고, 같은 수준에 있는 다른 노드들을 우선 방문해야 하기 때문에, 이 알고리즘은 재귀적인 성질을 가지지 않습니다.
# 큐(queue)의 자료구조를 활용 할 수 있습니다.
# 먼저 넣은 원소가 먼저 나오는, 선입선출(FIFO: First-in First-out) 성질을 가지고 있기 때문에, 큐는 이러한 종류의 응용에 딱 적합합니다.

# 원칙
'''
    수준(level)이 낮은 노드를 우선으로 방문
    같은 수준의 노드들 사이에는,
        부모 노드의 방문 순서에 따라 방문
        왼쪽 자식 노드를 오른쪽 자식보다 먼저 방문
'''


class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


# 넓이 우선 탐색 순회 알고리즘 구현
'''
    1. (초기화)traversal <- 빈 리스트, q <- 빈 큐
    2. 빈 트리가 아니면, root node 를 q 에 추가(enqueue)
    3. q 가 비어 있지 않은 동안
        3.1 node <- q 에서 원소를 추출(dequeue)
        3.2 node 를 방문
        3.3 node 의 왼쪽, 오른쪽 자식(있으면)들을 q 에 추가
    4. q 가 빈 큐가 되면 모든 노드 방문 완료
'''


def bft(self):
    traversal = []
    q = ArrayQueue()

    if self.root == None:
        return []

    q.enqueue(self.root)
    while not q.isEmpty():
        node = q.dequeue()
        traversal.append(node.data)
    if node.left:
        q.enqueue(node.left)
    if node.right:
        q.enqueue(node.right)

    return traversal
