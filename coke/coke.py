due = 50
coin = 0

while due > 0:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    if coin in (25, 10, 5):
        due = due - coin

if due <= 0:
    print(f"Change Owed: {abs(due)}")
