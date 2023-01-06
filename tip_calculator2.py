## tip calculator

print("                    ")

print("TIP CALCULATOR")
print("__________________________________")


print("                    ")

##create variable to allow dollar amount w/ decimal places
bill = float(input("Enter your total bill: $"))

print("                    ")

print(f"Original bill: ${bill}")

print("                    ")

## create variables based on 4 different amount tip calculations
## adding round function to two decimal places
tip = round(bill + (bill * .15), 2)
tip1 = round(bill + (bill * .18), 2)
tip2 = round(bill + (bill * .20), 2)
tip3 = round(bill + (bill * .25), 2)

print("Tipping options.")
print("                    ")

## show tip amounts and final totals including tips

print(f"15% tip: ${bill * .15 :,.2f}")
print(f"Total with 15% tip: ${tip} ")
print("                    ")

print(f"18% tip: ${bill * .18 :,.2f}")
print(f"Total with 18% tip: ${tip1} ")
print("                    ")

print(f"20% tip: ${bill * .20 :,.2f}")
print(f"Total with 20% tip: ${tip2} ")
print("                    ")

print(f"25% tip: ${bill * .25 :,.2f}")
print(f"Total with 25% tip: ${tip3} ")

print("                    ")
print("Tip generously! ")
print("____________________________________________    ")

print("                    ")
