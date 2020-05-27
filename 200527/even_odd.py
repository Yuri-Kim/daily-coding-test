def solution(num):
    return "Even" if num % 2 == 0 else "Odd"


def test_solution():
    assert solution(3) == "Odd"
    assert solution(4) == "Even"
    assert solution(0) == "Even"
