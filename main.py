# This is a basic tip calculator that splits the bill to x people, including tips.

print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, 15? ")
split = input("How many people to split the bill? ")

bill_to_number = float(bill) # Converts bill str input to float
tipInt = bill_to_number * (int(tip) / 100) # adds the tip to the total bill cost
splitInt = int(split) # converts split str input to int
calculation = round((bill_to_number + tipInt) / splitInt, 2) #calculates the total cost with tip,splits the bill between x people,and rounds to 2 numbers after comma.

print(f"Each person should pay: ${calculation}") # Prints the final cost per person.
