# 1부터 n까지 나머지 없이 딱 떨어지는 수를 더하면 되는데 반이 넘어가면 계산 안하고 걍 자기자신 더해주면 됨


def solution(num):
    return num + sum([i for i in range(1, (num // 2)+1) if num % i == 0])


def test_solution():
    assert solution(12) == 28
    assert solution(5) == 6
