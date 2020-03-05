def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)
    return answer


def test_sample():
    assert solution([1, 1, 3, 3, 0, 1, 1]) == [1, 3, 0, 1]
    assert solution([4, 4, 4, 3, 3]) == [4, 3]