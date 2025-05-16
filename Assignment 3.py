count = 0 
 
def merge(a, b):
    global count  
    i = 0
    j = 0
    result = []
 
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:  
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            count += len(a) - i  
            j += 1
 
 
    while i < len(a):
        result.append(a[i])
        i += 1
    
    while j < len(b):
        result.append(b[j])
        j += 1
 
    return result  
 
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid]) 
        a2 = mergeSort(arr[mid:])  
        return merge(a1, a2)
 
 
a = int(input()) 
b = list(map(int, input().split())) 
 
ans = mergeSort(b)  
print(count)
print(" ".join(map(str, ans)))
#Task 2

def max_pair(arr, l, r):
    if l==r:
        return float('-inf'), arr[l], arr[l] ** 2 
    else:
        mid = (l + r) // 2
        left_max, left_i, left_sqj = max_pair(arr,l,mid)
        right_max, right_i, right_sqj = max_pair(arr,mid+1,r)
        cross_max = left_i + right_sqj
        return max(left_max, right_max, cross_max), max(left_i, right_i), max(left_sqj, right_sqj)
 
n = int(input()) 
arr = list(map(int, input().split()))
 
 
result,x,y= max_pair(arr, 0, n - 1)
 
print(result)