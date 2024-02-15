import numpy as np
from sympy import symbols, solve

x, y, z = symbols('x, y, z')

# 1. a)

A = np.array([[-1, 2],
              [3, 1]])

B = np.array([[0, 1, 3],
              [2, -3, 5]])

C = A.dot(B)
print(C)

# 1. b)

D = np.array([[1, 3, 5],
              [0, -2, 1],
              [2, -1, 4]])

E = np.array([[1],
              [-3],
              [-1]])

# 1.c)

F = D.dot(E)
print(F)

G = np.array([[2, 0, 1],
              [1, -3, 4],
              [0, 1, 5]])

H = np.array([[3],
              [-5],
              [7]])

J = G.dot(H)
print(J)

# 1.d)

K = np.array([[1, -4, 2],
              [3, 0, -2],
              [2, 1, 0]])

L = np.array([[5, 1, -1],
              [-2, 1, 3],
              [0, 3, 4]])

M = K.dot(L)
print(M)

# Transpoosit ja determinantit

# Transpoosit tehtävä 1

AT = np.array([[4, -3],
               [9, 7],
               [0, -11]])

BT = np.array([[8, -3, 0, 7],
               [9, 12, -1, 1]])

print(AT)
print(BT)

# 1 a)

N = np.array([[5, -6],
              [8, 10]])

print(N)
print(np.linalg.det(N))

# 2 a)

P = np.array([[2, 3, 4],
              [-2, -1, 1],
              [5, 3, 2]])

print(P)
print(np.linalg.det(P))

# 2 a)

O = np.array([[3, 15, 7],
              [0, -4, 0],
              [3, 2, 3]])

print(O)
print(np.linalg.det(O))

# 1 Laske determinantti

Q = np.array([[-2, 0, 8, 5],
              [3, -1, 2, 1],
              [4, 7, 6, 2],
              [1, 0, 2, 3]])

print(Q)
print(np.linalg.det(Q))
