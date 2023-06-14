'''
2023.06.14
202395005 김대영
리스트의 값 10개중에서 10보다 큰 수를 출력하시오
numbers 변수에 숫자 아무거나 입력
'''
numbers=[2,5,11,14,39,54,64,77,79,99]

print("리스트 값 중 큰수 출력 - 반복문 사용")
for i in numbers :
    if i >= 10 :
        print(i, end=' ')

print('\n')

print("리스트 값 중 큰수 출력 - continue 사용")
for i in numbers :
    if i < 10 :
        continue
    
    else :
        print(i, end=' ')

print('\n')

'''
1에서 30사이의 수 중에서 7의 배수를 출력 continue 사용 
'''
number=range(1,31)

for i in number :
    if i % 7 != 0 :
        continue

    else :
        print(i, end=' ')
