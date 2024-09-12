a = [1,2,3]
b = a
a[1] = 4

print(a)
print(b)

from copy import copy
a = [1,2,3]
b = copy(a)
a[1] = 4
print(a)
print(b)

