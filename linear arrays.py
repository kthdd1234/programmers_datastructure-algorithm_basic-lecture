# 선형 배열(Linear Arrays): 선형 배열은 데이터들이 선(line) 처럼 일렬로 늘어선 형태를 말합니다.
# Python 에서는 서로 다른 종류의 데이터 또한 줄세울 수 있는 리스트(list) 라는 데이터형이 있습니다.
# 데이터를 늘어놓은 모양새를 말할 때는 배열(array)이라는 용어 사용
# python 의 데이터형을 가리킬 때에는 리스트(list)라는 용어 사용

# Python 리스트에 활용할 수 있는 연산들

# 리스트 길이와 관계 없이 빠르게 실행 결과를 보게되는 연산들
# 원소 덧붙이기: list.append()
# 원소 하나를 꺼내기: list.pop()
# 위 연산들은 리스트의 길이와 무관하게 빠르게 실행할 수 있는 연산들입니다.
# big-o notation: O(1)

# 리스트의 길이에 비례해서 실행 시간이 걸리는 연산들(리스트가 커지면 그에 따라 실행시간이 길어지는 연산들)
# 원소 삽입하기: .insert()
# 원소 삭제하기: .del()
# 이런 연산들은 리스트의 길이가 길면 길수록 처리가 오래 걸리게 됩니다.
# 리스트의 길이가 100배가 되면, 위 연산들을 실행하는 데 걸리는 시간도 100배 커짐
# big-o notation: O(n)

# 추가 다른 연산
# 원소 탐색하기: .index()

# 정렬된 리스트에 원소 삽입
L = [20, 37, 58, 72, 91]
x = 65
for i, value in enumerate(L):
    if value > x:
        L.insert(i, x)
        break
print(L)

# 리스트에서 원소 찾아내기
answer = []
L2 = [64, 72, 83, 72, 54]
y = 72

for i, value in enumerate(L2):
    if value == y:
        answer.append(i)

if len(answer) == 0:
    answer = [-1]

print(answer)
l = [1, 2, 3]
print(l.pop(0), l)
