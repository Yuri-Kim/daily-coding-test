def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
        answer.append(get_num(array, commands[i]))
    return answer


def get_num(array, commands_unit):
    slice_array = sorted(array[commands_unit[0] - 1:commands_unit[1]])
    return slice_array[commands_unit[2]-1]


def test_sample():
    assert solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]


# 미쳤다
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))