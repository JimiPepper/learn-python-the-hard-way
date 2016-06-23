from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on line, how ?
in_file = open(from_file)
indata = in_file.read()

print("The input file is %d bytes long" % len(indata))
print("Does the output file exists? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input('?')

out_file = open(to_file, 'w')
out_file.write(indata)

print("Allright, all done.")

out_file.close()
in_file.close()


to_file = "new_file.txt"
open(to_file, 'w').write(open(from_file).read()) # exercise : the reduced code that performs the exact same behaviour as above
