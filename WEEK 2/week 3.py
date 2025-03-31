def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, it applies the discount.
    Otherwise, it returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display result
    print(f"Final price after discount: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numerical values.")
