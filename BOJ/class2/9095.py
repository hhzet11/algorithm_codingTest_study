T = int(input())
def fact(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return fact(num-1) * num

for _ in range(T):
    n = int(input())
    cnt = 0
    for x in range(n+1):
        for y in range((n//2)+1):
            for z in range((n//3)+1):
                if x + 2*y + 3*z == n:
                    cnt += fact(x+y+z)/(fact(x) * fact(y) * fact(z))
    print(int(cnt))

'''
test_case=int(input())

input_list=[]
for i in range(test_case):
    input_list.append(int(input()))
dp=[1,2,4]

for i in range(3,max(input_list)):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in input_list:
    print(dp[i-1])
'''