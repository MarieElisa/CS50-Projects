dic_groceries = {}


def main():
    while True:
        try:
            item = input().upper()
            if item in dic_groceries:
                count_item(item)
            else:
                dic_groceries[item] = 1
        except EOFError:
            print("")
            for grocery in sorted(dic_groceries):
                print(dic_groceries[grocery], grocery, sep=" ")
            break


def count_item(x):
    dic_groceries[x] += 1


main()
