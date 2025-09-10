u = [1, 2, 3]
u_norm = (u[0]**2 + u[1]**2 + u[2]**2)**0.5
print(f"norm of u(before normalizing): {u_norm:.2f}")

u_ = []
u_.append(u[0] / u_norm)
u_.append(u[1] / u_norm)
u_.append(u[2] / u_norm)

u_norm_ = (u_[0]**2 + u_[1]**2 + u_[2]**2)**0.5
print(f"norm of u(after normalizing) : {u_norm_:.2f}")