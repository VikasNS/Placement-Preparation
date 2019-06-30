import functools

def myFunc(x,y):
  return int(str(x)+str(y))-int(str(y)+str(x))

arr = [1, 34, 3, 98, 9, 76, 45, 4]

arr.sort(key = functools.cmp_to_key(myFunc),reverse=True)

for ele in arr:
  print(ele,end="")
