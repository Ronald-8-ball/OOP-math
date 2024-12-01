class NumberOperations:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def add_numbers(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {result}")

# Creating objects
obj1 = NumberOperations(10, 20, 30)
obj2 = NumberOperations(5, 15, 25)

# Implementing the method
obj1.add_numbers()
obj2.add_numbers()



