def participation(arr,high,low):
    p=arr[low]
    i=low+1
    j=high
    while True:
        while i<=j and arr[i]<=p:
            i+=1
        while i<=j and arr[j]>=p:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quick_sort(arr,low,high):
   if low<high: 
    pivot=participation(arr,high,low)
    quick_sort(arr,pivot+1,high)
    quick_sort(arr,low,pivot-1)                


                 
n=int(input("Enter Size : "))
arr= []
for i in range(n):
    ele=int(input(f"Enter element no {i+1} array : "))
    arr.append(ele)
print("Unsorted array ",arr)
quick_sort(arr,0,n-1)
print("sorted array : ",arr)




