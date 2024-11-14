expenses=[]
expenses1={'amount':'51.00','category':'shirt'}
expenses.append(expenses1)
expenses2={'amount':'21.55','category':'groceries'}
expenses.append(expenses2)

def removeExpense():
    while True:
        listExpenses()
        print("What expenses would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove]
            break

        except:
            print("invalid input,please try again.")


def addExpense(amount,category):
    expense={'amount':amount,'category': category }
    expenses.append(expense)


def printMenu():
    print("1. Add a new Expense")
    print("2.Remove an Expense")
    print("3. List all Expenses")

def listExpenses():
    print("\nHere is the list of expenses..")
    print("--------------------")  
    counter=0
    for expense in expenses:
        print("#",counter," - ",expense['amount']," - ",expense['category'])    
        counter+= 1
    print("\n\n")

if __name__=="__main__":
   while True:
    printMenu()
    optionSelected = input("> ")   

    if(optionSelected=="1"):
        print("howw much was this expense?") 
        while True:
            try:
                amountToAdd =input("> ")
                break 
            except:
                print("Invalid input.Please try again.")

        print("What category was this expense?")
        while True:
            try:
                category=input("> ")
                break
            except:
                print("Invalid input.Please try again.")
        
        addExpense(amountToAdd, category)
    elif(optionSelected =="2"):
        removeExpense()
    elif(optionSelected =="3"):
        listExpenses()
    else:
        print("Invalid input. Please try again.")