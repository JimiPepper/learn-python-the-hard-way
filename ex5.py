my_name = 'Romain Rose Philippon'
my_age = 35 # the cake is a lie
my_heigh = 74 # inches
my_weight = 180 # lbs
my_eyes = "Brown"
my_teeth = "White"
my_hair = "Brown"

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_heigh)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usualyy %s depending on the coffe." % my_teeth)

# this line is tricky, try to get it right
print("If I add %d, %d, and %d I get %d." % (my_age, my_heigh, my_weight, my_age + my_heigh + my_weight))

one_pound = 0.453592 # kilo
one_inch = 2.54 # centimeter
my_kilo = my_weight * one_pound
my_centimeter = my_heigh * one_inch

print("Or, He's %.2f centimeters tall and %.4f kilos heavy" % (my_centimeter, my_kilo))
