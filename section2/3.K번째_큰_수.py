import sys
sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
res = set()

# 01
for i in range(n):
    for j in range(n):
        for k in range(n):
            if ((i!=j) & (i!=k) & (k!=j)):
                res.add(a[i]+a[j]+a[k]) # set은 append가 아니라 add를 써야 함
lst = list(res)
lst.sort(reverse=True)
print(lst[m-1])

# 02
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            res.add(a[i]+a[j]+a[k])
res = list(res)
res.sort(reverse=True)
print(res[m-1])