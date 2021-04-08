# 환형 큐(Circular Queue)
# 큐에 담을 수 있는 데이터의 양(데이터 원소의 개수)이 무한할 수는 없습니다.
# 만약 큐에 담을 수 있는 원소의 개수의 상한을 미리 정하고 이를 지킬 수 있다면, 선형 배열을 이용해서 큐를 효과적으로 구현할 수 있습니다.
# 선형 배열의 한쪽 끝과 다른 쪽 끝이 서로 맞닿아 있는 모습(원형 또는 환형)으로 생각하고, 큐의 맨 앞과 맨 뒤를 가리키는(원소를 넣을쪽의 배열 인덱스와 꺼낼 쪽의 배열 인덱스를) 기억해두면
# 데이터 원소가 빠져 나간 쪽의 저장소를 재활용하면서 큐를 관리 할 수 있습니다.
# 이러한 모습으로 구성한 큐를 환형 큐(circular queue)라고 부릅니다.
# 데이터를 집어넣는 부분은 rear 라고 포인터를 가리키게 합니다.
# 데이터를 꺼내는 부분은 front 라고 포인터를 가리리게 합니다.

# 연산의 정의
'''
size() - 현재 큐에 들어 있는 데이터 원소의 수를 구함
isEmpty() - 현재 큐가 비어 있는지를 판단
isFull() - 큐에 데이터 원소가 꽉 차 있는지를 판단
enqueue(x) - 데이터 원소 x 를 큐에 추가
dequeue() - 큐의 맨 앞에 저장된 데이터 원소를 제거(또는 반환)
peek() - 큐의 맨 앞에 저장된 데이터 원소를 반환(제거하지는 않음)
'''

# 배열로 구현한 환형 큐


class CircularQueue:
    def __init__(self, n):
        self.maxCount = n  # 빈 큐를 초기화
        self.data = [None] * n  # 인자로 주어진 최대 큐 길이 설정
        self.count = 0
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.count == 0  # 큐가 비어 있는지 확인

    def isFull(self):
        return self.count == self.maxCount  # 큐가 꽉 차 있는지 확인

    def enqueue(self, x):  # 큐에 데이터 원소 추가
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.rear + 1) % self.maxCount
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):  # 큐의 데이터 원소 삭제
        if self.isEmpty():
            raise IndexError('Queue empty')
        self.front = (self.front + 1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):  # 큐의 맨 앞 원소 들여다보기
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]


circularQueue = CircularQueue(6)
circularQueue.enqueue('A')
circularQueue.enqueue('B')
circularQueue.enqueue('C')
circularQueue.enqueue('D')

pop1 = circularQueue.dequeue()
pop2 = circularQueue.dequeue()

circularQueue.enqueue('E')
circularQueue.enqueue('F')
circularQueue.enqueue('G')

pop3 = circularQueue.dequeue()

peek = circularQueue.peek()
