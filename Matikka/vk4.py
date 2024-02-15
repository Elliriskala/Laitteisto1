import numpy as np
from sympy import symbols, solve

# tehtävä osa 2 tehtävä 1

x, y, z = symbols('x, y, z')

result_1a = solve([x - 2*y - 2*z,
                  -2*x + y - z + 3,
                  3*x + 2*y + z - 4], [x, y, z])

print(result_1a)

result_1b = solve([x + y - 1,
                  2*x + y - z - 1,
                  3*x + y - 2*z - 1], [x, y, z])

print(result_1b)

# tehtävä osa 2 tehtävä 2

result_2a = solve([2*x + 4*y - z - 11,
                  6*x - y - 3*z - 7,
                  4*x + 5*y - 2*z - 16], [x, y, z])

print(result_2a)

result_2b = solve([4*x + 2*y - 2*z,
                  2*x + y - z - 1,
                  3*x + y - 2*z - 1], [x, y, z])

print(result_2b)

# tehtävä osa 3 tehtävä 1


result_1A = solve([5*x + 3*y - 9,
                  2*x + y - 4], [x, y])

print(result_1A)

result_1B = solve([2*x + y + z - 6,
                  x + 3*y + z - 2,
                  2*x + y + 2*z - 9], [x, y, z])

print(result_1B)

result_1C = solve([x + y + 3*z + 1,
                  3*x + y + z - 5,
                  2*x + y + 2*z - 2], [x, y, z])

print(result_1C)


