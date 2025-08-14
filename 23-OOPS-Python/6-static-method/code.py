# 🧪 Code Example: Without Static Method
class MathTool:
    def square(x):
        return x * x

print(MathTool.square(5))  # ❌ Error: missing 1 required positional argument


# ✅ Using @staticmethod Correctly
class MathTool:
    @staticmethod
    def square(x):
        return x * x

    @staticmethod
    def is_even(n):
        return n % 2 == 0

# No need to create object
print(MathTool.square(5))       # 25
print(MathTool.is_even(10))     # True


# You can also call it via instance, but it's not recommended:
tool = MathTool()
print(tool.square(7))  # Works, but prefer MathTool.square(7)


# 🎯 Mini Use Case Example
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

print("0°C in F:", Temperature(0).to_fahrenheit())  # Instance method
print("300K in °C:", Temperature.kelvin_to_celsius(300))  # Static method
