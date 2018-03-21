from sys import argv

script,input_file=argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

current_file=open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

'''
Regarding seek() there's not too much to worry about.
First of all, it is useful when operating over an open file.
It's important to note that its syntax is as follows:
fp.seek(offset, from_what)
where fp is the file pointer you're working with; 
offset means how many positions you will move; 
from_what defines your point of reference:
0: means your reference point is the beginning of the file
1: means your reference point is the current file position
2: means your reference point is the end of the file
if omitted, from_what defaults to 0.
Never forget that when managing files, there'll always be a position inside that file where you are currently working on.
When just open, that position is the beginning of the file, but as you work with it, you may advance.
seek will be useful to you when you need to walk along that open file, just as a path you are traveling into.
'''