#By: Sabria Fafach
#Date: January 30, 2025
#Name: program_1.py

cost_item1=float(input("Enter the cost in dollars of first item:"))
cost_item2=float(input("Enter the cost in dollars of second item:"))
cost_item3=float(input("Enter the cost in dollars of third item:"))
cost_item4=float(input("Enter the cost in dollars of fourth item:"))
cost_item5=float(input("Enter the cost in dollars of fifth item:"))

subtotal=cost_item1+cost_item2+cost_item3+cost_item4+cost_item5
print(f"Your subtotal is: ${subtotal}")

sales_tax=0.07
tax_amount=subtotal*sales_tax

print(f"The amount of sales tax is ${tax_amount}")
print(f"Your total is ${subtotal+tax_amount}")
