T = int(input().strip())

for _ in range(T):
    N,K = [int(ele) for ele in input().strip().split(" ")]
    arr = [int(ele) for ele in input().strip().split(" ")]
    arr.sort()
    dic = dict()
    startingLoc = 0
    endingLoc = 0
    count = 0
    flag = 0
    for i,ele in enumerate(arr):
        if(ele in dic):
            previous = ele
            dic[ele]=[dic[ele][0],dic[ele][1],dic[ele][2]+1]
        else:
            dic[ele]=[i,0,1]
            if(flag == 1):
                dic[arr[i-1]]=[dic[arr[i-1]][0],i-1,dic[arr[i-1]][2]]
        flag = 1
    dic[ele]=[dic[ele][0],i,dic[ele][2]]
    cost = 10000000
    for key,value in dic.items():
        if(value[2] == K):
            tempCost = 0
        elif(value[2] < K):
            noOfElements = K - value[2]
            if(value[0]-noOfElements < 0):
                left = arr[0:value[0]]
            else:
                left = arr[value[0]-noOfElements:value[0]]
            right = arr[value[1]+1:value[1]+1+noOfElements]
            temp = sorted([(key-ele)*3 for ele in left] + [(ele-key)*5 for ele in right])[:noOfElements]
            tempCost = sum(temp)
           
        elif(value[2] > K):
            tempCost = (value[2] - K) * 3
        
        if tempCost < cost:
            cost = tempCost
    print(cost)
    
