
# more files
#argv is a list in Python that contains all the command-line arguments passed to the script
from sys import argv
#Return True if path refers to an existing path or an open file descriptor. Returns False for broken symbolic links.
from os.path import exists

script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))

# we could do these two on one line, how?
#in_file = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()

print("The input file is {} bytes long".format(len(indata)))

print("Does the output file exist? {}".format(exists(to_file)))

print("Ready, hit RETURN to continue, CTRL-C abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)
'''
print("Alrighty, all done")
'''
out_file.close()
in_file.close()