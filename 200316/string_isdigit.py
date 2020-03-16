# isalpha 나 isdigit 쓰고 길이 확인


def solution(s):
    return s.isdigit() and len(s) in [4, 6]


def test_solution():
    assert solution('a1234') == False
    assert solution('1234') == True
