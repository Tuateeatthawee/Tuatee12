# Example 1: Hello World
print("Hello, World!")

# Example 2: Simple Addition
a = 5
b = 3
print(a + b)

# Example 3: List Comprehension
squares = [x**2 for x in range(10)]
print(squares)

# Example 4: Dictionary Usage
person = {"name": "Alice", "age": 25}
print(person["name"])

# Example 5: Function Definition
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))

# Example 6: For Loop
for i in range(5):
    print(i)

# Example 7: If-Else Statement
num = 10
if num > 0:
    print("Positive number")
else:
    print("Negative number")

# Example 8: Reading a File
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Example 9: Writing to a File
with open('output.txt', 'w') as file:
    file.write("Hello, file!")

# Example 10: Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")