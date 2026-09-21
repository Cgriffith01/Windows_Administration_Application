#
#SEC290.FA2022.13767
#Christine Griffith
#Step 1 Menu driven interface
#

dictionary = {}

window_attributes = """
Window Administration Application\n
a: Exit application
b: Enter an attribute
c: Calculate and display the aspect ratio
d: Display the window attributes and values
"""
done = False

while not done:
    print(window_attributes)

    selection = input("Please select a,b,c or d: ")

    if selection == "a":
        done = True

    elif selection == "b":
        print("Entering an attribute selected.")

    elif selection == "c":
        print("Calculate aspect ratio selected.")

    elif selection == "d":
        print("Display the attributes and values selected.")

    else:
        print("{} is invalid. Only a,b,c and d are acceptable.".format(selection))
        print()

print("Done!")
