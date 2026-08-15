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

class tracker:
    def __init__(self):
        self.expenses = []


    def add_expense(self, exp):
        e1_dict = exp.to_dict()
        with open("python.json", "r") as f:
            content = f.read()
            expenses = json.loads(content) if content.strip() else []
        expenses.append(e1_dict)
        with open("python.json", "w") as f:
            json.dump(expenses, f)

    def get_all(self):
        with open("python.json", "r") as f:
            jsdat = json.load(f)            
        for i in jsdat:
            print(f"""
        ID     Name      Amount      Time/Date
        {i['Id']} {i['Name']} PKR{i['amount']}  {i['date']}
                """)
            
    def remove_single(self, inptid):
        with open("python.json", "r") as f:
            redjs = json.load(f)
        new_list = [e for e in redjs if e["Id"] != inptid]
        with open("python.json", "w") as f:
            json.dump(new_list, f)
        print("Expense has been deleted")

    def remove_all(self):
        with open("python.json", "w") as f:
                json.dump([], f)
        print("All Expenses deleted")
        
    
def main():
    t = tracker()
    while True:
        inp = input("""
========= Expense Tracker =========
1. Add Expense
2. View All Expenses
3. Filter by Category
4. Filter by Date Range
5. View Summary
6. Remove Expense
7. Remove all
8. Export Report (.txt)
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
                tracker.add_expense(expense(names, categorys, amounts))
                

            case "2":
                print("Here's the list of you expenses")
                tracker.get_all()

            case "6":
                print(f"""Here's the list of you expenses, which one do you want to remove""")
                tracker.get_all()
                inptid = input()
                tracker.remove_single(inptid)

            case "7":
                perm = input("Are you sure you want to remove all expenses, once done, it's irretrievable: ").upper()
                if perm == "YES":
                    tracker.remove_all()
            

    
main()

