# index 찾아서 문장 포메팅..?


def solution(seoul):
    return '김서방은 %d에 있다' % seoul.index('Kim')


def test_solution():
    assert solution(['Jane', 'Kim']) == '김서방은 1에 있다'
