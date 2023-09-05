def main():
    fuel = get_percent("Fraction: ")


def get_percent(prompt):
    while True:
        try:
            fraction = input(prompt)
            num, den = fraction.split("/")
            percent = (100 * int(num)) / int(den)
        except (ValueError, ZeroDivisionError):
            True
        else:
            return get_fuel(percent)


def get_fuel(x):
    if 99 <= x <= 100:
        print("F")
    elif 1 < x < 99:
        print(f"{round(x)}%")
    elif x <= 1:
        print("E")
    else:
        main()


main()
