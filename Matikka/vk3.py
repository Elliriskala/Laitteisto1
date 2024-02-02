import numpy as np
from sympy import symbols, solve

# 1. Dokumentit-osassa on Matriisilaskentaa Pythonilla html-sivu.
# Laske edellinen tehtävä sen avulla.

A = np.array([[-1, 2], [3, -5]])
B = np.array([[2, 0], [-1, 4]])

print(A)
print(B)

# Määritä 2A + 3B ja A - B

print(2*A + 3*B)
print(A-B)

# 2. Dokumentissa käydään myös läpi yhtälöryhmien ratkaisemista numpyn avulla.
# Ratkaise sen avulla tämän tehtäväosa kolme ensimmäistä kertaustehtävää.

x, y, z = symbols('x, y, z')

result_a = solve([5*x + 3*y - 9,
                  2*x + y - 4], [x, y])

print(result_a)

result_b = solve([2*x + y + z - 6,
                  x + 3*y + z - 2,
                  2*x + y + 2*z - 9], [x, y, z])

print(result_b)

result_c = solve([x + y + 3*z + 1,
                  3*x + y + z - 5,
                  2*x + y + 2*z - 2], [x, y, z])

print(result_c)



