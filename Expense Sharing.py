class ExpenseManager:
    def __init__(self):
        self.members=[]
        self.balance={}

    def add_members(self):
        n=int(input("Enter number of members : "))

        for i in range (n):
            name=input(f"Enter the name of number { i+1}: ").strip()
            self.members.append(name)

    def add_expense(self):
        print("add_expense")

    def show_expenses(self):
        print("show_expenses")

    def run(self):
        self.add_members()
        while True:
           
            print("\n1. Add an Expense\n2. show Expenses\n3. Exit")
            try:
                choice =int(input("Enter your option: "))
                if choice==1:
                    self.add_expense()
                elif choice==2:
                    self.show_expenses()
                elif choice==3:
                    break
                else:
                    print("Invalid options.Try again")
            except ValueError:
                print("Please enter a valid number.")        




ExpenseManager().run()

