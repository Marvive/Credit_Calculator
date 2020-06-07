import math

angle = int(input())

cotangent = math.cos(math.radians(angle)) / math.sin(math.radians(angle))
print(round(cotangent, 10))
