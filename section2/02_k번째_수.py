# -*- coding: utf-8 -*-
"""02_K번째_수.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XLJOFQ-OqAr8vDre6eUg_glKHV4Nyvea

# K번째 수

N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하시요.<br><br>

**입력 설명**<br>
첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어진다.
각 케이스별
첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다.
두 번째 줄에 N개의 숫자가 차례로 주어진다.<br><br>
**출력 설명**<br>
각 케이스별 k번째 수를 아래 출력예제와 같이 출력하시오.
"""

T = int(input())

for t in range(T):
  n, s, e, k = map(int, input().split())
  a = list(map(int, input().split()))
  a = a[s-1:e]
  a.sort()
  print('#%d %d' %(t+1, a[k-1]))

