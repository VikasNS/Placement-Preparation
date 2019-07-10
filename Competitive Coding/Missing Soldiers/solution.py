B = int(input().strip())
x,y,d = [int(ele) for ele in input().strip().split(" ")]
xmin = x
xmax = x + d
s = d + 1
for _ in range(B-1):
    x,y,d = [int(ele) for ele in input().strip().split(" ")]
    if(d == 1 and ( x ==  xmin or x == xmax)):
        pass
    elif(x >= xmin and x+d <= xmax):
        pass
    elif(x < xmin and (x+d<=xmax and x+d>=xmin)):
        s = s + xmin - x 
        xmin = x
    elif(x+d>xmax and (x>=xmin and x<=xmax)):
        s = s + (x+d) - xmax 
        xmax = x + d
    elif(x<xmin and x+d>xmax):
        s = s + (xmin - x) + (x+d - xmax)  
        xmin = x
        xmax = x+d
    else:
        s= s + d + 1
        if(x+d < xmin):
            xmin = x
        elif(x > xmax):
            xmax = x+d
print(s)
