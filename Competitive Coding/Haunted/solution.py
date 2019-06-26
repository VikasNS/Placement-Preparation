N,M = [int(ele) for ele in input().strip().split(" ")]
days = [int(ele) for ele in input().strip().split(" ")]
 
dic = dict()
ci=0
cv=0
for day in days:
    if day in dic:
        dic[day]+=1
    else:
        dic[day]=1
    
    if(cv < dic[day]):
        cv = dic[day]
        ci = day
    elif(cv == dic[day]):
        if(ci < day):
            ci = day
    print(ci,cv)
        