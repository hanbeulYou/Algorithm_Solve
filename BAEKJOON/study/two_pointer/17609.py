T = int(input())
cnt = 0
out = 0

def is_palin(str_list, s, e) : # 회문 검사
    global cnt
    while e - s > 0 : # start_idx 와 end_idx가 뽑뽀하기 전까지 가까이 오게함
        if str_list[s] != str_list[e] : # 만약 양쪽 끝에서 오다가 다른걸 만났을 때
            if cnt == 1 : # 이미 한번이라도 만난 적이 있으면 False
                return False
            else : # 처음 만난거면
                cnt += 1
                if is_palin(str_list, s + 1, e) : # 왼쪽 값 하나 지우고 회문 검사 -> 회문일 시 1 출력
                    print(1)
                elif is_palin(str_list, s, e - 1) : # 오른쪽 값 하나 지우고 회문 검사 -> 회문일 시 1 출력
                    print(1)
                else : # 두번 다 지워봤는데 회문이 아니므로 2 출력
                    print(2) 
        else : # 두 값이 같으면 계속 한 칸씩 전진
            s += 1
            e -= 1
    if cnt == 0 : # while이 다 돌았는데 만난 개수가 0개 -> 회문
        print(0)
    else : # while이 다 돌았는데 만난 개수가 0개가 아님 -> 재귀 들어왔으니 True return
        return True
            

for _ in range(T) :
    str_list = list(input())
    start_idx = 0
    end_idx = len(str_list) - 1
    cnt = 0
    is_palin(str_list, start_idx, end_idx)