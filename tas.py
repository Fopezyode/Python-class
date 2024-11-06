print("Welcome to the Tip Calculator")
total = float(input("What was the total bill?$"))

tip = int(input("How much tip would you like to give? 10, 12, or 15 \n"))

split = int(input("How Many people to split the bill?"))
total_with_tip = tip / 100 *total + total
total_per_person = total_with_tip/split
final_amount = round(total_per_person, 2)
print(f"Each person should pay: ${final_amount}")