# n이 2이상이니까 n=1은 고려 안해도 됨
# 2,3,...,i 의 배수 제외한 개수
# 전체 - i의 배수


def solution(n):
    n_set = set(range(2, n+1))
    for i in range(2, n+1):
        if i in n_set:
            n_set -= set(range(2*i, n+1, i))
    return len(n_set)


def test_solution():
    assert solution(10) == 4
    assert solution(5) == 3
