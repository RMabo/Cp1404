"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Get the sales amount from the user.
sales = float(input("Enter sales: "))
# Calculate the bonus amount.
if sales < 1000:
  bonus = sales * 0.1
elif sales >= 1000:
  bonus = sales * 0.15
# Print the bonus amount.
print("Bonus:", bonus)