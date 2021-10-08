# Problem 1
# n = int(input())
# dct = {}
# for pair in range(n):
#     key, item = map(int, input().split())
#     if key not in dct.keys():
#         dct[key] = 0
#     dct[key] += item
# for k in sorted(dct.keys()):
#     print(k, dct[k])

# Problem B Не решена
# import sys
# dct = {}
# for line in sys.stdin:
#     key, item = line.strip().split()
#     if key not in dct.keys():
#         dct[key] = 0
#     dct[key] += int(item)
# for k in sorted(dct.keys()):
#     print(k, dct[k])

# Problem C
# wordcnt = {}
# # with open('input.txt', 'r', encoding='utf8') as file: # хороший способ открытия файла
# file = open('input.txt', 'r', encoding='utf8')
# for line in file:
#     words = line.split()
#     for word in words:
#         wordcnt[word] = wordcnt.get(word, 0) + 1
# file.close()
# ans = []
# for word in wordcnt:
#     ans.append((-wordcnt[word], word))
# ans.sort()
# for wordcnt, word in ans:
#     print(word)


# Problem D
# partys = []
# sumcnt = 0
# i = 0
# file = open('input.txt', 'r')
# for line in file:
#     words = line.split()
#     cnt = int(words[-1])
#     partynName = ' '.join(words[:-1])
#     partys.append([partynName, cnt, i])
#     sumcnt += cnt
#     i += 1
# file.close()
# f = sumcnt / 450
# free = 450
# for i in range(len(partys)):
#     party = partys[i]
#     party.append(party[1] // f)
#     free -= party[1] // f
#     party.append(party[1] % f)
# partys.sort(key=lambda x: x[4], reverse=True)
# for i in range(int(free)):
#     partys[i][3] += 1
# partys.sort(key=lambda x: x[2])
# for party in partys:
#     print(party[0], int(party[3]))

# Problem E
n = int(input())
reply = [0] * n
topics = [''] * n
for i in range(n):
    num = int(input())
    if num == 0:
        reply[i] = i
        topics[i] = input()
        input()
    else:
        reply[i] = reply[num - 1]
        input()
cntreplies = {}
for rep in reply:
    cntreplies[rep] = cntreplies.get(rep, 0) + 1
ans = []
for topic in cntreplies:
    ans.append((-cntreplies[topic], topic))
print(topics[min(ans)[1]])
