x, y = map(int, input().split())
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(0, x-1):
    y += mon[i]
print(day[y % 7 -1])