                #"""MockTest from scratch: Banking Program Test 7th ATTEMPT. :)"""
# balance, deposit , withdraw ,fund_tranfer, bank_number and ErrorHandling
#using define function

def check_balance(balance):
    print(f"Your available balance is ${balance}")
    
def deposit(balance):
    try:
        amount = int(input("please input how many do you want to deposit: "))
        
        if amount <= 0:
            print("please input the value greater than 0")
            return 0
        else:
            print(f"you has been succeed deposit ${amount}")
            return amount
    except ValueError:
        print("please enter numeric value")
        return 0
    
def withdraw(balance):
    try:
        amount = int(input("please input the amount that you want to withdraw: "))
        
        if amount > balance:
            print("innuficient balance")
            return 0
        elif amount <= 0:
            print("please input the amount greather than 0 ")
            return 0
        else:
            print(f"you has been succeed withdraw ${amount}")
            return amount
    except ValueError:
        print("please enter numeric value")
        return 0
        
def fund_tranfer(balance):
    try:
        amount = int(input("please input the amount you want to tranfer: "))
        
        if amount >  balance:
            print("innuficient fund")
            return 0
        elif amount <= 0:
            print("please input the value greather than 0")
            return 0
        else:
            while True:
                bank_number = input("please enter the 7-digit  bank number destination: ")
                
                if bank_number.isdigit() and len(bank_number) == 7:
                    print(f"you has been succeed tranfer ${amount} to this bank number {bank_number}")
                    return amount
                else:
                    print("please enter the valid bank number")
                    return 0
    except ValueError:
        print("please enter numeric value")
        return 0
            
        
def main():
    balance = 0
    run = True
    
    while run:
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Fund Tranfer")
        print("5. Exit")
        
        choice = input("please select the number transaction do you want to execute from 1, 2, 3, 4 or 5: ")

        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            balance -= fund_tranfer(balance)
        elif choice == '5':
            run = False
        else:
            print("please only select from 1,2,3,4 or 5 !")
    print("Thank You for your today transaction! ")
    
if __name__ == '__main__':
    main()