#
# Created on Mon Jan 26 2026
#
# Copyright (c) 2026 Your Company
#
#Lesson 10: Comparison and logit operators - Các toán tử so sánh và logit

print('Comparison operator')
x = int(input('X: '))
y = int(input('Y: '))

print('{0} < {1}: {2}'.format(x, y, x<y))
print('{0} > {1}: {2}'.format(x, y, x>y))
print('{0} == {1}: {2}'.format(x, y, x==y))
print('{0} <= {1}: {2}'.format(x, y, x<=y))
print('{0} >= {1}: {2}'.format(x, y, x>=y))

print('Logit operator')
z = int(input('Z: '))
print('{0} < {1} and {2} > {3}: {4}'.format(x, y, y, z, (x<y) and (y>z)))
print('{0} > {1} or {2} < {3}: {4}'.format(x, y, y, z, x>y or y<z))
print('not({0} < {1}): {2}'.format(x, y, not(x<y)))