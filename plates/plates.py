def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    conditions = 0
    first_num = 0
    if s[:2].isalpha():  # Two first chara are letters
        conditions += 1

    if 2 <= len(s) <= 6:  # Lenght between 2 & 6
        conditions += 1

    if s.isalnum():  # Only alphanumeric
        conditions += 1

    for letter in s:
        if letter.isnumeric() == True:
            if letter == "0":  # Spot the first digit in str
                conditions -= 1
            first_num = s.find(letter)
            break

    if first_num != 0:
        for number in s[first_num:]:  # Cut the str at first digit
            if (
                number.isnumeric() == False
            ):  # Check if all digits are at the end of the str
                conditions -= 1
                break

    if conditions == 3:  # Check if all conditions are filled
        return True


main()
