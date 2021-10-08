# Problem A
# r = int(input())
# i = int(input())
# c = int(input())
# if (i == 0 or i == 4) and r != 0:
#     print(3)
# elif i == 0 and r == 0:
#     print(c)
# elif i == 1:
#     print(c)
# elif i == 4 and r == 0:
#     print(4)
# elif i == 6:
#     print(0)
# elif i == 7:
#     print(1)
# else:
#     print(i)


# Problem B
# stations = list(map(int, input().split()))
# if stations[2] > stations[1]:
#     pos = stations[2] - stations[1] - 1
#     neg = stations[0] + stations[1] - stations[2] - 1
#     if pos <= neg:
#         print(pos)
#     else:
#         print(neg)
# elif stations[2] < stations[1]:
#     neg = stations[1] - stations[2] - 1
#     pos = stations[0] + stations[2] - stations[1] - 1
#     if pos <= neg:
#         print(pos)
#     else:
#         print(neg)


# Problem C
# data = list(map(int, input().split()))
# if data[0] <= 12 and data[1] <= 12 and data[0] != data[1]:
#     print(0)
# else:
#     print(1)


# Problem D
#  Acceptable solution
# number = int(input())
# places = list(map(int, input().split()))
# mid_elem_index = len(places) // 2
# print(places[mid_elem_index])
#  Time limit solving
# min_distance = float('Inf')
# min_index = -1
# for i in range(len(places)):
#     sum = 0
#     for j in range(len(places)):
#         sum = sum + abs(places[i] - places[j])
#     if sum <= min_distance:
#         min_distance = sum
#         min_index = i
# print(places[min_index])


# Problem E
d = int(input())
x, y = map(int, input().split())
if x in range(d + 1) and y in range(d + 1) and x + y <= d:
    print(0)
else:
    if (x < 0 and y < 0) or (x == 0 and y < 0) or (x < 0 and y == 0) or (x < 0 and y > 0 and y <= d // 2) or (x > 0 and y < 0 and x <= d // 2):
        print(1)
    elif (x > d and y == 0) or (x > 0 and y < 0 and x > d // 2) or (x > 0 and y > 0 and x + y > d and y <= x):
        print(2)
    elif (x == 0 and y > d) or (x < 0 and y > 0 and y > d // 2) or (x > 0 and y > 0 and x + y > d and y > x):
        print(3)
