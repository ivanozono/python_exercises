def is_valid_parentheses(s: str) -> bool:
    """
    Validates the sequence of parentheses.

    Args:
    - s (str): Input string containing only the characters (, ), {, }, [ and ].

    Returns:
    - bool: True if the sequence is valid, otherwise False.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

# Example usage:
sequence = input("Enter the sequence of parentheses: ")
print("Valid" if is_valid_parentheses(sequence) else "Invalid")
