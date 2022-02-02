num = int(input())
cnt = 0
six = 666
while True:
    if '666' in str(six) :
        cnt += 1 #666이 들어있으면 count 더해주기
    if cnt == num : # count가 num과 같다는 건, 해당 index까지 도달했다는 것
        print(six)
        break
    six += 1 # 666에 1씩 더해주면서 맞는 값을 하나하나 다 확인해보기