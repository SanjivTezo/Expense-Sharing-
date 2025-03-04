class ExpenseManager:
    def __init__(self):
        self.members=[]
        self.balances={}

    def add_members(self):
        n=int(input("Enter number of members : "))

        for i in range (n):
            name=input(f"Enter the name of number { i+1}: ").strip()
            self.members.append(name)
            self.balances = {member: {other: 0 for other in self.members} for member in self.members}

    def add_expense(self):
        print("1. All users share the expense")
        print("2. Only some users share the expense")
        choice = int(input("Choose an option: "))

        if choice == 1:
            print("\n1. Everyone shares the expense equally")
            print("2. Expense is shared in a ratio")
            split_choice = int(input("Choose an option: "))

            if split_choice == 1:
                involved = self.members[:] 
            elif split_choice == 2:
                payer = input("Who paid the expense? ").strip()
                if payer not in self.members:
                    print("Payer is not a valid member")
                    return
                
                amount = float(input("Enter amount paid: "))
                
                ratio_input = input(f"Enter the ratio for {', '.join(self.members)} (use ':' as delimiter, e.g., 1:3:2): ").strip()
                ratio_parts = ratio_input.split(":")
                
                if len(ratio_parts) != len(self.members) or not all(part.isdigit() for part in ratio_parts):
                    print("Invalid ratio input. No expense recorded.")
                    return
                
                ratios = list(map(int, ratio_parts))
                total_ratio = sum(ratios)

                for i, person in enumerate(self.members):
                    if person != payer:
                        self.balances[person][payer] += (amount * ratios[i]) / total_ratio

                self.check_balances()
                return 
            
            else:
                print("Invalid choice. Returning to main menu.")
                return

        elif choice == 2:
            involved = input("Enter names of people who share the expense (comma-separated): ").strip().split(",")
            involved = [person.strip() for person in involved if person.strip() in self.members]

            if not involved:
                print("Invalid members selected. No expense recorded.")
                return

        else:
            print("Invalid choice. Returning to main menu.")
            return

        payer = input("Who paid the expense? ").strip()
        if payer not in self.members:
            print("Payer is not a valid member")
            return

        amount = float(input("Enter amount paid: "))
        
        split_amount = amount / len(involved)
        for person in involved:
            if person != payer:
                self.balances[person][payer] += split_amount

        self.check_balances()


    def check_balances(self):
       
        for member in self.members:
            for other in self.members:
                if self.balances[member][other] > 0 and self.balances[other][member] > 0:
                    min_value = min(self.balances[member][other], self.balances[other][member])
                    self.balances[member][other] -= min_value
                    self.balances[other][member] -= min_value


    def show_expenses(self):
        print("\nBalance Sheet:")
        print("\t" + "\t".join(self.members))
        for member in self.members:
            print(member, end="\t")
            for other in self.members:
                # print(f"{self.balances[member][other]:.2f}", end="\t")
                print(f"{int(self.balances[member][other])}", end="\t")
            print()

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

if __name__ == "__main__":
    ExpenseManager().run()

