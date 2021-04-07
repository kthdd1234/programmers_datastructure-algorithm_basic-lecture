# stacks: 마치 접시를 차곡차곡 쌓았다가 맨 위의 접시부터 다시 꺼내어 사용하는 것처럼, 추가된 데이터 원소들을 끄집어내면 마지막에 넣었던 것부터 넣은 순서의 역순으로 꺼내지는 자료구조를 스택(stack)이라고 부릅니다.
# 이처럼 마지막에 넣은 것(후입)이 가장 먼저 꺼내어지는(선출) 성질 때문에 스택을 다른 말로는 후입선출(LIFO: Last-In First-Out) 자료 구조라고도 합니다.
# 스택에 데이터 원소를 추가하는(집어넣는) 동작을 푸시(push) 연산이라고 합니다.
# 스택 마지막에 추가되었던 원소를 참조하고 삭제하는(꺼내는) 동작을 팝(pop) 연산이라고 합니다.

# size(): 현재 스택에 들어 있는 데이터 원소의 수를 구함
# isEmpty(): 현재 스택이 비어 있는지를 판단(size() == 0?)
# push(x): 데이터 원소 x 를 스택에 추가
# pop(): 스택에 가장 나중에 저장된 데이터 원소를 제거(또는 반환)
# peek(): 스택에 가장 나중에 저장된 데이터 원소를 참조(반환), 그러나 제거하지는 않음

# 스택에서 발생하는 오류
# 비어 있는 스택에서 데이터 원소를 꺼내려 할때 -> 스택 언더플로우(stack underflow)
# 꽉 찬 스택에 데이터 원소를 넣으려 할때 -> 스택 오버플로우(stack overflow)

from doublylinkedlists import DoublyLinkedList
from doublylinkedlists import Node


# 배열로 구현한 스택
class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)  # 스택의 크기를 리턴

    def isEmpty(self):
        return self.size() == 0  # 스택이 비어 있는지 판단

    def push(self, item):
        self.data.append(item)  # 데이터 원소를 추가

    def pop(self):
        return self.data.pop()  # 데이터 원소를 삭제(리턴)

    def peek(self):
        return self.data[-1]  # 스택의 꼭대기 원소 반환


# 양방향 연결리스트로 구현한 스택

'''
class LinkedListStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data
'''

# 스택의 응용 - 수식의 후위 표기법(Postfix Notation)

# 우리가 일상에서 사용하는 수식의 표기법은, 중위 표기법(infix notation)이라고 부릅니다.
# 두개의 피연산자 A 와 B 를 가지고 덧셈을 하는 수식을 표기하면 A + B 와 같이 되는데, 이 때 연산자인 + 가 두 피연산자의 사이에 위치하기 때문에 중위 표기법이라고 부릅니다.

# 중위 표기법 예시
# 예시1: (A + B) * (C + D )
# 예시2: A + B * C

# 그렇다면 후위 표기법은 무엇일까요?
# 연산자를 두 피연산자의 뒤에 쓰는 방식입니다. 따라서 앞의 예인 A + B 를 후위 표기법으로 표기하면 AB+ 가 됩니다.

# 후위 표기법 예시
# 예시1: AB+CD+*
# 예시2: ABC*+ => A 와 (B 와 C 의 곱)을 더한다는 의미

# 알고리즘의 설계

# 연산자의 우선순위 설정
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

'''
중위 표현식을 왼쪽부터 한글자씩 읽어서
    피연산자이면 그냥 출력
    '(' 이면 스택에 push
    ')' 이면 '(' 이 나올 때까지 스택에서 pop, 출력
    연산자이면 스택에서 이보다 높(거나 같)은 우선순위 것들을 pop, 출력
        그리고 이 연산자는 스택에 push

스택에 남아 있는 연산자는 모두 pop, 출력
'''

# 코드의 구현 - 힌트
# 스택의 맨 위에 있는 연산자와의 우선순위 비교: 스택의 peek() 연산 이용
# 스택에 남아 있는 연산자 모두 pop() 하는 순환문: while not opStack.isEmpty(): 사용


def solution(S):  # (A+B)*(C+D)
    opStack = ArrayStack()
    answer = ''

    for str in S:
        if str.isalpha():
            answer += str
        elif '(' == str:
            opStack.push(str)
        elif ')' == str:
            pop = opStack.pop()

            while pop != '(':
                answer += pop
                pop = opStack.pop()

        elif str in prec:
            try:
                peek = opStack.peek()
                operator = prec[peek]
                curr = prec[str]

                while operator >= curr:
                    answer += opStack.pop()

                opStack.push(str)
            except IndexError:
                opStack.push(str)

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer


# 후위 표기 수식 계산
'''
후위 표현식을 왼쪽부터 한 글자씩 읽어서
    피연산자이면 스택에 push
    연산자를 만나면 스택에서 pop -> (1), 또 pop -> (2)
        (2) 연산 (1) 을 계산, 이 결과를 스택에 push

수식의 끝에 도달하면 스택에서 pop -> 이것이 계산 결과
'''


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)

    if valProcessing:
        tokens.append(val)

    return tokens
