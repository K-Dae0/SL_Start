'''
2023.06.16
202395005 김대영
사전 : 키와 값으로 이루어져 있음
키는 중복 x
'''
list1=[[1,'하나'],[2,'둘'],[3,'셋']] # 리스트
dict1=dict(list1) # 리스트를 사전으로 반환

print("리스트 :",list1)
print("사전 :",dict1)

dict2={'제목' : '어벤져스','장르' : '히어로 무비'}

print("사전 :",dict2)

print('\n')
# 특정키를 출력
# 키 값은 리스트의 대괄호를 사용 # dict{'제목'} 시 오류발생
print("영화 제목 :",dict2['제목'])
print("영화 장르 :",dict2['장르'])

print('\n')

dict2['감독']=['안소니 루소','조 루소']
print("영화 감독 :",dict2['감독'])

print('\n')

dict2['출연진']=['아이언맨','토르','닥터스트레인지','헐크']
print("영화 출연진 :",dict2['출연진'])

print('\n')

# 장르 변경
print("<","장르 변경",">")
dict2['장르']='SF'
print("영화 장르 :",dict2)

print('\n')

# 출연진 추가
print("<","출연진 추가",">")
dict2['출연진'][1]='타노스'
print("영화 출연진 :",dict2['출연진'])
print("특별 캐스팅 :",dict2['출연진'][1])

print('\n')

# 출연진 삭제
print("<","출연진 삭제",">")
del dict2['출연진']
print("영화 출연진 :",dict2)

print('\n')

student={} # 빈 사전 생성
print("학생 추가 전 : ",student)

student['학과']='컴퓨터공학부'
student['학번']='202395005'
student['이름']='김대영'

print("학생 추가 후 :",student)

print('\n')

# 딕셔너리에 키가 있는지 확인
key=input('찾고 싶은 키 입력 : ')
if key in student :
    print(student[key])

else :
    print("존재하지 않는 키 입니다.")