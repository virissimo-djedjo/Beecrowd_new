A, B, C = map(int, input().split())

maior = A

if(B > maior):
    maior = B
elif(C > maior):
    maior = C

print(f"{maior} eh o maior")