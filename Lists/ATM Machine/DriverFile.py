import AtmMachine as AM

def main():
    print()
    print("----------------- ATM Machine -----------------")
    print()
    while True:
        UserDetails = AM.VerifyDebitCard()
        if UserDetails:
            break
        
    while True:
        print("1. Withdrawl")
        print("2. Deposit")
        print("3. Check current balance")
        print("4. Exit")
        Choice = int(input("Enter your choice (1 to 4): "))
        if Choice == 1:
            AM.Withdrawl(UserDetails)
        elif Choice == 2:
            AM.Deposit(UserDetails)
        elif Choice == 3:
            AM.ShowAccountBalance(UserDetails)
        elif Choice == 4:
            print("Exiting! Thank you!")
            break
        
if __name__ == "__main__":
    main()