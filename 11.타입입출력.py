'''
2023.06.16
202395005 김대영
랜덤으로 10명의 학생의 키와 몸무게를 생성하여 타입에 저장
import random 사용
f_name 변수에 리스트 김 이 박 
'''
import random

f_name=list('김박이차남곽홍정엄')
s_name=list('가나다라마바사아자차카타파하준식')

with open("impo.txt","w") as file :
    for i in range(10) :
        name=random.choice(f_name) + random.choice(s_name) + random.choice(s_name)
        weight=random.randrange(40,100)
        height=random.randrange(140,200)
        file.write('{}, {}, {} \n'.format(name,weight,height))

