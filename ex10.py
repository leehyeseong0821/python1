score = float(input(">학점을 입력해주세요:"))

if score == 4.5:
    print("신")
elif 4.2<= score:
    print("교수님의 사랑")
elif 3.5<= score:
    print("현 체제의 수호자")
elif 2.8<= score:
    print("일반인")    
elif 2.3<= score:
    print("일탈을 꿈구는 소시민")
elif 1.75<= score:
    print("오락문화의 선구자")
else:
    print("바보")
    
number = input("정수입력")
number = int(number)
if number% 2 ==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")