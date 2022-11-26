def solution(s):
    s = list(s)
    n = len(s)
    max = -1
    for idx, c in enumerate(s) :
        if idx == n - 2 :
            break
        if s[idx] == s[idx+1] and s[idx] == s[idx+2] :
            if max < int(s[idx]) :
                max = int(s[idx])
    if max != -1 :
        max = max * 111
    return max