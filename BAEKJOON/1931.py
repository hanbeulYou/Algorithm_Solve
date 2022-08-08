n = int(input())
meetings = []
for _ in range(n) :
    meetings.append(tuple(map(int, input().split())))

meetings.sort(key=lambda x:(x[1],x[0]))
cnt = 1
end = meetings[0][1]
for idx, meeting in enumerate(meetings) :
    if idx == 0 :
        continue
    if meeting[0] < end :
        continue
    else :
        cnt += 1
        end = meeting[1]
print(cnt)