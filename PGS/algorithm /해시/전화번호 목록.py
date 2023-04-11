def solution(phone_book):
    answer = True
    # 1차 시도 - 실패
    phone_book.sort() # 적용하고 해결
    for i, num in enumerate(phone_book[:-1]):
        next = phone_book[i+1]
        if num == next[:len(num)] :
            answer = False
            break
    return answer

# 다른 사람 풀이
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True