from sys import argv

script, username = argv
prompt = '@~> '

print("Hi %s, I'm the %s script." % (username, script))
print("I'd like to ask you a few question.")
print("Do you like me %s ?" % username)
likes = input(prompt)

print("Where do you live %s ?" % username)
lives = input(prompt)

print("What kind of computer do you have ?")
computer = input(prompt)

print("""
Allright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))
