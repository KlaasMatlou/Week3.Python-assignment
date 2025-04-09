def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage to apply.

  Returns:
    The final price after discount if the discount is 20% or higher,
    otherwise returns the original price.
  """
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price 
  else:
    return price 

# Get user input for the original price
try:
  original_price = float(input("Enter the original price of the item: "))
except ValueError:
  print("Invalid input. Please enter a numeric value for the price.")
  exit()

# Get user input for the discount percentage
try:
  discount_percentage = float(input("Enter the discount percentage: "))
except ValueError:
  print("Invalid input. Please enter a numeric value for the discount percentage.")
  exit()

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if discount_percentage >= 20:
  print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
else:
  print(f"No discount applied. The original price is: ${final_price:.2f}")