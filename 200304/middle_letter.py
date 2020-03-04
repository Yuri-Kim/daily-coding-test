def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]


def test_sample():
    assert solution("abcde") == "c"
    assert solution("qwer") == "we"