print("Have a file named 'in.txt' in the same directory as the converter")

input("Press enter to convert")

try:
    with open("in.txt", "r") as file:
        text = file.readlines()
except:
    input("You dont have a 'in.txt' file")
    quit()

newText = []
for i in text:
    if "\n" in i:
        i = i.replace("\n", "")
    newText.append(i)

try:
    with open("out.txt", "x") as file:
        file.write(str(newText))
except:
    answere = input("You want to overwrite the 'out.txt' file? y or n")
    answere.lower()
    if answere == "y":
        with open("out.txt", "w") as file:
            file.write(str(newText))
    else:
        quit()
