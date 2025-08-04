# ✅ Project 1: Mad Libs Generator

# Concepts Used:
# input(), print()
# String formatting (f-string)
# Variables

print("Let's create a fun story! Please answer the following:")

name = input("Enter a name: ")
place = input("Enter a place: ")
hobby = input("Enter a hobby: ")
adjective = input("Enter an adjective: ")
animal = input("Enter your favorite animal: ")

story = f"""
One day, {name} went to {place} for a vacation. While enjoying the {adjective} weather,
{name} saw a {animal} that was also doing {hobby}! It was the best vacation ever.
"""

print("\nHere’s your story:")
print(story)
