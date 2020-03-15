# reverse=True로 sorting하면 내림차순, 소->대문자 되니까 그렇게하고 list->str로 변환(.join)


def solution(s):
    return ''.join(sorted(s, reverse=True))


def test_solution():
    assert solution('Zbcdefg') == 'gfedcbZ'