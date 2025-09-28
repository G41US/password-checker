import re

COMMON_PASSWORDS = {"123456", "password", "qwerty", "letmein", "123456789"}

def check_strength(password: str) -> dict:
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short, use at least 12 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is too common and unsafe")
        score = 0

    if score >= 6:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return {"strength": strength, "feedback": feedback}
