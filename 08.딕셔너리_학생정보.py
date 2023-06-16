'''
2023.06.16
202395005 김대영
# 문제분석
    학생 정보를 사전에 저장하고 특정 학생의 정보를 입력하여 학생을 찾기(학번,이름 저장)
    사전에 저장 학번을 입력하면 학생을 찾아주는 시스템
    없다면 '없는 학생입니다' 출력

# 알고리즘
    1. 학생 정보를 저장할 사전 생성 - 빈 사전 생성
    2. 학생 정보를 입력 - 사전에 저장(무한 반복, z키를 누르면 종료)
    3. 학번으로 검색하여 학생 찾기(무한 반복, 학번이 빈칸이면 검색 종료)
'''
student={} # 빈 사전 생성

while True :

    student_num=input("학생 학번 입력(z는 프로그램 종료) : ")
    student['학번']=student_num

    if student_num=='z' :
       break

    student_name=input("학생 이름 입력(z는 프로그램 종료) : ")   
    student['이름']=student_name

    if student_name=='z' :
       break
   
while True :

    search=input("학번으로 학생 검색(빈칸 시 프로그램 종료) : ")
    if search == '':
        print("프로그램을 종료합니다.")
        break

    if search in student['학번'] :
        print("{}번 학생의 이름 : {}".format(search,student['이름']))

    




