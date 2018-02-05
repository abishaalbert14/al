def rotate(lst, x):
    return [lst[-x:] + lst[:-x]]
l=list(map(int,input().split(' ')))    
p=int(input())            
print(''.join(str(x) for x in rotate(l,p)))   
