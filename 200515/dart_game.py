import re


def solution(dartResult):
    pat = re.compile(r'([0-9]|10)([SDT])([\*#]?)')
    temp = []
    proc = {'S': lambda x: x, 'D': lambda x: x*x, 'T': lambda x: x**3}
    for n, t, b in pat.findall(dartResult):
        p = proc[t](int(n))
        if b == '#':
            p *= -1
        elif b == '*':
            p *= 2
            if temp:
                temp[-1] *= 2
        temp.append(p)
    return sum(temp)


def test_solution():
    # assert solution("1D2S0T") == 3
    # assert solution("1S2D*3T") == 37
    assert solution("1D2S#10S") == 9
    # assert solution("1S2D*3T") == 37
    # assert solution("1S2D*3T") == 37
    # assert solution("1S2D*3T") == 37
    # assert solution("1S2D*3T") == 37
    # assert solution("1S2D*3T") == 37
