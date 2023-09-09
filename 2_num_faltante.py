# Encuentra el número faltante
# Dada una lista de N-1 enteros que van del 1 al N, encuentra el número entero que falta

def find_missing_number(nums):
    """
    Find the missing number in the list.

    Args:
    - nums (list): List of N-1 integers ranging from 1 to N.

    Returns:
    - int: The missing number.
    """
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum

# Example usage:
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(f"The missing number is: {find_missing_number(numbers)}")
