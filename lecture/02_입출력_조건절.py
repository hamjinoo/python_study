# 여러 변수 선언
name = "hong"
x, y = 7, 3
x = y = 10 # 오른쪽부터 삽입



# int
print(1 + 2) # 3
# float
print(1 + 1.5) # 2.5
# str
print("Hello" + "Python!")



# 원시 자료형
score = 2030
print(score) # 2030

score = float(score) # 2030.0

is_correct = True

teacher_name = "hong jinwab"
print(teacher_name[0]) # h
print(teacher_name[-2]) # a
print(teacher_name[5:9]) # jinw 인덱스 5부터 9 전까지 (즉, 5,6,7,8)
print(teacher_name[5:]) # jinwab 인덱스 5부터 끝까지
print(teacher_name[:5]) # hong  처음부터 인덱스 5 전까지 (즉, 0,1,2,3,4) (공백 포함)
print(teacher_name[::2]) # hn iwb 처음부터 끝까지 2칸씩 건너뛰면서
print(teacher_name[::-1]) # bawnij gnoh 전체 역순
print(teacher_name[::-2]) # bwi nh 끝에서 두 칸씩 거꾸로 (시작은 무조건 -1부터)
print(len(teacher_name)) # 11



# 자료형 타입 에러
print("Hello" + 1) # TypeError: can only concatenate str (not "int") to str
print("Hello" + str(1)) # Hello1



# 수학 연산자
print(3**3) # 27
print(60 % 13) # 8



# f-string 
name = "Hong"
age = 30
print("Hello, %s." % name)
print("Hello, %s, I am %s years old." % (name, age))
print("Hello, {}. I am {} years old.".format(name, age))
print("Hello, {1}. I am {0} years old.".format(age,name))
# # Python 2.6
person = {"name": "Hong", "age": 30}
print("Hello, {name}. I am {age}." .format(name=person["name"], age=person["age"]))
print("Hello, {name}. I am {age}.".format(**person))
# # Python 3.6
print(f"Hello, {name}. I am {age} years old.")
print(F"Hello, {name}. I am {age} years old.")
print(f"{name.lower()} is cool.")
