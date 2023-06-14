'''
2023.06.14
202395005 김대영
# 문제 분석
    -사용자가 입력한 값과 컴퓨터가 생성한 랜덤 값을 비교
    -몇번만에 맞췄는지 알려주는 프로그램
    -사용자에게 힌트를 준다
        -사용자가 입력한 값이 랜덤 값보다 크면 숫자가 작다고 출력
        -사용자가 입력한 값이 랜덤 값보다 작으면 숫자가 크다고 출력
    -사용자가 값을 입력하여 힌트를 받을 때 마다 카운트를 증가
    -사용자가 0을 입력할 시 게임 종료
# 알고리즘
    1.
'''
import random # 랜덤 모듈 생성

random_num = (random.randint(1,30))
int(random_num)

cnt=0 # 횟수

while True : # 무한 반복
    user_num=int(input("1부터 30 사이의 정수 입력(0을 입력시 종료) : "))

    if user_num==0 : # user_num가 0일 때 출력
        print("포기하시나요?")
        continue_ox=input("Yes or No : ")
        if continue_ox == "Yes" :
            break
        elif continue_ox == "No" :
            continue
    
    elif cnt==10 :
        print("벌써 10번이나 틀렸군")

    elif user_num > random_num :
        print("입력한 숫자보다 작습니다.") # user_num이 random_num보다 클 때 출력
        cnt+=1

        if cnt==10 :
            print("벌써 10번이나 틀렸군")
            
    elif user_num < random_num :
        print("입력한 숫자보다 큽니다.") # user_num이 random_num보다 작을 때 출력
        cnt+=1

        if cnt==10 :
            print("벌써 10번이나 틀렸군")

    else :
        print("축하합니다 {}번째만에 맞췄습니다.".format(cnt))
        break

    
        
        
    
