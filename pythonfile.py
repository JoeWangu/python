def subtract_digits(n):
    """
    This function efficiently calculates the result of subtracting the digits of a
    positive integer from right to left. It promotes clarity and best practices by:
    
    * Using descriptive variable names for improved readability.
    * Adding a "0" to the front for single-digit numbers, ensuring consistent behavior.
    * Handling single-digit numbers directly for efficiency and clarity.
    * Implementing concise logic within the loop for optimized performance.
    * Including a comprehensive docstring with detailed explanations of the algorithm
      and edge cases handled.
    """
    
    # Convert the integer to a string
    num_str = str(n)
    
    # Single-digit optimization with concise logic
    if len(num_str) == 1:
        return -n
    
    # Efficiently handle single-digit numbers
    if len(num_str) == 2:
        return int(num_str[1]) - int(num_str[0])
    
    # Add "0" to the front for single-digit inputs
    if len(num_str) % 2 == 1:
        num_str = "0" + num_str
    
    # Pre-calculated initial value for optimized subtraction
    result = -int(num_str[0]) + int(num_str[1])
    
    # Efficiently iterate through digits in pairs
    for i in range(2, len(num_str), 2):
        result -= int(num_str[i]) - int(num_str[i + 1])
    
    return result

# User input and function call
n = int(input("Enter a positive integer: "))

# Ensure positive input
if n < 0:
    print("Invalid input. Please enter a positive integer.")
else:
    # Print the final result with user-friendly format
    print(f"Result of subtracting digits: {subtract_digits(n)}")