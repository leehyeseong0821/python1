# dictionary ={
#     "이름": "구름",
#     "종족": "강아지"
    
# }

# if dictionary.get("나이") ==None:
#  dictionary.get("나이")
# else:
#     print("없는 키입니다.")    
# dict_a={
    
# }
# dict_a["name"]="구름"
# del dict_a["name"]
# print(dict_a)

# pets = [
#     {"name": "구름","age":5},
#     {"name": "초코","age":3},
#     {"name": "아지","age":1},
#     {"name": "호랑이","age":1}
# ]
# print("#우리 동네 애완 동물들")
# for pet in pets:
#  print("{} {}살".format(pet["name"],pet["age"]))

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}
 
for number in numbers:
     if number in counter:
        counter[number] += 1     
     else:
        counter[number] = 1
        
        print(counter)