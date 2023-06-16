'''
2023.06.16
202395005 김대영
'''
with open('impo.txt','r') as file :
    for line in file :
        (name,weight,height)=line.strip().split(",")
        
        if (not name) or (not weight) or (not height) :
            continue

    # 비만도 계산하기
        bmi=int(weight) / ((int(height) / 100) ** 2)

        if bmi >= 25 :
            result= "과체중"

        elif bmi >= 18.5 :
            result= "정상체중"

        else :
            result= "저체중"

        print("\n".join(["이름 : {}", "몸무게 : {}", "키 : {}", "bmi : {:.2f}", "결과 : {}"]).format(name,weight,height,bmi,result))
        print("\n")
