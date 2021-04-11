# 이진 트리(Binary Trees): 트리에 포함되는 모든 노드의 차수가 2 이하인 트리를 말합니다.

# 이진 트리의 추상적 자료구조
# 연산의 정의
# 트리는 정의 자체가 재귀적이기 때문에, 이를 대상으로 하는 연산들도 대부분 재귀적으로 구현 가능합니다.

'''
size() - 현재 트리에 포함되어 있는 노드의 수를 구함
depth() - 현재 트리의 깊이(또는 높이)를 구함
'''

# 트리의 각 노드를 정해진 순서로 방문하는 것을 순회(traversal)연산이라고 부릅니다.
# 트리를 순회하는 순서를 크게 나누면 깊이 우선 순회(depth first traversal)와 넓이 우선 순회(breadth first traversal)가 있습니다.
# 깊이 우선 순회에도, 특히 이진 트리를 대상으로 하는 경우에는, 세 가지의 서로 다른 순서를 정의할 수 있습니다.

'''
어느 노드 x 를 기준을 할 때,
    중위 순회(in-order traversal): 왼쪽 서브트리를 순회한 뒤 노드 x 를 방문, 그리고 나서 오른쪽 서브트리를 순회
    전휘 순회(pre-order traversal): 노드 x 를 방문한 후에 왼쪽 서브트리를 순회, 마지막으로 오른쪽 서브트리를 순회
    후위 순회(post-order traversal): 왼쪽 서브트리를 순회, 오른쪽 서브트리를 순회, 그리고 나서 마지막으로 노드 x 를 방문
'''

# 이진 트리의 구현 - 노드(Node)


class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0

        if l > r:
            return l + 1
        else:
            return r + 1

    # 중위 순회(In-order Traversal)
    # 순회의 순서
    '''
        (1) left subtree
        (2) 자기자신 
        (3) right subtree
    '''

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    # 전위 순회(Pre-order)
    # 순회의 순서
    '''
        (1) 자기자신
        (2) left subtree
        (3) right subtree
    '''

    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    # 후위 순회(Post-order)
    # 순회의 순서
    '''
        (1) left subtree
        (2) right subtree
        (3) 자기자신
    '''

    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal


class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []
