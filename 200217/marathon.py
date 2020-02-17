import collections


def solution(participant, completion):
    # participant.sort()
    # completion.sort()
    #
    # for par, com in zip(participant, completion):
    #     if par != com:
    #         return par
    #
    # return participant[-1]
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]


def test_sample():
    assert solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo"
    assert solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]) == "vinko"
    assert solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) == "mislav"
    assert solution(["mislav", "stanko", "mislav", "ana"], ["mislav", "ana", "mislav"]) == "stanko"
