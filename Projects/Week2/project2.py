#  Project 2: Even or Odd Counter with Range
# Concepts Used:
# for loop + range()
# Functions + conditional logic


def count_even_odd(start, end):
    even_count = 0
    odd_count = 0

    for num in range(start, end + 1):
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"Between {start} and {end}:")
    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

count_even_odd(start, end)
