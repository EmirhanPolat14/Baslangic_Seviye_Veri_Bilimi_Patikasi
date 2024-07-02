"""
x = 1

y = 1

z = 2

n = 3 

All permutations of [i, j, k] are:

[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]].

Print an array of the elements that do not sum to n = 3.
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())


a = [[i, j, k]  for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n ]

print(a)

