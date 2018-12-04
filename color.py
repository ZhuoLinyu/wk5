COLOR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
               "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "azure4": "#838b8b"}


color = input("Enter color name: ")

while color != "":

    if color in COLOR_NAMES:

        print(color, "is", COLOR_NAMES[color])

    else:

        print("Invalid color name")

    color = input("Enter color name: ")
