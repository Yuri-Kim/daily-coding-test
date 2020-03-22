# 맨앞 글자가 -일때만 -숫자 나머지는 무조건 숫자 -> 이 말은 곧 +없애고 나머지는 int로


# 이렇게 풀었지만 이게 정답일리 없지...
def solution(s):
    return int(s)
    # return int(s[1:]) if list(s)[0] == "+" else int(s)


# 이 사람 풀이 +고려해서 다시 확인해보기
# def solution(str):
#     result = 0
#
#     for idx, number in enumerate(str[::-1]):
#         if number == '-':
#             result *= -1
#         else:
#             result += int(number) * (10 ** idx)
#
#     return result


def test_solution():
    assert solution("1234") == 1234
    assert solution("-1234") == -1234
    assert solution("+1234") == 1234