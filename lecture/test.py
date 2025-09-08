# 변수에 각각 값을 대입시키면 슈퍼에서 산 물건을 각각 들고 다니는 것과 같다.
# 그래서 관리를 편리하게 장바구니가 필요한데 그게 '리스트'이다.

# 11. 파이썬 리스트트
# 리스트 넣기
score = [80, 100, 90]
print(f"{score = }")

u = [1, 2, 3]
v = [10, 20, 30]
print(f"{u = }")
print(f"{v = }")


# 리스트 원소 출력하기
score = [10, 20, 30]
print(score[0])
print(score[1])
print(score[2])

# 합 구하기
scores = [80, 100, 90]
score_sum = scores[0] + scores[1] + scores[2]
print(f"{score_sum = }")

score_sum2 = sum(scores)
print(f"{score_sum2 = }")


# Vector Norm
u = [1, 2, 3]
u_norm = (u[0]**2 + u[1]**2 + u[2]**2)**0.5
print(f"u_norm : {u_norm:.2f}")


# Dot Product
u = [1, 2, 3]
v = [10, 20, 30]

dot_prod = u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
print(f"dot Product: {dot_prod}")


# Squared Error
preds = [10, 20, 30]
labels = [5, 10, 15]

squared_error1 = (preds[0] - labels[0])**2
squared_error2 = (preds[1] - labels[1])**2
squared_error3 = (preds[2] - labels[2])**2

print(f"{squared_error1}")
print(f"{squared_error2}")
print(f"{squared_error3}")

# ---
# 12. 리스트와 len함수
u = [1, 2, 3]
v = [10, 20, 30]

e_dist = ((u[0] - v[0])**2 + (u[1] - v[1])**2 + (u[2] - v[2])**2)**0.5
print(f"Euclidean distance : {e_dist:.4f}")

test_list = []
print(len(test_list))

test_list2 = [1]
print(len(test_list2))

test_list3 = [1, 2]
print(len(test_list3))

test_list4 = [1, 2, 3]
print(len(test_list4))

score = [10, 20, 30]
score_mean = sum(score) / len(score)
print(f"{score_mean = }")

scores = [10, 20, 30]
score_mean = sum(scores) / len(scores)
score_squared_diff = [(scores[0] - score_mean)**2, 
                      (scores[1] - score_mean)**2,
                      (scores[2] - score_mean)**2]
score_var = sum(score_squared_diff) / len(score_squared_diff)
print(f"{score_var}")