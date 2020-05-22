def solution(arr):
    return sum(arr)/len(arr)


def test_solution():
    assert solution([5, 5]) == 5
    assert solution([1, 2, 3, 4]) == 2.5
