# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
#     if len(answer) == 0:
#         answer.append(-1)
#     answer.sort()
#     return answer


def solution(arr, divisor):
    return sorted(i for i in arr if i % divisor == 0) or [-1]


def test_sample():
    assert solution([5, 9, 7, 10], 5) == [5, 10]
    # assert solution([2, 36, 1, 3], 1) == [1, 2, 3, 36]
    # assert solution([3,2,6], 10) == [-1]