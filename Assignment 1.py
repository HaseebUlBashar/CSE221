#Task 1 
n=int(input())
for i in range(n):
    x=int(input())
    if x%2==0:
        print(f"{x} is an Even number.")
    else:
        print(f"{x} is an Odd number.")
#Task 2
n=int(input())
store=["+","-","/","*"]
for i in range(n):
    line=input()
    a=line.split(" ")
    x=float(a[1])
    y=float(a[3])
    z=a[2]
    if z=="+":
        print(x+y)
    if z=="-":
        print(x-y)
    if z=="/":
        print(x/y)
    if z=="*":
        print(x*y)
 #Task 3
a=input()
b=input()
a=a.split(" ")
b=b.split(" ")
for i in range(int(a[0]),-1,-1):
    if i==0:
        print(b[i])
    elif(i<int(a[1])):
        print(b[i],end=" ")
#Task 4
T = int(input())
 
for _ in range(T):
   n= int(input())
   sum= (n*(n+1))//2
   print(sum)
#Task 5
a=int(input())
lst1=list(map(int,input().split(" ")))
n=len(lst1)
for i in range(n-1):
    flag=True
    for j in range(n-1-i):
        if lst1[j]>lst1[j+1]:
            flag=False
            lst1[j],lst1[j+1]=lst1[j+1],lst1[j]
    if flag==True:
        break
lst1=list(map(str,lst1))
print(" ".join(lst1))
#Task 6
num=int(input())
id=list(map(int,input().split(" ")))
marks=list(map(int,input().split(" ")))
swap=0
for i in range(num):
    max_idx=i
    for j in range(i+1,num,1):
        if marks[j]>marks[max_idx]:
            max_idx=j
        elif marks[j]==marks[max_idx]:
            if id[j]<id[max_idx]:
                max_idx=j
    if max_idx!=i:
        id[i],id[max_idx]=id[max_idx],id[i]
        marks[i],marks[max_idx]=marks[max_idx],marks[i]
        swap+=1
print("Minimum swaps:",swap)
for i in range(len(id)):
    print(f"ID: {id[i]} Mark: {marks[i]}")
    #Task 7
    def lex(a, b, idx1, idx2):
    return idx1 if a < b else idx2
 
def time(a, b, idx1, idx2):
 
    return idx2 if a < b else idx1
n=int(input())
train=[]
destination=[]
t=[]
for i in range(n):
    txt=input().split(" ")
    train.append(txt[0])
    destination.append(txt[len(txt)-3])
    t.append(txt[len(txt)-1])
for i in range(n):
    for j in range(n-1-i):
        if train[j]!=train[j+1]:
            idx=lex(train[j],train[j+1],j,j+1)
            if idx!=j:
                train[j],train[j+1]=train[j+1],train[j]
                destination[j],destination[j+1]=destination[j+1],destination[j]
                t[j],t[j+1]=t[j+1],t[j]
 
        else:
            if t[j+1]!=t[j]:
                 idx2=time(t[j],t[j+1],j,j+1)
                 if idx2!=j:
                    train[j],train[j+1]=train[j+1],train[j]
                    destination[j],destination[j+1]=destination[j+1],destination[j]
                    t[j],t[j+1]=t[j+1],t[j]
                
for i in range(n):
    print(f"{train[i]} will departure for {destination[i]} at {t[i]}")