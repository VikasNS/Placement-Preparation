D = int(input().strip())
X = 0
Y = 0
MX = 0
MY = 0
for _ in range(D):
    X = 0
    for e in input().strip():
        if(e == 'C'):
            X+=1
            Y+=1
        else:
            if(MX < X):
                MX = X
            if(MY < Y):
                MY = Y
            X = 0
            Y = 0
    if(MX < X):
        MX = X
    if(MY < Y):
        MY = Y
            
if(MX < X):
    MX = X
if(MY < Y):
    MY = Y
print(MX,MY)