# lambda 쓰면 될거같은데 n번째 글자가 같은 경우에 대한 처리 필요
# n번째 글자가 같은 경우에는 사전순이니까 걍 lambda전에 정렬한번 하면 될듯


def solution(strings, n):
    strings = sorted(strings)
    return sorted(strings, key=lambda strings:strings[n])


def test_sample():
    assert solution(['sun', 'bed', 'car'], 1) == ['car', 'bed', 'sun']
    assert solution(['abce', 'abcd', 'cdx'], 2) == ['abcd', 'abce', 'cdx']