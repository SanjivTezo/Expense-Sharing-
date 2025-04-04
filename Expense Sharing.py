class ExpenseManager:
    def __init__(self):
        self.members=[]
        self.balances={}

    def add_members(self):
        while True:  
            try:
                n = int(input("Enter number of members: "))
                break  
            except ValueError:
                print("Error: Please enter numbers only")
        
        i = 0
        while i < n:
            name = input(f"Enter the name of number {i+1}: ").strip()
            if not name or name.isspace():
                print("Error: Name cannot be empty or just spaces")
                continue
            if name.isdigit():
                print("Error: Name must contain letters, not just numbers")
                continue
            if name in self.members:
                print("Error: This name already exists")
                continue
                
            self.members.append(name)
            self.balances = {member: {other: 0 for other in self.members} for member in self.members}
            i += 1 
            
    def add_expense(self):
        while True: 
            print("\n1. All users share the expense")
            print("2. Only some users share the expense")
            print("3. Back to main menu") 
            try:
                choice = int(input("Choose an option: "))
            except ValueError:
                print("Please enter a valid number")
                continue
            
            if choice == 3: 
                return
            
            if choice == 1:
                while True:  
                    print("\n1. Everyone shares the expense equally")
                    print("2. Expense is shared in a ratio")
                    print("3. Back to previous menu")  
                    try:
                        split_choice = int(input("Choose an option: "))
                    except ValueError:
                        print("Please enter a valid number")
                        continue
                    
                    if split_choice == 3:  
                        break  
                    
                    if split_choice == 1:
                        involved = self.members[:] 
                        break
                    elif split_choice == 2:
                        payer = input("Who paid the expense? ").strip()
                        if payer not in self.members:
                            print("Payer is not a valid member")
                            continue  
                        
                        try:
                            amount = float(input("Enter amount paid: "))
                        except ValueError:
                            print("Please enter a valid amount")
                            continue
                        
                        ratio_input = input(f"Enter the ratio for {', '.join(self.members)} (use ':' as delimiter, e.g., 1:3.5:2): ").strip()
                        ratio_parts = ratio_input.split(":")
                        
                        try:
                            ratios = list(map(float, ratio_parts))
                        except ValueError:
                            print("Invalid ratio input. Please enter numbers only.")
                            continue
                            
                        if len(ratio_parts) != len(self.members):
                            print(f"Please enter exactly {len(self.members)} ratio values")
                            continue
                        
                        total_ratio = sum(ratios)

                        for i, person in enumerate(self.members):
                            if person != payer:
                                self.balances[person][payer] += (amount * ratios[i]) / total_ratio

                        self.check_balances()
                        return 
                    else:
                        print("Invalid choice. Please try again.")
                        continue
                
                if split_choice == 3: 
                    continue  
                else:
                    break 
                
            elif choice == 2:
                while True:
                    involved_input = input("Enter names of people who share the expense (comma-separated): ").strip()
                    involved = [person.strip() for person in involved_input.split(",")]
                    
                    
                    invalid_members = [name for name in involved if name not in self.members]
                    if invalid_members:
                        print(f"Error: These members are not valid: {', '.join(invalid_members)}")
                        print(f"Valid members are: {', '.join(self.members)}")
                        continue
                    
                    if not involved:
                        print("Error: No valid members selected")
                        continue
                        
                    break
                break
            else:
                print("Invalid choice. Please try again.")
                continue

       
        payer = input("Who paid the expense? ").strip()
        if payer not in self.members:
            print("Payer is not a valid member")
            return

        try:
            amount = float(input("Enter amount paid: "))
        except ValueError:
            print("Please enter a valid amount")
            return
        
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
                print(f"{self.balances[member][other]:.2f}", end="\t")
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