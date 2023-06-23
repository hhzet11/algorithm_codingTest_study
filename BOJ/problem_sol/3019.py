# 1차시도 시패 : 이유모르겠음 
# import sys
# input = sys.stdin.readline
# 
# c, p = map(int, input().split())
# num = list(map(int, input().split()))
# 
# block = [[], ['0000'], ['00'], ['001', '10'], ['100', '01'], ['101', '000', '01', '10'],
#          ['000', '00', '011', '20'], ['000', '02', '110', '00']]
# total = 0
# for b in block[p] :
#     length = len(b)
#     for i in range(c - length + 1) :
#         key_list = num[i:i+length]
#         key = ''
#         for k in key_list :
#             key += str(k - min(num[i:i+length]))
#     if key == b :
#         total += 1
# if p == 1 :
#     total += c
# print(total)

# 다른 사람 풀이
#1. 각블록마다 회전하여 놓았을때 딱맞을 수 있는 높이의 경우를 구해줌
#2. 그 경우에 해당하면 ans를 1씩 증가시킴

import sys

c,p=map(int,input().split())
fd=list(map(int,sys.stdin.readline().split()))

ans=0
if p==1:
    #ㅣ모양의 블럭은 모든열에 놓을 수 있기 때문에 c만큼 경우의 수를 더함
    ans=ans+c  #0
    for i in range(c-3):
        #0000
        if fd[i] == fd[i + 1] and fd[i + 1] == fd[i + 2] and fd[i + 2] == fd[i + 3]:
            ans+=1
if p==2:
    for i in range(c-1):
        #00
        if fd[i] == fd[i + 1]:
            ans+=1
if p==3:
    for i in range(c-2):
        #001
        if fd[i] == fd[i + 1] and fd[i + 1] == fd[i + 2] - 1:
            ans+=1
    for i in range(c-1):
        #10
        if fd[i] == fd[i + 1] + 1:
            ans+=1
if p==4:
    for i in range(c-2):
        #100
        if fd[i] == fd[i + 1] + 1 and fd[i + 1] == fd[i + 2]:
            ans+=1
    for i in range(c-1):
        #01
        if fd[i] == fd[i + 1] - 1:
            ans+=1
if p==5:
    for i in range(c-2):
        #000
        if fd[i] == fd[i + 1] and fd[i + 1] == fd[i + 2]:
            ans+=1
        #101
        if fd[i] == fd[i + 1] + 1 and fd[i + 1] == fd[i + 2] - 1:
            ans+=1
    for i in range(c-1):
        #10
        if fd[i] == fd[i + 1] - 1:
            ans+=1
        #10
        if fd[i] == fd[i + 1] + 1:
            ans+=1
if p==6:
    for i in range(c-2):
        #000
        if fd[i]==fd[i+1] and fd[i+1]==fd[i+2]:
            ans+=1
        #011
        if fd[i]==fd[i+1]-1 and fd[i+1]==fd[i+2]:
            ans+=1
    for i in range(c-1):
        #00
        if fd[i]==fd[i+1]:
            ans+=1
        #20
        if fd[i]==fd[i+1]+2:
            ans+=1
if p==7:
    for i in range(c-2):
        #000
        if fd[i]==fd[i+1] and fd[i+1]==fd[i+2]:
            ans+=1
        #110
        if fd[i]==fd[i+1] and fd[i+1]==fd[i+2] + 1:
            ans+=1
    for i in range(c-1):
        #02
        if fd[i]==fd[i+1]-2:
            ans+=1
        #00
        if fd[i]==fd[i+1]:
            ans+=1

print(ans)