import VendingMachine as VM 

def main():
    Flag = True 

    while Flag:
        print()
        print("------------ Vending Machine ------------")
        print()

        TotalAmount = 0
        while TotalAmount == 0:
            TotalAmount = VM.AddDenomination()
            print("Amount inserted: Rs", TotalAmount)

        VM.ShowItems()
        print()
        VM.PurchaseItems(TotalAmount)

        while True:
            Question = input("\n(N)ext customer, or (Q)uit? ")
            if Question.lower() == 'q':
                Flag = False  
                break  
            elif Question.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'N' or 'Q'.")

            
if __name__ == "__main__":
    main()