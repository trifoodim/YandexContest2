# Probelem A
# element = int
# maximum = 0
# counter = 0
# while element != 0:
#     element = int(input())
#     if element > maximum:
#         maximum = element
#         counter = 1
#     elif element == maximum:
#         counter += 1
# print(counter)


# Problem B
# plan=list(map(int, input().split()))


# Problem C
# word = list(input())
# counter = 0
# for i in range(len(word) // 2):
#     if word[i] != word[len(word) - i - 1]:
#         counter += 1
# print(counter)


# Problem D
L, K = map(int, input().split())
ls = list(map(int, input().split(maxsplit=K)))
left_stolbs = []
left = []
right = []
if L // 2 in ls and L % 2 == 1:
        left_stolbs.append(L // 2)
elif L % 2 == 0:
    left = [elem for elem in ls if elem < L // 2]
    right = [elem for elem in ls if elem >= L // 2]

print(left)










# if L // 2 in ls:
#         left_stolbs.append(L // 2)
# else:
#     left = [elem for elem in ls if elem < L // 2]
#     right = [elem for elem in ls if elem > L // 2]
#     left_stolbs.append(max(left))
#     left_stolbs.append(min(right))
#     print(left)
#     print(right)
# print(*left_stolbs)