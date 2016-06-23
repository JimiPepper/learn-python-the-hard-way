### GLOBAL FUNCTIONS

def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVINDING %d / %d" % (a, b))
    return a / b

### MAIN CODE

print("Let's do some math with just functions!")

age = add(30, 5)            # -> 35
height = subtract(78, 4)    # -> 74
weight = multiply(90, 2)    # -> 180
iq = divide(100, 2)         # -> 50

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it anyway
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # 35 + (74 - (180 * (50 / 2))) = -4391

print("That becomes:", what, "Can you do it by hand?")
