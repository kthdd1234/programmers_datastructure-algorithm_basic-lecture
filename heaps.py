# 힙(heap): 이진 힙(binary heap)이라고도 부릅니다. 힙은 데이터 원소들의 순서를 교묘하게 표현한 트리입니다. 따라서 데이터의 정렬에도 이용할 수 있는데, 힙을 이용하여 데이터를 정렬하는 알고리즘을 힙 정렬(heap sort)이라고 부릅니다.
# 힙에는 최대 힙(max heap)과 최소 힙(min heap)이 있습니다. 최대 힙과 최소 힙은 데이터 원소의 순서 기준이 내림차순이냐 오름차순이냐만 달리지고 완전히 대칭입니다.
# 최대 힙은 세 가지의 성질을 유지하고 있는 이진 트리입니다.
'''
    - 루트 노드가 항상 최댓값을 가진다.
    - 완전 이진 트리이다.
    - 최대 힙 내의 임의의 노드를 루트로 하는 서브트리 또한 최대 힙니다.
'''

# 이진 탐색 트리에서는 원소들이 완전히 크기 순서대로 정렬되어 있습니다.(따라서 중위 순회를 하면 데이터를 정렬된 순서로 뽑아낼 수 있습니다.)
# 최대 힙은 완전히 크기 순서대로 정렬되어 있지는 않습니다.(따라서 트리를 순회함으로써 데이터를 정렬할 수는 없습니다.)
# 또한, 이진 탐색 트리에서는 루트 노드로부터 시작하여 특정 원소를 빠르게 검색할 수 있는 반면, 최대 힙은 이러한 탐색 연산을 제공할 수 없습니다.

# 그렇다면 최대 힙의 장점은 무엇일까요? 바로 부가의 제약 조건, 즉 완전 이진 트리 (complete binary tree)여야 한다는 제약 때문에, n 개의 노드로 이루어진 최대 힙의 높이(깊이)는 log(n) + 1 로 정해집니다.
# 이 성질 때문에 데이터 원소의 삽입/삭제 연산의 실행 시간은 언제나 log(n)에 비례합니다. 따라서,어떤 최대 힙이 존재할 때, 이 힙으로부터 반복적으로 루트 노드를 삭제하면 (서 데이터 원소들을 꺼내면) 루트 노드에 들어 있는 키가 힙 내에서 최대임이 보장되어 있으므로 데이터를 내림차순으로 정렬할 수 있고, 이 정렬에 소요되는 시간 또한 log(n) 에 비례합니다.

# 데이터 표현의 설계
'''
    배열을 이용한 이진 트리의 표현
        - 노드 번호 m 을 기준으로
            -> 왼쪽 자식의 번호: 2 * m
            -> 오른쪽 자식의 번호: 2 * m + 1
            -> 부모 노드의 번호: m // 2
    
    완전 이진 트리이므로
        - 노드의 추가/삭제는 마지막 노드에서만
'''
'''
                    30
            24              12
        18      25      8       6
       4  2   19  21

      [None, 30, 25, 12, 18, 24, 8, 6, 4, 2, 19, 21]
'''
# 최대 힙에 원소 삽입
# 1. 트리의 마지막 자리에 새로운 원소를 임시로 저장
# 2. 부모 노드와 키 값을 비교하여 위로, 위로, 이동
# 최대 힙에 원소 삽입 복잡도: 원소의 개수가 n 인 최대 힙에 새로운 원소 삽입
# -> 부모 노드와의 대소 비교 최대 회수: log(n)
# -> 최악 복잡도 O(logN)의 삽입 연산


class MaxHeap:

    def __init__(self):
        self.data = [None]

    # 힌트: python 에서 두 변수의 값 바꾸기
    # a = 3; b = 5; 일때 a, b = b, a
    def insert(self, item):
        if self.data[-1] == None:
            return self.data.append(item)

        self.data.append(item)
        currIndex = len(self.data) - 1
        parentIndex = currIndex // 2
        parentItem = self.data[parentIndex]

        while item > parentItem:
            self.data[currIndex], self.data[parentIndex] = parentItem, item
            currIndex = parentIndex
            parentIndex = currIndex // 2
            parentItem = self.data[parentIndex] or item + 1
        return True

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = 2 * i

        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = 2 * i + 1
        smallest = i

        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if len(self.data) - 1 >= left and self.data[left] > self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            smallest = left

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if len(self.data) - 1 >= right and self.data[right] > self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest = right

        if smallest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]

            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)


# 최대 힙(Max Heap)에서 원소의 삭제
'''
    1. 루트 노드의 제거 - 이것이 원소들 중 최댓값
    2. 트리 마지막 자리 노드를 임시로 루트 노드의 자리에 배치
    3. 자식 노드들과의 값 비교와 아래로, 아래로, 이동
'''
# 최대 힙에서의 원소 삭제는 항상 루트 노드에서 이루어집니다. 최댓값을 순서대로 뽑아 내는 데 관심이 있기 때문입니다.
# 노드의 삭제 또한 맨 마지막 노드에서만 일어납니다(완전 이진 트리의 성질을 만족해야 하므로).즉, 우선은 루트 노드의 데이터를 꺼내고, 맨 마지막 노드의 원소를 루트 노드의 자리에 임시로 집어넣습니다. 그 후, 마지막 노드를 제거한 다음에 루트 자리에 임시로 들어간 노드의 새로운 올바른 자리를 찾아 주면 됩니다.
# 노드의 삽입 연산에서와는 반대로, 이번에는 임시로 들어간 (일시적으로 위치가 올바르지 않은) 노드는 루트 노드에서 시작해서 아래로 아래로 내려갑니다.
# 자식들 중 더 큰 값을 가지는 노드와 자리를 바꾸면서, 더이상 바꿀 필요가 없거나 리프 노드에 도달할 때까지 이 과정을 반복합니다.
