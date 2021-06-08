weight = int(input("Weight: "))
unit = input(" (L)bs or (K)g : ")

if unit.upper() == "K":
    converted = round(weight * 0.45, 2)
    print(f"You are {converted} kilos")
else:
    converted = round(weight/0.45300,2)
    print(f" you are {converted} pounds")


