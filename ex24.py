# array = []
# for i in range(0,20,2):
#     array.append(i*i)
    
# print(array)
# array_1 = [i for i in range(10)]
# array_2 = [i for i in range(0,10,2)]
# array_3 = [1 for i in range(10)]
# array_4 = [i for i in range(10) if i% 3==0]
# print(array_1)
# print(array_2)
# print(array_3)
# print(array_4)
#1~100 /2진수 / 0이 하나만 포함된 숫자> 합!!

for i in range(1,101):
    print(i)
    print("{:b}".format(i))