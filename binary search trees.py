# 이전 탐색 알고리즘: 이미 정렬된 선형 배열을 대상으로, 배열을 절반씩 잘라 가면서 찾고자 하는 원소(또는 키 - key)가 들어 있을 수 없음이 보장되는 절반을 탐색 대상에서 제외함으로써 매 반복에서 탐색 대상이 되는 배열의 길이를 반으로 만들어 나가는 알고리즘입니다.
# 해당 알고리즘의 실행 시간은 배열의 길이를 n 이라고 할 때, log(n)에 비례합니다. 이진 탐색을 적용하기 위해서는 탐색 대상인 배열이 미리 정렬되어 있어야 하므로, 이 배열에 데이터 원소를 추가하거나 배열로부터 데이터 원소를 삭제하는 일은 n 에 비례하는 시간을 소요합니다.

# 이진 탐색 트리에서는, 모든 노드에 대해서 왼쪽 서브트리에 들어 있는 데이터는 모두 현재 노드의 값(키)보다 작고 오른쪽 서브트리에 들어 있는 데이터는 모두 현재 노드의 값(키)보다 크도록 트리를 유지합니다.
# 다시 말하면, 이러한 성질을 만족하는 이진 트리를 이진 탐색 트리라고 부릅니다.

# 탐색을 할 때는 루트 노드에서 시작해서 한 번에 한 단계씩 간선을 딸 아래로 아래로 내려갑니다.
# 어느 노드를 방문했을 때, 이 노드에 담긴 데이터 원소보다 찾고자 하는 키가 더 작은 경우에는 왼쪽 서브트리를 택합니다.
# 찾고자 하는 키가 더 큰 경우에는 오른쪽 서브트리를 택합니다.
# 반대쪽 서브트리에는 찾고자 하는 값이 없음을 보장할 수 있으니까 탐색할 피룡가 없다는 성질을 이용하는 것이죠.
# 이렇게 해서 리프 노드에까지 이르렀는데도 그 사이에 찾고자 하는 값을 만나지 못하면 이 이진 탐색트리에는 찾으려는 값이 없다는 것을 알 수 있습니다.

# 이진 탐색 트리를 추상적 자료 구조로 정의하는데, 아래와 같은 연산을 제공하도록 합니다.

'''
    insert(): 트리에 주어진 데이터 원소를 추가
    remove(): 특정 원소를 트리로부터 삭제
    lookup(): 특정 원소를 검색(탐색)
    inorder(): 키의 순서대로 데이터 원소들을 나열
    min(), max(): 최소 키, 최대 키를 가지는 원소를 각각 탐색
'''

# 핵심이 되는 연산인 탐색(lookup)의 실행 시간은 트리의 높이 (또는 깊이)에 비례하므로, 평균적으로(노드의 개수, 즉 데이터 원소의 개수를 n 이라 할 때)log(n) 에 비례합니다.
# 또한, 선형 배열이 아닌 트리 구조를 택하기 때문에 삽입/삭제(insert/remove)연산 또한 평균적으로 log(n)에 비례하는 시간을 소요합니다.


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        try:
            if key < self.key:
                if self.left == None:
                    newNode = Node(key, data)
                    self.left = newNode
                    return True
                else:
                    self.left.insert(key, data)
            elif key > self.key:
                if self.right == None:
                    newNode = Node(key, data)
                    self.right = newNode
                    return True
                else:
                    self.right.insert(key, data)
            else:
                raise KeyError('same key')
        except KeyError:
            return False

    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent

    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None

                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                childNode = None
                if node.left:
                    childNode = node.left
                else:
                    childNode = node.right

                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if parent.left == node:
                        parent.left = childNode
                    elif parent.right == node:
                        parent.right = childNode

                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = childNode

            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    successor = successor.left
                    parent = node.right
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                if parent.left == successor:
                    parent.left = successor.left or successor.right
                elif parent.right == successor:
                    parent.right = successor.left or successor.right
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
            return True

        else:
            return False

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()

        return traversal

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


class BinSearchTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None


# 이진 탐색 트리에서 원소 삭제
'''
    1. 키(key)를 이용해서 노드를 찾는다.
        - 해당 키의 노드가 없으면, 삭제할 것도 없음
        - 찾은 노드의 부모 노드도 알고 있어야 함
    2. 찾은 노드를 제거하고도 이진 탐색 트리 성질을 만족하도록 트리의 구조를 정리한다.
'''

'''
삭제되는 노드가
    1. 말단(leaf) 노드인 경우
        그냥 그 노드를 없애면 됨
        -> 부모 노드의 링크를 조정(좌?우?)

    2. 자식을 하나 가지고 있는 경우
        삭제되는 노드 자리에 그 자식을 대신 배치
        -> 자식이 왼쪽?오른쪽?
        -> 부모 노드의 링크를 조정(좌?우?)

    3. 자식을 둘 가지고 있는 경우
        삭제되는 노드보다 바로 다음 (큰)키를 가지는 노드를 찾아
        그 노드를 삭제되는 노드 자리에 대신 배치하고
        이 노드를 대신 삭제
'''
