import math
square = math.pi * 6.5 ** 2
a, b = map(int, input().split())
if a * b > square:
    print('нет')
else:
    print('да')