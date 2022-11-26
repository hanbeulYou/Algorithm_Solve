def invite(pairs, ifrom, d):
    if d == 2 :
        p = 0
        for i in pairs :
            if i[0] == ifrom :
                p+=1
        return p

    if d == 1 :
        p1 = 0
        p2 = 0
        for i in pairs :
            if i[0] == ifrom :
                p1 += 3
                p2 += invite(pairs, i[1], 2)
        return p1 + p2
    
    if d == 0 :
        p1 = 0
        p2 = 0
        for i in pairs :
            if i[0] == ifrom :
                p1 += 5
                p2 += invite(pairs, i[1], 1)
        return p1 + p2

def solution(invitationPairs):
    i_dict = {}
    for i in invitationPairs :
        i_dict[i[0]] = invite(invitationPairs, i[0], 0)
    sorted_i = sorted(i_dict.items(), key=lambda x: x[1], reverse=True)
    n = len(sorted_i)
    answer = []
    if n > 3 :
        for i in range(3) :
            answer.append(sorted_i[i][0])
    else :
        for i in range(n) :
            answer.append(sorted_i[i][0])

    return answer

print(solution([[1,2],[2,3],[2,4],[2,5],[5,6],[5,7],[6,8],[2,9]]))