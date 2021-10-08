# Problem A

# def l_binary_search(l, r, check, check_params):
#     while l < r:
#         m = (l + r) // 2
#         if check(m, check_params):
#             r = m
#         else:
#             l = m + 1
#     return l
#
# def r_binary_search(l, r, check, check_params):
#     while l < r:
#         m = (l + r + 1) // 2
#         if check(m, check_params):
#             l = m
#         else:
#             r = m - 1
#     return l
#
# n = int(input())
# cut = list(map(int, input().split()))
# cut.sort()
# cnt_pairs = int(input())
# ans = []
# for pair in range(cnt_pairs):
#     l = 0
#     r = len(cut) - 1
#     L, R = map(int, input().split())
#     while l < r:            # left number search
#         m = (l + r) // 2
#         if cut[m] >= L:
#             r = m
#         else:
#             l = m + 1
#     st = l - 1
#     l = 0
#     r = len(cut) - 1
#     while l < r:            # right number search
#         m = (l + r + 1) // 2
#         if cut[m] <= R:
#             l = m
#         else:
#             r = m - 1
#     end = l
#     print(end, st)
#     ans.append(end - st)
# print(*ans)


# Problem B
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))
# for x in b:
#     left = -1
#     right = len(a)
#     #левый бинпоиск, который ищет левую границу
#     while right - left > 1:
#         middle = (right + left) // 2
#         if a[middle] < x:
#             left = middle
#         else:
#             right = middle
#
#     left_1 = -1
#     right_1 = len(a)
#     #правый бинпоиск, который ищет правый границу
#     while right_1 - left_1 > 1:
#         middle = (right_1 + left_1) // 2
#         if a[middle] <= x:
#             left_1 = middle
#         else:
#             right_1 = middle
#
#     if left == left_1 and right == right_1:
#         print(0, 0)
#         continue
#     if right == left_1:
#         print(right + 1, right + 1)
#     else:
#         print(right + 1, left_1 + 1)


# Problem C
# eps = 0.00001
# a, b, c, d = map(float, input().split())
# if a < 0:
#     a, b, c, d = -a, -b, -c, -d
#
# def f(x):
#     return a * x**3 + b * x**2 + c * x + d
# def root():
#     left = -2000
#     right = 2000
#     while right - left > eps:
#         mid = (left + right) / 2
#         if f(mid) > 0:
#             right = mid
#         else:
#             left = mid
#     return (left + right) / 2
#
# print(root())


# Problem D
# a, k, b, m, x = map(int, input().split())
# l = 0
# r = x * 2 // a + 1
# while l < r:
#     days = (l + r) // 2
#     hd = days // k
#     hf = days // m
#     lumber = (days - hd) * a + (days - hf) * b
#     if lumber < x:
#         l = days + 1
#     else:
#         r = days
# print(l)


# Problem E
n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
left = 0
right = x[-1] - x[0]
while left < right:
    l = (right + left) // 2
    cnt = 0
    rmax = x[0] - 1
    for nowx in x:
        if nowx > rmax:
            cnt += 1
            rmax = nowx + l
    if cnt <= k:
        right = l
    else:
        left = l + 1
print(left)