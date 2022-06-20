from shutil import copyfile
from sys import exit
import os

print(f"The copy tool will be set to the following directory: %s" % os.getcwd())

menu_options = {
    1: 'Keep the current working directory',
    2: 'Change the directory',
    3: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key])

def option1():
     print(f"Current working directory: %s" % os.getcwd())

def option2():
     path = input(f"Set a new directory: \n")
     os.chdir(path)
     print(f"Current working directory: %s" % os.getcwd())

while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        
        #Check what choice was entered and act accordingly
        if option == 1:
            option1()
            break
        elif option == 2:
            option2()
            break
        elif option == 3:
            print('Thanks message before exiting')
            exit()


source = input("Enter source file with full path: ")
target = input("Enter target file with full path: ")

# adding exception handling
try:
    copyfile(source, target)
except IOError as e:
    print("Unable to copy file. %s" % e)
    exit(1)
except:
    print("Unexpected error:", sys.exc_info())
    exit(1)

print("\nFile copy done!\n")

while True:
    print("Do you like to print the file? (y/n): ")
    check = input()
    if check == 'n':
        break
    elif check == 'y':
        file = open(target, "r")
        print("\nHere follows the file content:\n")
        print(file.read())
        file.close()
        print()
        break
    else:
        continue

