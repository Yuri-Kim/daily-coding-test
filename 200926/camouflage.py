import collections


def solution(clothes):
    # sorted_list = sorted(clothes, key=lambda x: x[1])
    # print(sorted_list)
    key_list = (list(zip(*clothes))[1])
    print(key_list)
    all_key_list = list(set(key_list))
    key_cnt_list = collections.Counter(key_list)
    cnt = 1
    for i in range(0, len(all_key_list)):
        cnt *= (key_cnt_list[str(all_key_list[i])]+1)
    return cnt-1


def test_solution():
    # assert solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5
    assert solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]) == 3
