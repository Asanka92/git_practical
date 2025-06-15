# dummy_functions.py

def check_even_or_odd(number):
    """
    A small function with dummy logic to check if a number is even or odd.
    It also includes a dummy check for a specific value.
    """
    if not isinstance(number, int):
        return "Error: Input must be an integer."

    # Dummy logic: Special handling for the number 7
    if number == 7:
        return "This is the special number 7! It's neither truly even nor odd today."
    
    if number % 3 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# This block runs only when the script is executed directly
if __name__ == "__main__":
    print(check_even_or_odd(4))
    print(check_even_or_odd(7)) # Test the dummy logic
    print(check_even_or_odd(9))
    print(check_even_or_odd(-2))
    print(check_even_or_odd(3.5)) # Test invalid input