# Defines a function called can_buy_house that takes two arguments - value and salary
def can_buy_house(value, salary):
    # Set max_value to five times salary, using this as a comparison to value
    max_value = salary * 5
    # Compare the size of max_value to the size of value, and define what the output depends on
    if value <= max_value:
        return "Yes"
    else:
        return "No"
# Ask user to input the value and the salary
value = input("Please enter the vlue of the house: ").upper()  # You can enter 180000
salary = input("Please enter your salary: ").upper()  # You can enter 35000
# The result of this calculation is stored in the variable can_buy
can_buy = can_buy_house(value, salary)
# Output the result
print(can_buy) # If you type value=180000, salary=35000, the output should be yes