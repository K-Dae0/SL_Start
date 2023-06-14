'''
2023.06.14
202395005 김대영
리스트를 만들고 반복문으로 출력하시오
# 문제분석
    1에서 100 까지에 정수중 10개를 뽑아 리스트에 저장
'''
import random # 항상 첫번째 줄에 import 사용

num1=[]
for i in range(10) :
    num1.append(random.randint(1,100)) # .append는 추가

print("생성된 리스트 :",num1)

print()


