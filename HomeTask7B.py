# Problem A.
# На числовой прямой окрасили N отрезков.
# Известны координаты левого и правого концов каждого отрезка (L(i) и R(i)).
# Найти длину окрашенной части числовой прямой.

# n = int(input())
# LeftBound = -1
# RightBound = 1
# larr = []
# rarr = []
# for i in range(n):
#     L, R = map(int, input().split())
#     larr.append(L)
#     rarr.append(R)
# line = []
# for i in range(n):
#     line.append((larr[i], LeftBound))
#     line.append((rarr[i], RightBound))
# line.sort()
# openedSegments = 0
# notemptyline = 0
# for i in range(len(line)):
#     if openedSegments > 0:
#         notemptyline += line[i][0] - line[i - 1][0]
#     if line[i][1] == LeftBound:
#         openedSegments += 1
#     elif line[i][1] == RightBound:
#         openedSegments -= 1
# print(notemptyline)


# Problem B.
# В выходной файл выведите одно число – наименьшее количество аппаратов,
# которое нужно установить, чтобы не вызвать подозрений у Министерства.

# n = int(input())
# LeftBound = 1
# RightBound = -1
# larr = []
# rarr = []
# for i in range(n):
#     L, T = map(int, input().split())
#     larr.append(L)
#     rarr.append(L + T)
# line = []
# for i in range(n):
#     line.append((larr[i], LeftBound))
#     line.append((rarr[i], RightBound))
# line.sort()
# openedSegments = 0
# maxMachineTools = 0
# for i in range(len(line)):
#     if line[i][1] == LeftBound:
#         openedSegments += 1
#     elif line[i][1] == RightBound:
#         openedSegments -= 1
#     maxMachineTools = max(maxMachineTools, openedSegments)
# print(maxMachineTools)


# Problem D. Наполненность котятами.
n, m = map(int, input().split())
catsPos = list(map(int, input().split()))
catsPos.sort()
larr = []
rarr = []
for i in range(m):
    L, R = map(int, input().split())
    larr.append(L)
    rarr.append(R)
events = []
LeftBound = -1
CatCome = 0
RightBound = 1
for i in range(m):
    events.append((larr[i], LeftBound, i))
    events.append((rarr[i], RightBound, i))
for i in range(n):
    events.append((catsPos[i], CatCome))
events.sort()
ans = [0] * n
for i in range(len(events)):
    if events[i][1] == -1