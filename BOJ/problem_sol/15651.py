'''
1. 아이디어
- 백트래킹하는 함수 안에서 For문을 돌면서 숫자 선택
- 재귀함수에서 m개 선택할 경우 print
2. 시간복잡도
- 중복이므로 n^2 : n최대 7이므로 가능
3. 자료구조
- 결과값 저장 : int[]
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
def recur(num):
    if num == m :
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        result.append(i)
        recur(num+1)
        result.pop()
recur(0)