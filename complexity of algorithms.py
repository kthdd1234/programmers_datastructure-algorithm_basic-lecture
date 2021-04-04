# 알고리즘의 "복잡도(complexity)": 알고리즘이 실행함에 있어, 문제의 크기(일반적으로 데이터 원소의 개수를 뜻함)가 커짐에 따라서 얼마나 큰 시간을(또는 공간을) 요구하느냐를 뜻합니다.
# 알고리즘의 시간 복잡도는 문제가 커짐에 따라 이 문제를 해결하는 데 소요되는 시간이 어떤 양상으로 증가하는가를 다룹니다.
# 공간 복잡도는 문제가 커짐에 따라 이 문제를 해결하는 데 소요되는 기억 공간(메모리)의 필요가 어떤 양상으로 증가하는가를 다룹니다.
# 알고리즘의 복잡도를 표현하는 데에는 점근 표기법(asymptotic notation)을 흔히 이용
# 그 중, 특히 big-O notation 을 많이 사용
# 입력의 크기가 N 일 때,
# O(logN) - 입력의 크기의 로그에 비례하는 시간 소요
# O(n) - 입력의 크기에 비례하는 시간 소요

# 평균 시간 복잡도(Average Time Complexity)
# 임의의 입력 패턴을 가정했을 때 소요되는 시간의 평균

# 최악 시간 복잡도(Worst-case Time Complexity)
# 가장 긴 시간을 소요하게 만드는 입력에 따라 소요되는 시간

# 데이터 원소의 개수가 n 개라고 할 때, O(n) 복잡도를 가지는 알고리즘은 원소의 개수에 비례하여 소요 시간이 증가합니다.
# 10 개짜리 데이터로 이루어진 문제를 푸는 데 걸리는 시간이 A 라면, 100 개짜리 데이터로 이루어진 문제를 푸는 데 걸리는 시간은 10 * A 입니다.
# 1,000,000 개짜리 데이터로 이루어진 문제를 푸는 데 걸리는 시간은 100,000 * A 입니다.

# 그렇다면, O(n2)(n 제곱을 표기) 복잡도를 가지는 알고리즘은?
# 알고리즘의 실행 시간이 n 의 제곱에 비례하기 때문에, 10 개짜리 데이터로 이루어진 문제를 푸는 데 걸리는 시간이 B 라면, 100 개짜리 데이터로 이루어진 문제를 푸는 데 걸리는 시간은 100 * B 입니다.

# n 의 제곱 / n! / 2 의 n 제곱: bad
# log(n) / n * log(n): good

# 선형 시간 알고리즘 - O(n)
# 예: n 개의 무작위로 나열된 수에서 최댓값을 찾기 위해 선형 탐색 알고리즘을 적용
# [3, 8, 2, 7, 6, 10, 9] 최댓값: 10
# 최댓값 - 끝까지 다 살펴 보기 전까지는 알 수 없음
# Average case: O(n)
# Worst-case: O(n)

# 로그 시간 알고리즘 - O(logn)
# 예: n 개의 크기 순으로 정렬된 수에서 특정 값을 찾기 위해 이진 탐색 알고리즘을 적용

# 이차 시간 알고리즘 - O(n2)(n 의 2 제곱)
# 예: 삽입 정렬(insertion sort) - 순환하는데 n 번, 정렬하는데 n 번
# Best case: O(n) - 처음에 주어진 리스트가 이미 정렬되어져 있는 상태일때
# Worst case: O(n2) - 리스트의 원소들이 역순을 늘어져 있을때

# 병합 정렬(merge sort) - O(nlogn)
# 입력 패턴에 따라 정렬 속도에 차이가 있지만 정렬 문제에 대해 O(n * logn) 보다 낮은 복잡도를 갖는 알고리즘은 존재할 수 없음이 증명