while True:
    print("Bill Split Calculator")

    totalBill = float(input("What was the bill?"))
    totalPeople = int(input("How many people? "))

    total = totalBill / totalPeople
    #rounding the string -total- by 2 decimal points
    total = round(total, 2)
    print("You need to pay each:", total)
    exitProgram = input("Do you want to exit, yes or no?")
    if exitProgram == "yes":
        break
print("Thanks for using my program!")
            


