import numpy as np

# 1. Määrittele ja esitä 5-alkioinen kokonaislukutaulukko numpyn avulla.
# luvut voivat olla satunnaisia.

x = np.random.randint(1, 50, size=5)
print(x)

# 2. Määrittele vektorit numpy taulukon avulla.

# a) u = 2i + 3j, v = 4i - 7j

u = np.array([2, 3])
v = np.array([4,-7])

print("Vektori u =", u)
print("Vektori v =", v)

# b) uu = i + j + k, vv = 3i -3j + 2k

uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

print("Vektori uu =", uu)
print("Vektori vv =", vv)

# 3. Laske kunkin vektorin normi.

u_normi = np.linalg.norm(u)
result_u = np.round(u_normi, 2)
print("Vektorin u normi:", result_u)

v_normi = np.linalg.norm(v)
result_v = np.round(v_normi, 2)
print("Vektorin v normi:",result_v)

uu_normi = np.linalg.norm(uu)
result_uu = np.round(uu_normi, 2)
print("Vektorin uu normi:",result_uu)

vv_normi = np.linalg.norm(vv)
result_vv = np.round(vv_normi, 2)
print("Vektorin vv normi:", result_vv)


