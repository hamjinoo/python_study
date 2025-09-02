# 1. 변수 타입
x, y = 7, 3
print(x + y, x / y)

# 2. 문자열
h = "Hello Python"
print(h.lower(), h.upper(), h.split(","))
print("pythin" in h.lower())

# 3. 리스트/슬라이싱
nums = [1, 2, 3, 4, 5]
print(nums[:3], nums[-2:])
nums.append(6); print(nums)

# 4. 조건문
score = 81
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(grade)

# 5. 반복문
total = 0
for n in range(1, 6): # 1~5
    total += n
print(total)

# 6. 함수
def greet(name: str) -> str:
    return f"Hi {name}!"
print(greet("kkong"))








