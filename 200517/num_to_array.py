def solution(n):
    return list(reversed(list(map(int, str(n)))))


def test_solution():
    assert solution(12345) == [5,4,3,2,1]