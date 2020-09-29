def solution(tickets):
    tickets.sort(reverse=True)
    print(tickets)
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    st = ['ICN']
    ans = []
    while st:
        top = st[-1]
        if top not in routes or len(routes[top])==0:
            ans.append(st.pop())
        else:
            st.append(routes[top].pop())
    ans.reverse()
    return ans


def test_solution():
    assert solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"]
    assert solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
