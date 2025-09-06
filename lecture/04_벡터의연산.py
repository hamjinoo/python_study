# 변수의 할당, 연산 -> 벡터의 연산
# 벡터 : 

u1, u2, u3 = 1, 2, 3
v1, v2, v3 = 10, 20, 30

print(f"u: ({u1, u2, u3})")
print(f"v: ({v1, v2, v3})")

sum1 = u1 + v1
sum2 = u2 + v2
sum3 = u3 + v3
print(f"u + v: ({sum1}, {sum2}, {sum3})")

sub1 = u1 - v1
sub2 = u2 - v2
sub3 = u3 - v3
print(f"u - v: ({sub1}, {sub2}, {sub3})")

# Scalar Multiplication
k = 10
u1, u2, u3 = 1, 2, 3

print(f" k: {k}")
print(f"u: ({u1} , {u2}, {u3})")

mul1 = k * u1
mul2 = k * u2
mul3 = k * u3

print(f"mul : ({mul1}, {mul2}, {mul3})")

# Norm
u1, u2, u3 = 1, 2, 3
print(u1, u2, u3)

u_norm = (u1**2 + u2**2 + u3**2)**0.5
print(f"norm of u: {u_norm:.2f}")


#
u1, u2, u3 = 1, 2, 3
u_norm = (u1**2 + u2**2 + u3**2)**0.5

u1 /= u_norm
u2 /= u_norm
u3 /= u_norm
u_norm = (u1**2 + u2**2 + u3**2)**0.5
print(u_norm)

# Dot Project
u1, u2, u3 = 1, 2, 3
v1, v2, v3 = 10, 20, 30

dot_prod = u1*v1 + u2*v2 + u3*v3
print(f"dot product : {dot_prod}")

# Euclidean Distance
u1, u2, u3 = 1, 2, 3
v1, v2, v3 = 10, 20, 30

e_dist = ((u1 - v1)**2 + (u2 - v2)**2 + (u3 - v3)**0.5)
print(f"Euclidean distance: {e_dist:.4f}")