# Week3.Python-assignment
Week 3 Python Assignment: Calculate_discount(price, discount_percent)

# Discount Calculator

This Python script calculates the final price of an item after applying a discount. It prompts the user for the original price and the discount percentage. If the discount is 20% or higher, it calculates and displays the discounted price. Otherwise, it displays the original price.

## Features

* Takes the original price and discount percentage as input from the user.
* Calculates the final price after applying the discount if the discount is 20% or more.
* Displays the original price if the discount is less than 20%.
* Includes basic error handling for non-numeric input.

## How to Use

1.  *Save the code:* discount_calculator.py.
2.  *Open a terminal or command prompt:* Navigate to the directory where you saved the discount_calculator.py file.
3.  *Run the script:* Execute the script using the Python interpreter with the command:
    bash
    python discount_calculator.py
    
4.  *Follow the prompts:* The script will ask you to enter:
    * The original price of the item.
    * The discount percentage.
5.  *View the result:* The script will then display the final price after the discount (if applicable) or the original price.

## Code Structure

The script consists of the following main parts:

* **calculate_discount(price, discount_percent) function:**
    * Takes the original price and discount_percent as arguments.
    * Checks if discount_percent is 20% or greater.
    * If true, calculates the discount_amount and returns the final_price.
    * Otherwise, returns the original price.
* *User Input:* Prompts the user to enter the original price and discount percentage using the input() function.
* *Error Handling:* Includes try-except blocks to catch ValueError if the user enters non-numeric input for the price or discount percentage.
* *Function Call:* Calls the calculate_discount() function with the user-provided inputs.
* *Output:* Prints the calculated final price or the original price based on the discount applied.

## Potential Improvements

* *Input Validation:* Implement more robust input validation to ensure the discount percentage is within a valid range (e.g., 0 to 100).
* *Looping for Multiple Calculations:* Allow the user to perform multiple discount calculations without restarting the script.
* *More Informative Output:* Provide more detailed output, such as the amount of discount applied.
* *Handling Invalid Discount Types:* Consider handling cases where the discount might not be a simple percentage (e.g., a fixed amount discount).
