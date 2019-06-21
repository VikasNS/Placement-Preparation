T = int(input().strip())

def isPrime(N):
    for i in range(3,int(N/2)+2,2):
        if(N%i == 0 and N!=i):
            return False
    return True


myDic = dict()
for _ in range(T):
    found = 0
    N = int(input().strip())
    if(N%2 == 0):
        print(N-2)
    else:
        for i in range(3,int(N/2)+2,2):
            if(N%i == 0):
                if i in myDic:
                    res = myDic[i]
                else:
                    res = isPrime(i)
                    myDic[i] = res
                if(res):
                    found = 1
                    print(N-i)
                    break
        if(not found):
                print(0)
    