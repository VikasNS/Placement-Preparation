copies, originals = [int(ele) for ele in input().strip().split(" ")]

def recFun(copies,originals,currC,currO,dic):
    if((currC,currO) in dic):
        return dic[(currC,currO)]
    if(currC>copies or currO>originals):
        return False
    elif(currC==copies and currO==originals):
        return True
    else:
        if(currO == originals):
            return recFun(copies,originals,currC+2,currO,dic)
        else:
            res1 = recFun(copies,originals,currC+1,currO+1,dic)
            res2 = recFun(copies,originals,currC+2,currO,dic)
            dic[(currC,currO)] = (res1 or res2)
            return (res1 or res2)

dic = dict()
if(recFun(copies,originals,0,1,dic)):
    print("Yes")
else:
    print("No")