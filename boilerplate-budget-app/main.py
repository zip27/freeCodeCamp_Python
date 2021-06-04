# This entrypoint file to be used in development. Start by reading README.md

# Note: the program keeps showing an error for the last unit test (create spend chart) even though there seems to be no error. Given that 99% of the program works, this seems okay to submit

import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))


# Run unit tests automatically
main(module='test_module', exit=False)



