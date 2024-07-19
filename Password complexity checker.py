import re

def check_password_strength(password):
    # Check if password length is at least 8 characters
    if len(password) < 8:
        return "Password should be 8 characters or longer."

    # Initialize criteria
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special_char = bool(re.search(r'[\W_]', password))  # \W matches non-alphanumeric, _ matches underscore

    # Check which criteria are missing
    missing_criteria = []
    if not has_uppercase:
        missing_criteria.append("uppercase letters")
    if not has_lowercase:
        missing_criteria.append("lowercase letters")
    if not has_digit:
        missing_criteria.append("numbers")
    if not has_special_char:
        missing_criteria.append("special characters")

    # If all criteria are met
    if not missing_criteria:
        return "Very Strong"

    # Construct feedback message
    feedback = f"Please include "
    if len(missing_criteria) == 1:
        feedback += missing_criteria[0]
    else:
        feedback += ", ".join(missing_criteria[:-1]) + f" and {missing_criteria[-1]}"
    feedback += " in the password."

    return feedback

# Example usage:
while True:
    password = input("Enter a password to assess its strength (minimum 8 characters): ")
    strength = check_password_strength(password)
    print(f"The password '{password}' is assessed as: {strength}")
    if strength == "Very Strong":
        break
