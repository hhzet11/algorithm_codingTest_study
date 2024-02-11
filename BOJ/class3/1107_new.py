'''
n = int(input())
m = int(input())

if m == 0 :
    print(len(str(n)))

elif n == 100 :
    print(0)

else:
    broken = list(map(int, input().split()))
    num_list = []
    # n보다 큰 채널
    c = ''
    for j in str(n):
        j = int(j)
        if j not in broken:
            c += str(j)
        else:
            while j in broken :
                j += 1
                if j > 9 and len(c) > 0:
                    j = 0
                    c = str(int(c) + 1)
                elif j > 9 and len(c) == 0:
                    j = 10
            c += str(j)
    num_list.append(int(c))

    #n보다 작은 채널
    c = ''
    for j in str(n):
        j = int(j)
        if j not in broken:
            c += str(j)
        else:
            while j in broken:
                j -= 1
                if j < 0 and len(c) > 0:
                    j = 9
                    c = str(int(c) - 1)
                elif j < 0 and len(c) == 0 :
                    j = 0

            c += str(j)
    num_list.append(int(c))
    print(num_list)
    c = min(num_list[0] - n + len(str(num_list[0])), n - num_list[1] + len(str(num_list[1])))
    print(c)
'''

# 앞선 방법으로 80000의 경우, 79999가 효과적임에도 불구하고 70000으로 탐색함
# 즉 위의 방법이 아닌 정말 모든 번호에 대해 모두 탐색하는 브루트포스 알고리즘이 필요함

n = int(input())
m = int(input())
if m != 0 :
    broken = list(input().split())
else:
    broken = []

count = abs(100 - n)
for i in range(1000001):
    for j in str(i):
        if j in broken:
            break
    else :
        count = min(count, len(str(i)) + abs(i-n))

print(count)