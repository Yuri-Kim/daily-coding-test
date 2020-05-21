def solution(n):
    return int("".join(sorted(str(n), reverse=True)))


def test_solution():
    assert solution(118372) == 873211
