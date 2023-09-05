camel = input("camelCase: ")

for c in camel:
    if c.islower() is True:
        print(c, end="")
    else:
        print(f"_{c.casefold()}", end="")

print(" ")
