def bubble_sort(A):
     for j in range (n):
          for i in range (n-1):
               if A[i]>A[i+1]:
                    A[i],A[i+1]=A[i+1],A[i]
     return j               

def selection_sort(A):
     for i in range (n-1):
          min_index =i
          for j in range(i,n):
             if A[min_index]>A[j]:
               min_index=j
               A[i],A[min_index]=A[min_index],A[i]
          print(A)
     print("Selection Sort Result",A)

n=int(input("Enter How many no in list : "))
A=[]
for i in range (n):
        ele=int(input(f"Enter elemrnt no {i+1} :"))  
        A.append(ele)
print ("Before Sorting List : ",A)
bubble_sort(A)
selection_sort(A)

        

