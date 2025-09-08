
# 연산자
num1, num2 = 10, 3
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 ** num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2) # 나머지

# 연산 결과 할당하기
sum_ = num1 + num2
sub = num1 + num2
mul = num1 * num2
pow_ = num1 ** num2
div = num1 / num2
qutient = num1 // num2
remainder = num1 % num2

# 자기 자신에 연산하기
score = 10
score = score + 10 # == score += 10
score = score - 10 # == score -= 10
score = score * 3 # == score *= 3
score = score / 3 # == score /= 3

# 합 구하기
score1, score2, score3 = 10, 20, 30
score_sum = score1 + score2 + score3
print(f"{score_sum}")

# 평균 구하기
score1, score2, score3 = 10, 20, 30
n_student = 3
score_mean = (score1 + score2 + score3) / 3
print(f"{score_mean}")

# 상수가 더해진 평균 구하기
score1, score2, score3 = 10, 20, 30
n_students = 3
base_score = 10
score_mean = (score1 + score2 + score3) / n_students
print(f"{score_mean = }")
score1 += base_score
score2 += base_score
score3 += base_score
score_mean = (score1 + score2 + score3) / n_students
print(f"{score_mean = }")

# 편차의 제곱
  # 편차란 각각의 자료값에서 평균값을 뺀 값
score1, score2, score3 = 10, 20, 30
n_students = 3

score_mean = (score1 + score2 + score3) / n_students

squared_diff1 = (score1 - score_mean)**2
squared_diff2 = (score2 - score_mean)**2
squared_diff3 = (score3 - score_mean)**2
print(f"{squared_diff1 = } / {squared_diff2 = } / {squared_diff3 = }")

# 분산 구하기(정의) : 데이터가 평균을 기준으로 얼마나 흩어져 있는지를 나타내는 값
# > “각 데이터 – 평균 → 각각 제곱 → 다 더함(Σ) → 1/n 나눔” = 분산
score1, score2, score3 = 10, 20, 30
n_students = 3
score_mean = (score1 + score2 + score3) / n_students
squared_diff1 = (score1 - score_mean)**2
squared_diff2 = (score2 - score_mean)**2
squared_diff3 = (score3 - score_mean)**2

score_var = (squared_diff1 + squared_diff2 + squared_diff3) / n_students
print(f"{score_var}")

# 분산 구하기(제평평제 - 제곱의 평균 / 평균의 제곱)
