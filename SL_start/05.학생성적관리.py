'''
2023.06.14
202395005 김대영
학생 이름과 점수를 입력받아 리스트에 저장하고
학생 점수의 총점과 평균을 출력하시오

# 알고리즘
    0. 학생 리스트를 생성
    1. 학생 수를 입력받기
        1.1. 학생 이름과 점수를 리스트에 저장
    2. 점수합계를 계산
    3. 리스트에 저장된 학생 정보를 출력
        3.3. 총점과 평균을 출력
'''
student=[]
sum=0

num=int(input("학생 수 입력 : "))

for i in range(num) :
    print("<",i+1,"번째 학생정보 입력 : ",">")

    name=input("학생 이름 입력 : ")
    score=int(input("%s학생의 점수 입력 : "%name))

    student.append([name,score])
    sum= sum + score

for impo in student :
    print("이름 :",impo[0],"점수 :",impo[1])

print("학생의 점수 합계 :",sum)
print("학생의 점수 평균 : {:.2f}".format(sum/num)) # :.2f는 소수 두번째 자리까지 출력  # :.3f는 소수 세번째 자리까지 출력
