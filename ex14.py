a=[1,2,3,4,5,6,7]

for element in a:
    print(element)
    

numbers = [273,103,5,32,65,9,72,800,99]


#  if number >=100 :
#      print("- 100 이상의 수:{}".format(number))     
# for number in numbers:
#  if number % 2 ==0 :
#     print("-{}는 짝수입니다.".format(number))
#  else:
#     print("-{}는 홀수 입니다.".format(number))

for number in numbers:
    print("{}는{}자리수 입니다.".format(number, len(str(number))))
    
    list_of_list =[
        [1,2,3],
        [4,5,6],
        [8,9]
    ]
    for a in list_of_list:
        for b in a:
            print(b)
   
   
   