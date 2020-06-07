import math

first = int(input())
second = int(input())

if second <= 1:
    print(round(math.log(first), 2))
else:
    print(round(math.log(first, second), 2))
