import json
import datetime
import time
import os
import calendar
import matplotlib.pyplot as plt

current_balance = 0

transactions = []



def ShowBalanceChart():
    plt.ion()
    dates = []
    balances = []
    running_balance = 0
    for transaction in transactions:
        transaction_date = datetime.date.fromisoformat(transaction['date'])
        if transaction['type'] == "income":
            running_balance += transaction['amount']
        elif transaction['type'] == "expense":
                running_balance -= transaction['amount']
        dates.append(transaction_date)
        balances.append(running_balance)
    plt.plot(dates, balances)
    plt.title("Balance Over Time")
    plt.xlabel("Date")
    plt.ylabel("Balance")
    plt.draw()
            



def SaveData():
    data = {
        "current_balance": current_balance,
        "transactions": transactions
    }
    with open("finance_data.json" , "w") as file:
        json.dump(data , file)



def LoadData():
    global current_balance,transactions
    with open("finance_data.json" , "r") as file: 
        data = json.load(file)

    current_balance = data["current_balance"]
    transactions = data["transactions"]



def AddIncome():
    global current_balance
    income = int(input("Please enter income amount: "))
    current_balance += income
    transaction = {
        "type" : "income",
        "amount" : income,
        "category": input("Please Enter Category: "),
        "date": str(datetime.date.today()),
        "description": input("Please Enter Description: ")
    }
    transactions.append(transaction)
    print(f"Income added: {income}TL")
    print(f"Current Balance: {current_balance}TL")
    SaveData()
    ShowBalanceChart()
    time.sleep(4)
    os.system("cls")



def AddExpense():
    global current_balance
    expense = int(input("Please enter expense amount: "))
    current_balance -= expense
    transaction = {
        "type" : "expense",
        "amount" : expense,
        "category": input("Please Enter Category: "),
        "date": str(datetime.date.today()),
        "description": input("Please Enter Description: ")
    }
    transactions.append(transaction)
    print(f"Expense added: {expense}TL")
    print(f"Current Balance : {current_balance}TL")
    SaveData()
    time.sleep(4)
    os.system("cls")


def DisplayTransaction(transaction):
    print("--- Transaction ---")
    print(f"Type: {transaction['type']}")
    print(f"Amount: {transaction['amount']}")
    print(f"Category: {transaction['category']}")
    print(f"Date: {transaction['date']}")
    print(f"Description: {transaction['description']}")



def ViewTransactions():

    option3 = True
    while(option3):
        print("1-Today")
        print("2-This week")
        print("3-This Month")
        print("4-All Transactions")
        print("0-Back")
        option4 = int(input("Please select a filter: "))
        if option4 == 1:
            for transaction in transactions:
                if transaction['date']==str(datetime.date.today()):
                    DisplayTransaction(transaction)

        elif option4 == 2:
            today = datetime.date.today()  
            start_date = today - datetime.timedelta(days=today.weekday())
            end_date = start_date + datetime.timedelta(days=6)

            for transaction in transactions:
                transaction_date = datetime.date.fromisoformat(transaction['date'])

                if start_date <= transaction_date <= end_date:
                    DisplayTransaction(transaction)
                    
        elif option4 == 3:
            today = datetime.date.today()
            start_date=today.replace(day=1)
            days_in_month = calendar.monthrange(today.year,today.month)[1]
            end_date = start_date + datetime.timedelta(days=days_in_month-1)

            for transaction in transactions:
                transaction_date = datetime.date.fromisoformat(transaction['date'])

                if start_date<= transaction_date <=end_date:
                    DisplayTransaction(transaction)

        elif option4 == 4:
            for transaction in transactions:
                    DisplayTransaction(transaction)

        elif option4 == 0:
            option3 = False
        
    time.sleep(5)
    os.system("cls")


def CompoundIncomeCalculator():
    
    while(True):
        try:
            initial_amount = float(input("Enter initial amount: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while(True):
        try:
            interest_rate = float(input("Enter Interest Rate: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while(True):
        try:
            periods = int(input("Enter number of periods: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    current_amount = initial_amount

    for i in range(periods):        
        interest_amount = interest_rate / 100 * current_amount
        current_amount+= interest_amount

    print(f"Final Amount: {current_amount:.2f}")
    print(f"Total Profit: {current_amount-initial_amount:.2f}")
    time.sleep(7)
    os.system("cls")



def MonthlyFinancialSummary():
    while(True):
        print("===== Monthly Financial Summary =====")
        print("1-January")
        print("2-February")
        print("3-March")
        print("4-April")
        print("5-May")
        print("6-June")
        print("7-July")
        print("8-August")
        print("9-September")
        print("10-October")
        print("11-November")
        print("12-December")
        print("0-Exit")
        selected_month = int(input("Select a month: "))
        selected_year = int(input("Select a year: "))

        total_income =0
        total_expense= 0
        for transaction in transactions:
            transaction_date = datetime.date.fromisoformat(transaction['date'])
            if selected_month == transaction_date.month:
                if selected_year == transaction_date.year:
                    if transaction['type'] == "income":
                        total_income+=transaction['amount']
                        DisplayTransaction(transaction)
                    elif transaction['type'] == "expense":
                        total_expense += transaction['amount']
                        DisplayTransaction(transaction)
        net_change = total_income - total_expense
        print(f"Total Income: {total_income}")
        print(f"Total Expense: {total_expense}")
        print(f"Net Change: {net_change}")



def CategoryAnalysis():
    categories = []
    for transaction in transactions:
        if transaction['category'] not in categories:
            categories.append(transaction['category'])
    for category in categories:
        category_total = 0
        for transaction in transactions:
            if transaction['category'] == category:
                if transaction['type'] == "expense":
                    category_total += transaction['amount']
        print(f"{category} => {category_total:.2f}")



def ResetFinanceData():
    global current_balance
    answer = input("Are you sure? Yes/No  ").lower()
    if answer == "yes":
        current_balance = 0
        transactions.clear()
        SaveData()

    elif answer == "no":
        pass
    time.sleep(2)
    os.system("cls")


LoadData()


option2 = True 
while(option2):
    print("==================")
    print("FINANCE TRACKER")
    print("==================")

    print(f"Current Balance: {current_balance} TL")

    print("1-Add Income")
    print("2-Add Expense")
    print("3-Vieww Transaction History")
    print("4-Compound Income Calculator")
    print("5-Monthly Financial Summary")
    print("6-Category Analysis")
    print("7-Reset Fınance Data")
    print("0-Exit")
    option = int(input("Please select an option: "))

    if option == 1:
        AddIncome()
    elif option ==2:
        AddExpense()
    elif option ==3:
        ViewTransactions()
    elif option == 4:
        CompoundIncomeCalculator()
    elif option == 5:
        MonthlyFinancialSummary()
    elif option == 6:
        CategoryAnalysis()
    elif option == 7:
        ResetFinanceData()
    elif option == 0:
        option2 = False