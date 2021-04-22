import sys

orange = ""
green = ""
with open(f"sprites/{sys.argv[1]}.bmp541", "r") as f:
    arr = f.read().split()
    for i in arr:
        if i == "d80":
            orange += "247\n"
            green += "276\n"
        elif i == "48f":
            orange += "fb4\n"
            green += "4fc\n"
        elif i == "acf":
            orange += "fec\n"
            green += i + "\n"
        else:
            orange += i + "\n"
            green += i + "\n"

with open(f"sprites/{sys.argv[2]}.bmp541", "w") as f:
    f.write(green)
