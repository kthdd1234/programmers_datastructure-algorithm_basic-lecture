# 재귀 알고리즘 (recursive algorithms) - 응용
# 재귀 알고리즘으로 풀 수 있는 문제들 ↓

# 조합의 수(n 개의 서로 다른 원소에서 m 개를 택하는 경우의 수) 구하기
def combi(n, m):
    if n == m:
        return 1
    elif m == 0:
        return 1
    else:
        return combi(n - 1, m) + combi(n - 1, m - 1)

# 하노이의 탑(크기 순서로 쌓여 있는 원반을 한 막대에서 다른 막대로 옮기기)


# 피보나치 순열
def recursive(n):
    if n <= 1:
        return n
    else:
        return recursive(n - 1) + recursive(n - 2)


def iteraive(n):
    if n <= 1:
        return n
    else:
        i = 2
        t0 = 0
        t1 = 1
        while i <= 2:
            t0, t1 = t1, t0 + t1
            i += 1
        return t1

# 일반적으로, 주어진 문제에 대해서 반복적인 알고리즘이 재귀적인 알고리즘보다 문제 풀이의 (시간적) 효율이 높습니다.
# 그럼에도 불구하고, 재귀 알고리즘이 가지는 특성때문에 트리(Tree) 와 같은 자료구조를 이용하는 알고리즘에는 매우 직관적으로 적용할 수 있는 경우가 많습니다.
