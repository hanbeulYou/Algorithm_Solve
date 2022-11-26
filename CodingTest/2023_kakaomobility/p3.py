def time_to_seconds(day, hour, minuate, second):
    return day * 86400 + hour * 3600 + minuate * 60 + second


def get_time(time):
    day, hour, minuate, second = [int(t) for t in time.split(':')]
    return time_to_seconds(day, hour, minuate, second)


def solution(s, times):
    start = get_time(s[8::])
    date = [start//86400]
    
    for time in times:
        start += get_time(time)
        next_date = start//86400
        if not next_date in date:
            date.append(next_date)
    
    date_len = date[-1]-date[0]+1
    answer = [int(date_len == len(date)), date_len]
    return answer

print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:04:12:00"]))
print(solution("2021:04:12:16:08:35", ["01:06:30:00", "00:01:12:00"]))
print(solution("2021:04:12:16:10:42", ["01:06:30:00"]))
print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:01:12:00", "00:00:09:25"]))