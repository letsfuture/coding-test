import sys
sys.stdin = open('input.txt', 'rt')

# python의 round 함수는 round_half_even 방식을 채택하고 있다.
# 4.5와 같이 정확하게 절반이면 짝수 값으로 근사값을 가지게 된다.
# round(4.500) -> 4
# round(4.511) -> 5
# round(5.500) -> 6
# a = 66.5
# a += 0.5
# a = int(a)
# print(a)

n = int(input())
a = list(map(int, input().split()))

avg = round(sum(a)/n)
min = 2147000000

for idx, x in enumerate(a): # enumerate는 리스트의 인덱스값과 인덱스 안의 실제값을 반환해준다.
    tmp = abs(x-avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1 # idx가 0으로 시작하니깐
    elif tmp == min:
        if x > score: # x >= score가 되면 idx가 가장 작은 것이 답이 된다.
            score = x
            res = idx + 1
            
print(avg, res)