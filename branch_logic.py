# branch_logic.py

def categorize_number(num):
    if num < 0:
        return "Negative"
    elif num == 0:
        return "Zero"
    elif num > 0 and num <= 10:
        return "Small Positive"
    else:
        return "Large Positive"
