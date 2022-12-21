#변수
#변할 수 있는 숫자
#데이터에 이름을 붙인 것
pi=3.14
print((pi +3.14)*2)

pi =1
pi += 1 #pi=2
pi += 1 #pi=3
pi += 1 #pi=4

# print(pi)

# input(">>>")

# a = input(">>>")
# print(a)
# print(type(a))
# a = (input("첫번째 숫자를 입력해주세요"))
# b = (input("두번째 숫자를 입력해주세요"))
# print(a+b)
# a = int(input("첫번째 숫자를 입력해주세요"))
# b = int(input("두번째 숫자를 입력해주세요"))
# print(a+b)
# a = float(input("첫번째 숫자를 입력해주세요"))
# b = float(input("두번째 숫자를 입력해주세요"))
# print(a+b)

# str_input = input("숫자 입력>")
# num_input = float(str_input)

# print()
# print(num_input, "inch")
# print((num_input*2.54),"cm")


# str_input = input("원의 반지름입력>")
# num_input = float(str_input)

# print("반지름:", num_input)
# print("둘레:",2*3.14*num_input)
# print("넓이",3.14*num_input**2)

a=input("문자열 입력")
b=input("문자열 입력")
print(a,b)
# c=b
# b=a
# a=c
a,b=b,a
print(a,b)