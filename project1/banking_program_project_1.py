# PROJECT#1 Python Banking Program V1.3

import datetime #this is import default python module

def validate_positive_number(imput_prompt): #this is function
    while True:
        try:
            value = float(input(imput_prompt))
            if value >= 50:
                return value
            else:
                print("Invalid Input. Please enter a number greater than 50 !")
        except ValueError:
            print("Invalid Input, please enter a numeric value !")
                     
def show_balance(balance):
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"Your Balance is ${balance:.2f}")

def show_success_message(message):
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    print(message)
    print("$$$$$$$$$$$$$$$$$$$$$$$")

def deposit(balance, transaction_history):
    
        amount = float(validate_positive_number("Please enter an amount to be Deposited: "))
    
        if amount < 0:
            print("$$$$$$$$$$$$$$$$$$$$$$$")
            print("Sorry, please enter the valid amount :)")
            return 0
        else:
            show_success_message(f"Deposit of ${amount:.2f} succeeded !")
            log_transaction(transaction_history, "Deposit", amount)
            return amount
    

def withdraw(balance, transaction_history):
    
        amounts = float(validate_positive_number("Please enter an amount to be withdrawn: "))

        if amounts > balance:
            print("Insufficient funds")
            return 0
        elif amounts < 50:
            print("Sorry, amount must be greater than 50 :) ")
            return 0
        else:
            show_success_message(f"Withdrawal of ${amounts:.2f} succeeded !")
            log_transaction(transaction_history, "Withdrawal", amounts)
            return amounts
   
    
def fund_tranfer(balance, transaction_history):
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    
    amounts = float(validate_positive_number("Please enter an amount to Tranfer: "))  
        
    if amounts > balance:
        print('Insufficient funds')
        return 0
    else:
        while True: 
            bank_number = input("Please Enter the valid Account number to tranfer: ")
            if bank_number.isdigit() and len(bank_number) == 10:
                print(f"Tranfer of {amounts} to bank number {bank_number} is succed !")
                log_transaction(transaction_history,"Transfer", amounts, recipient=bank_number)
                return amounts
            else:
                print("Invalid bank number. Please enter a valid 10-digit numeric bank number.")
                return 0
    
def log_transaction(transaction_history, transaction_type, amount, recipient=None):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction= {
        "type": transaction_type,
        "amount": amount,
        "recipient": recipient if recipient else "N/A",
        "timestamp": timestamp  
        
    }
    transaction_history.append(transaction)

def get_transaction_history(transaction_history):
    """Displays the transaction history""" 
    if not transaction_history:
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        print("No Transaction yet !")
        return 
    print("\nTransaction History:")
    print(f"{'Type':<15}{'Amount':<10}{'Recipient':<15}{'TimeStamp':<20}")
    print("-"* 60)
    for transaction in transaction_history:
        print(f"{transaction['type']:<15}{transaction['amount']:<10.2f}{transaction['recipient']:<15}{transaction['timestamp']:<20}")
    print("$$$$$$$$$$$$$$$$$$$$$$$")


    
def main():    
    balance = 0
    transaction_history = [] #Initialize an empty transaction history
    is_running = True

    while is_running:
        print("    Banking Program    ")
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        print("1.Show Balance")
        print("2.Deposit")
        print("3. Withdraw")
        print("4. Fund Tranfer")
        print("5. Transaction History")
        print("6.Exit")
        print("$$$$$$$$$$$$$$$$$$$$$$$")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1': #show balance
            show_balance(balance)
        elif choice == '2': #input deposit
            balance += deposit(balance, transaction_history)
        elif choice == '3': #input withdraw
            balance -= withdraw(balance,transaction_history)
        elif choice == '4': #input fund_tranfer
            transferred_amount = fund_tranfer(balance,transaction_history)
            if transferred_amount > 0:
                balance -= transferred_amount
        elif choice == '5':
            get_transaction_history(transaction_history)
        elif choice == '6':
            is_running = False
        else:
            print("$$$$$$$$$$$$$$$$$$$$$$$")
            print("Invalid choice. Please enter a number between 1 and 6")
            print("$$$$$$$$$$$$$$$$$$$$$$$")
    
    print("$$$$$$$$$$$$$$$$$$$$$$$")        
    print("Thank You! Have a nice day, sir!")
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    
if __name__ == '__main__': #
    main()