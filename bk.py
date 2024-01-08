bank_balance=0
def widraw(amt):
    global bank_balance
    if bank_balance>=amt:
        bank_balance -= amt 
        print("Your bank balance : ",bank_balance)
    else :
        print("not sufficient ammount : ")
def deposit(amt):
    global bank_balance
    bank_balance += amt
    print("Your  bank balance : ") 

trans_log=input("Enter Trans Log : ")
opration=trans_log.split(", ")
for data in opration:
    log=data.split(" ")
    dec=log[0]
    amt=int(log[1])
    if dec=='D':
        deposit(amt)
    elif dec=='W':
        widraw(amt)
    else:
        print("wrong input")
print("Your Final Bank Balance",bank_balance)                      
