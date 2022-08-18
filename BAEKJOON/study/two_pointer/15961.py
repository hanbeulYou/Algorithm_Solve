# 풀이가 많이 지저분합니다. 
import sys

n, d, k, c = map(int,sys.stdin.readline().split())
sushi = []
for _ in range(n) :
    sushi.append(int(sys.stdin.readline())) # timeout을 조금이라도 줄이고자 들인 노력

s_idx = 0
e_idx = k
cnt = 0
cnt_sushi = [0 for _ in range(3001)] # sushi의 중복 체크 겸 

for idx in range(k) : # 0 ~ k-1 까지 초밥 가짓수 count
    cnt_sushi[sushi[idx]] += 1
    if cnt_sushi[sushi[idx]] == 1 :
        cnt += 1

max_cnt = cnt
coupon = False # 내가 먹은 초밥들 중에 쿠폰 사용 가능한지?

if cnt_sushi[c] != 0 :
    coupon = True

if k != n :
    while s_idx < n : # s_idx, e_idx 1칸씩 늘려가며 cnt_sushi 변경 + 가짓수 count
        cnt_sushi[sushi[s_idx]] -= 1
        if cnt_sushi[sushi[s_idx]] == 0 : # start 인덱스 부분 삭제
            cnt -= 1
        cnt_sushi[sushi[e_idx]] += 1 # end 인덱스 부분 추가
        if cnt_sushi[sushi[e_idx]] == 1 :
            cnt += 1

        if max_cnt < cnt : # max값 찾기
            max_cnt = cnt
            if cnt_sushi[c] != 0 :
                coupon = True

        if max_cnt == cnt and coupon and cnt_sushi[c] == 0 : # 만약 count가 기존 max랑 같은데 얜 쿠폰 초밥을 안먹었을 때
            coupon = False

        if e_idx == n - 1 : # 회전
            e_idx = 0
            s_idx += 1

        else : 
            s_idx += 1
            e_idx += 1

else : # 만약 k==n일 경우 바로 빼버리기
    if cnt_sushi[c] != 0 :
        max_cnt -= 1

if coupon : # 쿠폰으로 먹을 수 있는 애를 이미 먹었을 경우
    print(max_cnt)

else : # 아닐 경우 1 종류 추가
    print(max_cnt + 1)