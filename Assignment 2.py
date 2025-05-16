#Task 1
n,s=(input().split(" "))
lst=list(map(int,input().split(" ")))
i=0
j=int(n)-1
while i<j:
    sum=lst[i]+lst[j]
    if sum==int(s):
        print(f"{i+1} {j+1}")
        break
    elif sum>int(s):
        j=j-1
    else:
        i+=1
if i>=j:
    print("-1")
#Task2:
n=int(input())
lst1=list(map(int,input().split(" ")))
m=int(input())
lst2=list(map(int,input().split(" ")))
i=0
j=0
merge=[]
while i<len(lst1) and j<len(lst2):
    if lst1[i]<=lst2[j]:
        merge.append(str(lst1[i]))
        i+=1
    else:
        merge.append(str(lst2[j]))
        j+=1
if i<len(lst1):
    while i<len(lst1):
        merge.append(str(lst1[i]))
        i+=1
elif j<len(lst2):
    while j<len(lst2):
        merge.append(str(lst2[j]))
        j+=1
print(" ".join(merge))
#task 3
n,k=input().split(" ")
lst1=list(map(int,input().split(" ")))
k=int(k)
n=int(n)
max_length=-float("inf")
sum=0
length=0
j=0
for i in range(n):
    sum+=lst1[i]
    length+=1
    if sum>k:
        while sum>k:
            sum=sum-lst1[j]
            j+=1
            length-=1
           
    if length>max_length:
        max_length=length
 
print(max_length)
#Task 4
def search(x):  
    l=0
    r=len(x)-1  
    while l<=r:
        mid=(l+r)//2
        if l==r and x[mid]=="1":
            return mid+1
        elif x[mid]=="1":
            r=mid
        elif x[mid]=="0":
            l=mid+1
    return -1
 
n=int(input())
for i in range(n):
    a=input()
    print(search(a))
#Task 5
import bisect
n,q=list(map(int,input().split(" ")))
lst1=list(map(int,input().split(" ")))
for i in range(q):
    p,q=list(map(int,input().split(" ")))
    x=bisect.bisect_left(lst1,p)
    y=bisect.bisect_right(lst1,q)
    print(y-x)
    
