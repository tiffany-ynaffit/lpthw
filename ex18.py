#this one is like the scripts with argv
#def stands for define
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1 = {arg1}, arg2 = {arg2}")

#args* can be done like this also:
def print_two_again(arg1, arg2) :
    print(f"Arg1 is {arg1}, arg2 is {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing.")

print_two("Tiffany", "Nyawambi")
print_two_again("Leana","Saunda")
print_one("Vivyanne")
print_none()
