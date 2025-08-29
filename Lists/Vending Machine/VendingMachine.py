from tabulate import tabulate

ItemList = [
    ["1", "Coke", "50", "30"],
    ["2", "Sprite", "30", "30"],
    ["3", "Mountain Dew", "25", "30"],
    ["4", "Mango Juice", "20", "40"],
    ["5", "Lays Chips", "40", "35"],
    ["6", "Balaji Chips", "30", "35"],
    ["7", "Dairy Milk", "100", "10"],
    ["8", "5-Star", "60", "10"],
    ["9", "Kitkat", "80", "10"],
    ["10", "Gems", "60", "20"],
    ]

def AddDenomination():
    
    ValidNotes = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    AmountInserted = 0
    
    while True:
        Note = input("Enter note amount (1/2/5/10/20/50/100/200/500/2000): ")
        if Note == "":
            print("Note value cannot be empty!")
        elif int(Note) < 0:
            print("We do not accept negative denomination!")
        elif int(Note) not in ValidNotes:
            print("We only accept notes of 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000!")
        else:
            AmountInserted = AmountInserted + int(Note)
            Question = input("Do you wish to add more? (Y/N): ")
            if Question.lower() == "n":   
                break
        
    return AmountInserted
        
def ShowItems():
    print()
    print("------------- All Items -------------")
    print()
    print(tabulate(ItemList, headers=["Item id", "Item name", "Quantity", "Price"]))

def PurchaseItems(TotalAmount):
    
    PurchaseList = []
    TotalSpent = 0
    ProductName = ""
    TotalReceived = TotalAmount
    
    while TotalAmount != 0 or ProductName.lower() != "stop":
        
        ProductName = input("Enter the product name you want to purchase (or type STOP to finish): ")
        if ProductName == "":
            print("Product name cannot be empty!")
        elif ProductName.lower() == "stop":
            break
        else:
            ProductFlag = False
            for Item in ItemList:
                if Item[1].lower() == ProductName.lower():
                    ProductIndex = ItemList.index(Item)
                    ProductFlag = True
                    break
                    
            if ProductFlag == False:
                print("Product not found!")
            else:
                Price = int(ItemList[ProductIndex][3])
                Quantity = int(ItemList[ProductIndex][2])
                
                if Quantity == 0:
                    print("There is no", ItemList[ProductIndex][1], "left in stock.")
                elif TotalAmount < Price:
                    print(ItemList[ProductIndex][1], "costs Rs", Price, ". You have Rs", TotalAmount, ". You can’t afford that.")
                else:
                    ItemList[ProductIndex][2] = str(Quantity - 1)
                    TotalAmount = TotalAmount - Price
                    TotalSpent = TotalSpent + Price
                    PurchaseList.append([ItemList[ProductIndex][1], Price])
                    
                    print("You bought", ItemList[ProductIndex][1], "for Rs", Price, ". You have Rs", TotalAmount, "left.")
                    
    Change = TotalReceived - TotalSpent
    
    print()
    print("----- Final Receipt -----")
    print()
        
    for Purchase in PurchaseList:
        print(Purchase[0] + "\t\t\tRs " + str(Purchase[1]))
        
    print()
    print("Amount received:\tRs " + str(TotalReceived))
    print("Amount spent:\t\tRs " + str(TotalSpent))
    print("Change given:\t\tRs " + str(Change))
    print()
    print("Thank you for shopping!")


