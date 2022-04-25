# 1번. 손익분기점
# A : 고정비용
# B : 가변비용
# C : 책정된 제품의 판매가격

# 손익분기점(BEP) : 총 수입이 총비용보다 많아져 이익이 발생하는 지점
# -> C = A + B  : 이익도 손해도 없는 지점

a,b,c = map(int,input().split())

if b >= c:  # 가변비용이 노트북 가격보다 같거나 크면
    print(-1)
else:
    print(a/(c-b)+1)


# 2번. 벌집

N = int(input())

number = 1 # 벌집 갯수
counts = 1 # 경로 갯수

while N > number:
    number += 6 * counts
    counts += 1
    
print(counts)

# 3번 (분수찾기)
X = int(input())

line = 0
max_X = 0
while X > max_X:
    line += 1    # 대각선 순서
    max_X += line  # 해당 대각선에서 가장 큰 X점

gap = max_X - X

if line % 2 == 0:
    numer = line - gap
    denomi = gap + 1
else:
    numer = gap + 1
    denomi = line - gap 

print(f'{numer}/{denomi}')

# 4번 문제 달팽이

# 높이 V / 낮 A(+) / 밤 B(-)
import math
A, B, V = map(int, input().split())

# (V-B) = (A-B)x ( x : 며칠 )
# (V-B) /(A-B) = x

day = (V-B) /(A-B)
print(math.ceil(day))


# day_count = 1

# while True:
#     if V - A > 0:
#         V -= (A - B) 
#         day_count += 1
#     else:
#         break
# print(day_count)

# 5번 문제 호텔

# H : 층 수, W : 각 층의 방 수, N 몇 번째 손님

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    num = N//H + 1

    floor = N % H

    if N % H == 0:
        num = N//H
        floor = H

    print(f'{floor*100+num}')

    # if N % H == 0:
    #     Y = H
    # else:
    #     Y = N % H

    # if N  // H < 1:
    #     X = 1        
    # elif N // H == N/H:
    #     X = N/H
    # else:
    #     X = (N // H) + 1

    # if X < 10:
    #     print(f'{Y}0{X}')
    # else:
    #     print(f'{Y}{X}')

# 6번 반상회

# k층 n호
# k-1층 1~n호까지의 사람들의 수의 합만큼
# 아파트는 0층 1호부터 
T = int(input())

for i in range(T):
    floor = int(input())
    num = int(input())
    zero_f = [x for x in range(1,num+1)]

    for j in range(floor):
        for k in range(1, num):
            zero_f[k] += zero_f[k-1]
    print(zero_f[-1])

# 7번 설탕 배달

# N kg 설탕 배달
# 봉지종류 : 3kg, 5kg
#  최대한 적은 봉지
N = int(input())

plastic_bag = 0

while N >= 0:
    if N % 5 == 0: 
        plastic_bag += N // 5 # 5로 나눈 몫 -> 봉지 수 한 번에 추가
        print(plastic_bag)     # 0을 5로 나눈 나머지는 0이 될까? 된다
        break
    N -= 3 # 설탕이 5의 배수가 될때까지
    plastic_bag += 1 # 봉지 추가
else:
    print(-1) # while 문이 거짓이면 -1 출력

# 8번 문제???

# 큰 수 A+B

A, B = map(int, input().split())

print(A+B)
