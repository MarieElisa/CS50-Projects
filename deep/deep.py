question = input("What is the Great Answer of Life, the Universe and Everything? ")

match question.strip().title():
    case "42" | "Forty Two" | "Forty-Two":
        print("Yes")
    case _:
        print("No")