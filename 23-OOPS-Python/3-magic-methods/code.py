# ✅ Example 1: __init__ and __str__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

book1 = Book("Python 101", "Vikash")
print(book1)  # Python 101 by Vikash


# ✅ Example 2: __add__ for Operator Overloading
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"${self.amount}"

wallet1 = Money(50)
wallet2 = Money(70)
total = wallet1 + wallet2
print(total)  # $120


# ✅ Example 3: __len__ and __repr__
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

    def __repr__(self):
        return f"Team({self.members})"

t = Team(["Alice", "Bob", "Charlie"])
print(len(t))   # 3
print(t)        # Team(['Alice', 'Bob', 'Charlie'])
