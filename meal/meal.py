def main():
    meal_time = input("What time is it? ")

    if meal_time.endswith("p.m."):
        meal_time = convert(meal_time.removesuffix("p.m."))
        if 0 <= meal_time <= 1:
            print("Lunch time")
        elif 6 <= meal_time <= 7:
            print("Dinner time")

    else:
        meal_time = convert(meal_time)
        if 7 <= meal_time <= 8:
            print("Breakfast time")
        elif 12 <= meal_time <= 13:
            print("Lunch time")
        elif 18 <= meal_time <= 19:
            print("Dinner time")


def convert(time):
    h, m = time.split(":")
    time = float(h) + float(m) / 60
    return time


if __name__ == "__main__":
    main()
