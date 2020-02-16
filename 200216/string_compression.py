# 문자열의 길이 a 구해서
# 1부터 a 단위로 잘라봄
# 자른 단위씩 증가하면서 input 이랑 비교
# 같은 문자열이면 숫자 + 1 / 다른 문자열이면 비교문자열 바꾸고 저장될 문자열 변경(숫자+문자열)
# 원래 answer 보다 짧으면 answer 변경


def solution(s):
    min_len = len(s)

    for i in range(1, len(s)+1):
        output_sen = ''
        split_sen = s[0:i]
        zip_cnt = 1

        for j in range(i, len(s)+1, i):
            if split_sen == s[j:j+i]:
                zip_cnt += 1
            else:
                output_sen += "{}".format(zip_cnt if zip_cnt > 1 else '') + split_sen
                split_sen = s[j:j+i]
                zip_cnt = 1

        output_sen += split_sen

        if min_len > len(output_sen):
            min_len = len(output_sen)

    answer = min_len
    return answer


def test_sample():
    assert solution("aabbaccc") == 7
    assert solution("ababcdcdababcdcd") == 9
    assert solution("abcabcdede") == 8
    assert solution("abcabcabcabcdededededede") == 14
    assert solution("xababcdcdababcdcd") == 17
