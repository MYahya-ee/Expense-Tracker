import json
import uuid
from datetime import datetime
class expense:
    def __init__(self,name, amount, category):
        self.name = name
        self.id = str(uuid.uuid1())[:5]
        self.amount = float(amount)
        self.category = category
        self.date = datetime.now().strftime("%H:%M %d/%m")

    def to_dict(self):
        return {
            "Name":self.name,
            "Id": self.id,
            "amount": self.amount,
            "date": self.date,
            "category": self.category
        }

    def statement(self):
        return(f"{self.name} bought at {self.date}")

def show_expense():
    with open("python.json", "r") as f:
        jsdat = json.load(f)            
    for i in jsdat:
        print(f"""ID     Name          Amount      Time/Date
{i['Id']}  {i['Name']}      PKR{i['amount']}    {i['date']}"
        """)
    exit()

def filter_categories():
    with open("python.json", "r") as f:
        readme = json.load(f)
    categories = set()
    for i in readme:
        categories.add(i["category"])
    for cat in categories:
        print(f"\n {cat}:")
        for i in readme:
            if i['category'] == cat:
                print(f"""    {i['Name']:<12}   ======    PKR{i['amount']}""")
    exit()
def main():
    while True:
        inp = input("""
========= Expense Tracker =========
1. Add Expense
2. View All Expenses
3. Filter by Category
4. Remove Expense
5. Remove all
6. Export Report (.txt)
0. Quit
===================================
""")

        match inp:
            case "0":
                exit()

            case "1":
                names = input("Enter the name: ")
                categorys = input("Enter the category: ")              
                amounts = input("Enter the amount: ")
                e1 = expense(names, amounts, categorys)
                e1_dict = e1.to_dict()
                with open("python.json", "r") as f:
                    expenses = json.load(f)
                    if not isinstance(expenses, list):  
                        expenses = []                  
                expenses.append(e1_dict)
                with open("python.json", "w") as f:
                    json.dump(expenses, f)
                print("Expense was added")

            case "2":
                print("Here's the list of you expenses:")
                show_expense()

            case "3":
                filter_categories()

            case "4":
                print(f"""Here's the list of you expenses, which one do you want to remove""")
                show_expense()
                inptid = input()
                with open("python.json", "r") as f:
                    redjs = json.load(f)
                new_redjs = []
                for e in redjs:
                    if e["Id"] != inptid:
                        new_redjs.append(e)
                with open("python.json", "w") as f:
                    json.dump(new_redjs, f)
                print("Expense has been deleted")

            case "5":
                perm = input("Are you sure you want to remove all expenses, once done, it's irretrievable: ").upper()
                if perm == "YES":
                    with open("python.json", "w") as f:
                        json.dump([], f)
                    print("All Expenses deleted")
                    exit()
                else:
                    print("Cancelled, returning to menue")         
            
            case "6":
                print(f"""
EXPENSE REPORT — Generated: {datetime.now().strftime("%H:%M %d/%m")}
======================================
""")
                with open("python.json", "r") as f:
                    readme = json.load(f)
                categories = set()
                for i in readme:
                    categories.add(i["category"])
                Total_price = 0
                for cat in categories:
                    cat_price = 0
                    for i in readme:
                        if i['category'] == cat:
                            cat_price += float(i['amount'])
                    Total_price += cat_price
                    print(f"{cat:<15}: PKR {cat_price}") 

                print("--------------------------------------")
                print(f"{'TOTAL':<15}: PKR{Total_price}")
                print("\nFull Expense log: ")
                with open("python.json", "r") as f:
                    jsdat = json.load(f)            
                for i in jsdat:
                    print(f"[{i['date']}] {i['Name']} PKR {i['amount']}")
                print()
                exit()

                
main()


                