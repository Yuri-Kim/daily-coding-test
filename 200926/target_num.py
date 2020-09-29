def solution(numbers, target):
    cnt = 0
    len_num = len(numbers)
    def oper(index=0):
        if index < len_num:
            numbers[index] *= 1
            oper(index+1)

            numbers[index]*= -1
            oper(index+1)

        elif sum(numbers) == target:
            nonlocal cnt
            cnt += 1

    oper()

    return cnt


def test_solution():
    assert solution([1, 1, 1, 1, 1], 3) == 5
