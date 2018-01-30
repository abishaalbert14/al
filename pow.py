import math
n = int(input("enter n :"))
m = int(input("enter m :"))
i = 1
res =1
while i <= m:
    res *= n
    i+=1
    print (str(n) + '^' + str(m) + '=' + str(res))
    print(str(math.pow(n,m)))
