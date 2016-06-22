from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that; hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w") # by default, if no mode is passed, the file opened is on read-mode

print("Truncating the file. Goodbye!")
target.truncate() # impossible if target is open on read-mode

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print("And finally, we close it.")
target.close()

target_opened_back = open(filename)
print(target_opened_back.read())
