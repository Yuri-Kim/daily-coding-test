# s를 다 대문자로 바꾸고 upper()
# 개수 세서 count() 같으면 true 아니면 false


def solution(s):
    return s.upper().count('P') == s.upper().count('Y')


def test_sample():
    assert solution('pPooyY') == True
    assert solution('Pyy') == False