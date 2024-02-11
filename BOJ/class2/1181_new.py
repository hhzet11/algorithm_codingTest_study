n = int(input())
word = []
for i in range(n):
    word.append(input())
word = list(set(word))
word = sorted(word)
word = sorted(word, key = lambda x:len(x))
for i in word:
    print(i)