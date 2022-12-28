# print(min(273,52,32,5,103))
# print(max(273,52,32,5,103))
# print(sum([273,52,32,57,103]))
a=[0,1,2,3,4,5]
reversed_a = reversed(a)
for i in reversed_a:
    print(i, end=" ")
print()
for i in reversed_a:
    print(i, end="")

b=[273,103,52,32,57]
for i, element in enumerate(b):
    print("{}번째 요소는 {} 입니다".format(i,element))