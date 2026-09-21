#
#SEC290.FA2022.13767
#Christine Griffith
#Step 3 Menu driven interface
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
        attribute = input("What is the attribute name? ")
        value = input("What is the attribute value? ")
        try:
            dictionary[attribute] = int(value)
            print(f"{attribute}:{value} has been stored in the dictionary.")
        except ValueError:
            print(f"'{value}' is not a valid number. The attribute was not stored.")

    elif selection == "c":
        print("Calculate aspect ratio selected.")

        width = dictionary.get("width")
        height = dictionary.get("height")

        if width is None or height is None:
            print("Please make sure both 'width' and 'height' attributes have been entered.")
        else:
            try:
                ratio = width / height
                print(f"The aspect ratio: {ratio}")
            except ZeroDivisionError:
                print("Please enter a positive, non zero number for height.")

    elif selection == "d":
        print("Display the attributes and values selected.")
        print("Displaying the window attributes: ")

        for item in dictionary:
            print(item, dictionary[item])

    else:
        print("{} is invalid. Only a,b,c and d are acceptable.".format(selection))
        print()

print("Done!")
