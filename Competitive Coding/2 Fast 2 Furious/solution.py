N = int(input().strip())

X = [int(ele) for ele in input().strip().split(" ")]
Y = [int(ele) for ele in input().strip().split(" ")]

XMax = 0
YMax = 0
for i in range(len(X)-1):
    if(abs(X[i+1]-X[i]) > XMax):
        XMax = abs(X[i+1]-X[i])
    
    if(abs(Y[i+1]-Y[i]) > YMax):
        YMax = abs(Y[i+1]-Y[i])
        
if(XMax > YMax):
    print("Dom")
    print(XMax)
elif(XMax < YMax):
    print("Brian")
    print(YMax)
else:
    print("Tie")
              