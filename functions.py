def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"The final price after applying the discount is: Ksh.{final_price:.2f}")
else:
    print(f"No discount applied. The original price is: Ksh.{original_price:.2f}")
