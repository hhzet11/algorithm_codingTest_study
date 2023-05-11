# 시간 초과!
# arr = str(input())
# bomb = str(input())
# while bomb in arr :
#     arr = arr.replace(bomb, '')
# if len(arr) == 0 :
#     print('FRULA')
# else :
#     print(arr)

import sys
input = sys.stdin.readline
arr = input().rstrip()
bomb = input().rstrip()

stack = []
for i, v in enumerate(arr) :
    stack.append(v)
    if ''.join(stack[-len(bomb) : ]) == bomb :
        for _ in range(len(bomb)) :
            stack.pop()

if stack :
    print(''.join(stack))
else :
    print("FRULA")