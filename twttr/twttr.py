yes_vowel = input("Input: ")

print("Output: ", end="")

for w in yes_vowel:
    if w.casefold() in ("a", "e", "i", "o", "u"):
        print("", end="")
    else:
        print(w, end="")

print(" ")