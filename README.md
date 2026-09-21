# Window Administration Application

A three step progression of a menu driven command line program for tracking a window's attributes (like width and height) and calculating its aspect ratio.

## Files

- **Week_4_Assignment_Step1_Christine_Griffith.py** - the menu skeleton. Shows the menu and responds to each option with a placeholder message, no attributes are actually stored yet.
- **Week_4_Assignment_Step2_Christine_Griffith.py** - adds real functionality: entering attributes into a dictionary, calculating the aspect ratio from stored width and height, and displaying all stored attributes.
- **Week_4_Assignment_Step3_Christine_Griffith.py** - builds on Step 2 by adding error handling for a zero height value when calculating the aspect ratio.

All three share the same menu:

```
a: Exit application
b: Enter an attribute
c: Calculate and display the aspect ratio
d: Display the window attributes and values
```

## What it does

- **Option b** prompts for an attribute name and a numeric value, then stores it in a dictionary (e.g. `width: 1920`). A non-numeric value is rejected with a message instead of being stored.
- **Option c** looks up `width` and `height` from the dictionary and prints the aspect ratio (`width / height`). If either attribute hasn't been entered yet, it says so instead of failing. In Step 3, entering `0` for height is caught and reported instead of crashing.
- **Option d** lists every attribute currently stored, along with its value.
- **Option a** exits the application.

## Requirements

- Python 3

## Usage

Run whichever step you want from the command line:

```
python3 Week_4_Assignment_Step1_Christine_Griffith.py
python3 Week_4_Assignment_Step2_Christine_Griffith.py
python3 Week_4_Assignment_Step3_Christine_Griffith.py
```

Example session (Step 2 or 3):

```
Please select a,b,c or d: b
What is the attribute name? width
What is the attribute value? 1920

Please select a,b,c or d: b
What is the attribute name? height
What is the attribute value? 1080

Please select a,b,c or d: c
The aspect ratio: 1.7777777777777777
```
