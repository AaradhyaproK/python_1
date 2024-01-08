def intersection(l1,l2):
    ans=[]
    for i in l1:
        if i in l2:
            ans.append(i)
    return ans        

def union(l1,l2):
    ans1=[]
    ans1=l1.copy()
    for i in l2:
        if i not in l1:
            ans1.append(i)
    return ans1        
            
def diff(l1,l2):
    ans2=[]
    for i in l1:
        if i not in l2:
            ans2.append(i)
    return ans2

nc=int(input("Enter no of players in cricket : "))
C=[]
for i in range (nc):
    pn=int(input("Enter jersy no of player : "))
    C.append(pn)
print("Player Jersy No who play cricket : ",C)  

nf=int(input("Enter no of players in football : "))
F=[]
for i in range (nf):
    pf=int(input("Enter jersy no of player : "))
    F.append(pf)
print("Player Jersy No who play Football : ",C)

nh=int(input("Enter no of players in hockey : "))
H=[]

for i in range (nh):
    ph=int(input("Enter jersy no of player : "))
    H.append(ph)
print("Player Jersy No who play hockey : ",H)

print("the player who play only cricket : ",diff(diff(C,H),F))
print("play cri batmin ",union(C,H))
