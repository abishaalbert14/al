lower=int(input("Enter the lower limit of the range:"))
upper=int(input("Enter the upper limit of the range:"))
for i in range(lower,upper+1):
    if(i%2!= 0):
        print(i)

