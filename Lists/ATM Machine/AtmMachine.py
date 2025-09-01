# ATM Machine

DebitCardDetails = [
    ["Mahender Vohra", 3000000, 1973, "4614-2231-8693-1241"],
    ["Hargun Vohra", 450000, 2621, "7684-3921-4283-9837"],
    ["Aarav Mehta", 125000, 1345, "5532-7621-3982-7810"],
    ["Ishaan Khanna", 890000, 9023, "6712-8890-1123-4567"],
    ["Rehaan Kapoor", 275000, 4109, "4321-3345-6678-2233"],
    ["Vihaan Batra", 1320000, 8234, "8891-5643-2222-9001"],
    ["Kavya Sethi", 465000, 3456, "3333-1212-4545-6767"],
    ["Anaya Sharma", 98000, 9988, "7878-2323-1212-5656"],
    ["Siya Malhotra", 325600, 7789, "9000-1111-2233-4444"],
    ["Aanya Joshi", 1500000, 6677, "5555-8888-9999-0000"]
]

def VerifyDebitCard():
    while True:
        DebitCard = input("Enter your debit card number(xxxx-xxxx-xxxx-xxxx): ")
        if DebitCard == "":
            print("Debit card cannot be blank!")
        else:
            break
        
    for Details in DebitCardDetails:
        if Details[3] == DebitCard:
            print()
            print("Welcome,", Details[0])
            print()
            print("Please select an option from the menu below:")
            return Details

    print("Debit Card not found!")
    return False

def Withdrawl(Details):
    while True:
        Withdrawl = int(input("Enter the amount you want to withdrawl (in Rs): "))
        if Withdrawl == "":
            print("Withdrawl cancelled!")
            break
        elif Withdrawl < 0:
            print("Withdrawl value cannot be negative!")
        elif Withdrawl > Details[1]:
            print("Insufficient balance!")
        else:
            NewBalance = Details[1] - Withdrawl
            Details[1] = NewBalance
            print("Withdrawl of Rs", Withdrawl, "successful. Remaining Balance: Rs", NewBalance)
            break
        
def Deposit(Details):
    while True:
        Deposit = int(input("Enter the amount you want to deposit (in Rs): "))
        if Deposit == "":
            print("Deposit cancelled!")
            break
        elif Deposit < 0:
            print("Deposit value cannot be negative!")
        else:
            NewDeposit = Details[1] + Deposit
            Details[1] = NewDeposit
            print("Deposit of Rs", Deposit, "successful. Your balance is", NewDeposit)
            break
        
def ShowAccountBalance(Details):
    AccountBalance = Details[1]
    
    print("Your current balance is Rs", AccountBalance)