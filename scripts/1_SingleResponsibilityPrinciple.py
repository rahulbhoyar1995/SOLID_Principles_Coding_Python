# S - Single Responsibility Principle
# The Single Responsibility Principle (SRP) states that a class should have only one reason to change. In other words, a class should do one thing and do it well. This makes our code easier to understand and maintain.

# For example, let's say we have a class called Calculator that performs addition, subtraction, multiplication, and division. This violates the SRP because it has multiple responsibilities. Instead, we can create separate classes for each operation, like Addition, Subtraction, Multiplication, and Division.


class Addition:
    def calculate(self, x, y):
        return x + y

class Subtraction:
    def calculate(self, x, y):
        return x - y

class Multiplication:
    def calculate(self, x, y):
        return x * y

class Division:
    def calculate(self, x, y):
        return x / y
