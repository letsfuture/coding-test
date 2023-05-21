# -*- coding: utf-8 -*-
"""01_K번쨰_약수.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ssR8i8vAmBWjRddl_vTWGq5hqdFvxPl3

# K번째 약수

두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을
작성하시오.<br><br>
**입력 설명**<br>
첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N
이하이다.<br><br>
**출력 설명**<br>
첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서
K번째 약수가 존재하지 않을 경우에는 -1을 출력하시오.
"""

n, k = map(int, input().split())

cnt = 0
for i in range(1, n+1):
  if n%i==0:
    cnt+=1
  if cnt==k:
    print(i)
    break
# 정상적으로 실행됐다면
else:
  print(-1)

