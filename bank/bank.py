greeting = input("Greeting: ").strip().casefold()

if greeting.find("hello", 0, 5) == 0:
    print("$0")
elif greeting.find("h", 0, 1) == 0:
    print("$20")
else:
    print("$100")