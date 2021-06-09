#imports the argv module
from sys import argv

#the argv variables
script, input_file = argv

#the f function to print all
def print_all(f):
    #print the contents of f
    print(f.read())

#the funtion to go to the beginning of the line
def rewind(f):
    f.seek(0)

#the f function to print a line in the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

#this will open the selected file
current_file = open(input_file)


print("First let's print the whole file: \n")

#calls the print_all function to open the file and print all it's contents
print_all(current_file)


print("Now let's rewind, kind of like a tape.")

#calls the rewind function
rewind(current_file)
print("Let's print three lines:")

#initializes the line line_count
current_line = 1
#calls the the print_a_line function
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
