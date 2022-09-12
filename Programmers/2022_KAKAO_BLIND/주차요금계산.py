def fee_compute(fees, time_total):
    if time_total <= fees[0]:
        return fees[1]
    else:
        if (time_total - fees[0]) % fees[2]:
            return fees[1] + ((time_total - fees[0])//fees[2]+1) * fees[3]
        else:
            return fees[1] + ((time_total - fees[0])//fees[2]) * fees[3]

def solution(fees, records):
    cars = dict()
    answer = []

    for record in records:
        time, car, io = record.split()
        h = int(time[0:2])
        m = int(time[3:5])
        if io == 'IN' and car not in cars:
            cars[car] = [h*60+m,]
        else:
            cars[car].append(h*60+m)
    
    tmp = []
    for key, value in cars.items():
        n = len(value)
        idx = 0
        if n%2:
            value.append(24*60-1)
            n+=1
        time_total = 0
        while idx < n - 1:
            time_total += value[idx+1] - value[idx]
            idx += 2
        tmp.append([key, fee_compute(fees, time_total)])
    tmp.sort(key=lambda x:x[0])
    for t in tmp:
        answer.append(t[1])
    return answer

#print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))