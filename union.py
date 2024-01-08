def intersection(l1,l2):
    ans=[]
    for i in l1:
        if i in l2:
            ans.append(i)
    return ans


def union(l1,l2):
    #ans=[]
    ans=l1.copy()
    for i in l2:
        if i not in l1:
            ans.append(i)
    return ans

def diff(l1,l2):
    sol=[]
    for i in l1:
        if i not in l2:
            sol.append(i)
    return sol
        
n=int(input("Enter no in list 1 : "))
list1=[]
for i in range (n):
    item=int(input(f"Enter Item no {i+1} : "))
    list1.append(item)

n2=int(input("Enter no in list 2 : "))
list2=[]
for i in range (n2):
    item2=int(input(f"Enter Item no {i+1} in 2nd List : "))
    list2.append(item2)

print("list :1 ",list1)
print("List 2 : ",list2) 
print("intersection",intersection(list1,list2))   
print("union",union(list1,list2))   
print("Difference",diff(union(list1,list2),intersection(list1,list2)))  