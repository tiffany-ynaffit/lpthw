def add (a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide (a, b):
    print(f"Multiplying {a} / {b}")
    return a / b

print("Let's do something with just functions!")

age = add(13, 10)
height = subtract(170, 2)
weight = multiply(11, 5)
iq = divide(200, 2)

print(f"age: {age}, height: {height}, weight: {weight}, iq: {iq}")

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes " ,what, " can you do it by hand?")
