import sys

len = sys.stdin.readline()
num1 = list(map(int,sys.stdin.readline()))
len = sys.stdin.readline()
num2 = list(map(int, sys.stdin.readline()))
ans = list(map(lambda n : n in num1, num2))

for _ in range (0,len):
    print("%d"%ans[_], end=" ")
