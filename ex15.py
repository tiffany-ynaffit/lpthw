#line 2 and 4 get the filename from argv
#from sys import argv

#script, filename = argv

#using inout to get the filename
filename = input("What is the file name?")
#opens the file
txt = open(filename)

#prints the filename
print(f"Here's your file {filename}:")
#prints what's in the file for you to read it
print(txt.read())
#closes the file
txt.close()


print("Type the filename again")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
