# Problem A
# n, q = map(int, input().split())
# query = [int(i) for i in input().split()]
# prefixSum = [0] * (len(query) + 1)
# for i in range(1, len(query) + 1):
#     prefixSum[i] = prefixSum[i - 1] + query[i - 1]
# for pair in range(q):
#     left, right = map(int, input().split())
#     print(prefixSum[right] - prefixSum[left - 1])

# Problem B. Kadane's algorithm
# n = int(input())
# sequence = [int(i) for i in input().split()]
# max_so_far = sequence[0]
# max_ending_here = 0
#
# for i in range(len(sequence)):
#     max_ending_here = max_ending_here + sequence[i]
#     if (max_so_far < max_ending_here):
#         max_so_far = max_ending_here
#     if max_ending_here < 0:
#         max_ending_here = 0
#
# print(max_so_far)


# Problem C. Не сделал самостоятельно
# def readandnum():
#     x = list(map(int, input().split()))
#     for i in range(len(x)):
#         x[i] = (x[i], i + 1)
#     x.sort()
#     return x
#
# n, m = map(int, input().split())
# x = readandnum()
# y = readandnum()
# ynum = 0
# ans = [0] * (n + 1)
# cnt = 0
# for pupils, xnum in x: # количество людей и номер группы
#     while ynum < len(y) and y[ynum][0] < pupils + 1:
#         ynum += 1
#     if ynum == len(y):
#         break
#     ans[xnum] = y[ynum][1]
#     ynum += 1
#     cnt += 1
# print(cnt)
# print(*ans[1:])


# Problem D
# strn = list(input())
# counter = 0
# for i in range(len(strn)):
#     if strn[i] == '(':
#         counter += 1
#     else:
#         counter -= 1
#     if counter < 0:
#         print('NO')
#         break
# if counter == 0:
#     print('YES')
# elif counter > 0:
#     print('NO')


# Procblem E. Перебор всего кроме последнего. Решается с помощью словаря или двух указателей
def readandnum():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        x[i] = x[i], i
    x.sort()
    return x

s = int(input())
a = readandnum()
b = readandnum()
c = readandnum()
c.sort(key=lambda x: (x[0], -x[1]))
flag = False
for aval, apos in a:
    cpos = len(c) - 1
    for bval, bpos in b:
        while cpos > 0 and aval + bval + c[cpos][0] > s:
            cpos -= 1
        if aval + bval + c[cpos][0] == s and (not flag or (apos, bpos, cpos) < ans):
            ans = apos, bpos, c[cpos][1]
            flag = True
if flag:
    print(*ans)
else:
    print(-1)