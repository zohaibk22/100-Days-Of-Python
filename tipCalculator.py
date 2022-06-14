print("Welcome to the tip calculator!")
total = float(input("what was the total bill? $"))
tip_amount = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_num = int(input("How many people to split the bill? "))

bill_total = round(total + (total * (tip_amount/100)), 2)
each_person = round(bill_total / people_num, 2)

print(f"each person should pay: {each_person}")