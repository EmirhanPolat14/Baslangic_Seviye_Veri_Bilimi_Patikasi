a, b = map(int,input().split(" "))
def pol(a, b):
    top = 0
    for i in range(1, b+1):
        top += a ** i
    if b == top:
        return True
    
print(pol(a,b))