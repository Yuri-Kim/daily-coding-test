# n/2*"수박" + n%2*"수" 하면되지 않을까


def solution(n):
    return "수박"*(n//2)+"수"*(n%2)


def test_solution():
    assert solution(3) == "수박수"
    assert solution(4) == "수박수박"