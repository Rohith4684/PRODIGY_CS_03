import re


def password_strength_checker(password):
    # Initialize strength score
    strength_score = 0
    feedback = []

    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    # Update score and feedback based on criteria
    if length_criteria:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        strength_score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if lowercase_criteria:
        strength_score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if number_criteria:
        strength_score += 1
    else:
        feedback.append("Password should include at least one number.")

    if special_criteria:
        strength_score += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Determine strength level
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide feedback
    feedback_message = " ".join(feedback) if feedback else "Your password is strong."

    return strength, feedback_message


# Prompt the user to enter a password
password = input("Enter your password: ")
strength, feedback = password_strength_checker(password)
print(f"Password Strength: {strength}")
print(f"Feedback: {feedback}")
