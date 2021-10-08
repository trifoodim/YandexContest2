# Задача А
# ls1 = set(map(int, input().split()))
# ls2 = set(map(int, input().split()))
# print(len(ls2 & ls1))

# Задача Б
# ls1 = list(map(int, input().split()))
# check = set()
# for i in range(len(ls1)):
#     if ls1[i] not in check:
#         check.add(ls1[i])
#         print('NO')
#     else:
#         print('YES')


# Задача В
# Решение с использованием сторонней библиотеки
# from collections import OrderedDict
# ls1 = list(map(int, input().split()))
# tmp = list(OrderedDict.fromkeys(ls1))
# numbers = []
# for i in range(len(tmp)):
#     if ls1.count(tmp[i]) == 1:
#         numbers.append(tmp[i])
# print(*numbers)

# Решение через два вспомогательных списка
# ls1 = list(map(int, input().split()))
# tmp = []
# numbers = []
# for i in range(len(ls1)):
#     if ls1[i] not in tmp:
#         tmp.append(ls1[i])
# for i in range(len(tmp)):
#     if ls1.count(tmp[i]) == 1:
#         numbers.append(tmp[i])
# print(*numbers)


# Задача Г
# n = int(input())
# all_nums = set(range(1, n + 1))
# possible_nums = all_nums
# while True:
#     guess = input()
#     if guess == 'HELP':
#         break
#     guess = {int(x) for x in guess.split()}
#     answer = input()
#     if answer == 'YES':
#         possible_nums &= guess
#     else:
#         possible_nums &= all_nums - guess
#
# # print(' '.join([str(x) for x in sorted(possible_nums)]))

# n = int(input())
# possible = set(range(1, n + 1))
# s = input().strip()
# while s != 'HELP':
#     nums = set(map(int, s.split()))
#     s = input().strip()
#     if s == 'YES':
#         possible.intersection_update(nums)
#     else:
#         possible.difference_update(nums)
#     s = input().strip()
# print(*sorted(possible))

# Задача Д
m = int(input())
wits = []
for str in range(m):
    wits.append((set(input().strip())))
n = int(input())
nums = []
maxwitcnt = 0
for i in range(n):
    num = input().strip()
    numset = set(num)
    witcnt = 0
    for wit in wits:
        if wit <= numset:
            witcnt += 1
    nums.append((num, witcnt))
    maxwitcnt = max(maxwitcnt, witcnt)
ans = []
for num in nums:
    if num[1] == maxwitcnt:
        ans.append(num[0])
print('\n'.join(ans))




