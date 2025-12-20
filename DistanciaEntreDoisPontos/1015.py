import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
'''
x1 = p1[0]
y1 = p1[1]

x2 = p2[0]
y2 = p2[1]

'''
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"{distancia:.4f}")