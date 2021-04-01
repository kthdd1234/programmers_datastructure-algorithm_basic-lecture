# 재귀 알고리즘(recursive algorithms): 하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것
# 재귀 알고리즘의 종결 조건: 알고리즘의 종결조건에 반드시 필요

# 문제: 1 부터 N 까지의 모든 자연수의 합을 구하시오.

# Recursive version
def sum_recursive_version(n):
    if n <= 1:  # 종결조건 매우 중요!
        return n
    else:
        return n + sum(n - 1)


N = int(input('Number: '))
print(sum_recursive_version(N))

# 알고리즘 복잡도: n 이 커지면  n 에 따라서 함수를 호출해야하는 횟수가 증가하기 때문에 n 에 비례하는 복잡도를 가짐, O(n)
# 알고리즘 효율성: iterative version 보다 효율성이 떨어짐

# Iterative version


def sum_iterative_version(n):
    s = 0
    while n >= 0:
        s += n
        n -= 1
    return s


n = int(input('Number: '))
print(sum_iterative_version(n))

# 알고리즘 복잡도: n 이 커지면  n 에 따라서 순환문 반복 횟수가 증가하기 때문에 n 에 비례하는 복잡도를 가짐, O(n)
# 알고리즘 효율성: recursive version 보다 효율성이 좋음


def sum_good_version(n):
    return n * (n + 1) // 2

# 알고리즘 복잡도: O(1)

# 재귀 알고리즘 추가 예제
# 1 부터 n 까지의 모든 자연수를 곱하는 문제이며 n! 을 구하는 문제


def what(n):
    if n <= 1:
        return 1
    else:
        return n * what(n - 1)

# 피보나치 순열 구현하기

# Recursive version


def solution_recursive_version(x):
    answer = 0
    if x < 2:
        return x
    else:
        answer = solution_recursive_version(
            x - 1) + solution_recursive_version(x - 2)

    return answer

# Iterative version


def solution_iterative_version(x):
    answer = 0
    fa = 0
    fb = 1
    while x > 0:
        x -= 1
        fa, fb = fb, fa+fb
        answer = fa
    return answer
