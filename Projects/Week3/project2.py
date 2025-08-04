#  Project 2: Text Analyzer

#  Concepts:
# String slicing, counting, and formatting
# Dictionary to store character/word counts
# Error handling
# Simple logic for whitespace/punctuation

# Text Analyzer

def analyze_text(text):
    word_count = len(text.split())
    char_count = len(text)
    vowel_count = 0

    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            vowel_count += 1

    print("\nText Analysis:")
    print(f"Total characters: {char_count}")
    print(f"Total words: {word_count}")
    print(f"Vowels: {vowel_count}")

try:
    user_text = input("Enter some text to analyze: ")
    if not user_text.strip():
        raise ValueError("Empty input is not allowed.")
    analyze_text(user_text)
except Exception as e:
    print("Error:", e)
