"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Get the score from the user.
score = float(input("Enter score: "))
# Check if the score is valid.
if score < 0 or score > 100:
    print("Invalid score")
# Determine the score status.
else:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")