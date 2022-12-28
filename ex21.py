# i=1

# while True:
#     print("{}번째 반복문입니다.".format(i))
#     i += 1
#     input_text =input("> 종료하시겠습니까?(y)")
#     if input_text in ["Y","y"]:
#      print("반복을 종료합니다.")
#     break

numbers = [5,15,6,20,7,25]

for number in numbers:
    # number가 10보다 작으면 다음 반복으로 넘어갑니다.
    if number <10: 
        continue
    elif number<20:
        continue
    #현재 반복을 중지하고, 다음 반복으로 넘어간다.
    print(number)