# XYZ store plans to give festival discount to its customers . The store management has decided to give discount on the following criteria ;
# Shopping amount :   >= 500 and < 1000 ,   Discount : 5%
# Shopping amount :  >= 1000 and  < 2000 ,   Discount :  8%
# Shopping amount :   >= 2000 ,   Discount :  10%
# .. An additional discount of 5% is given to customers who are the members of the store. Create  a python program using user defined function  that accepts the shopping amount as a parameter & calculates discount & net .

# The net payable amount = Total shopping amount - discount
def calculate_discount_and_net(shopping_amount, is_member):
    # Apply discount based on shopping amount
    if shopping_amount >= 500 and shopping_amount < 1000:
        discount_percentage = 5
    elif shopping_amount >= 1000 and shopping_amount < 2000:
        discount_percentage = 8
    elif shopping_amount >= 2000:
        discount_percentage = 10
    else:
        discount_percentage = 0  # No discount for shopping amount less than 500

    # Additional discount for members
    if is_member:
        discount_percentage += 5

    # Calculate discount and net payable amount
    discount = (discount_percentage / 100) * shopping_amount
    net_payable = shopping_amount - discount

    return discount, net_payable

# Input shopping amount and membership status
shopping_amount = float(input("Enter the shopping amount: "))
is_member = input("Are you a member of the store? (yes/no): ").lower() == 'yes'

# Calculate discount and net payable amount using the function
discount, net_payable = calculate_discount_and_net(shopping_amount, is_member)

# Display the results
print(f"Shopping Amount: { shopping_amount:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Net Payable Amount: {net_payable:.2f}")


