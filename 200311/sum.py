# 걍 공식쓰면 끝날거같은데?


def solution(a, b):
    return (a+b)*(abs(a-b)+1)/2


def test_sample():
    assert solution(3, 3) == 3
    assert solution(3, 5) == 12
    assert solution(5, 3) == 12