def binary_search(list,key):
    low=0
    high=n-1
    while(low<=high) :
        mid=(high+low)//2
        if list[mid]==key:
            print("p")
        elif list[mid]>=key:
            high=mid-1
        else:
            low=mid+1
    else:
        print("A")
list=[]
n=int(input("Enter Total No of Student who attend lecture : "))
for i in range (n):
    st=int(input("Enter roll no of Students : "))
    list.append(st)    
list.sort()

key=int(input("Enter Key: "))
binary_search(list,key)                    