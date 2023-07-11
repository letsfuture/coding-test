import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = list(input().split())
maxNum = -2147000000

# 01
for i in range(n):
    sum = 0
    for j in range(len(a[i])):
        sum += int(a[i][j])
        if sum > maxNum:
            maxNum = sum
            res = i

print(a[res])

# 02
'''
n = int(input())
a = list(map(int, input().split()))
maxNum = -2147000000

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

for x in a:
    tot = digit_sum(x)
    if tot > maxNum:
        maxNum = tot
        res = x

print(res)
'''