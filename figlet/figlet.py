from pyfiglet import Figlet
import random
import sys


def main():
    while True:
        try:
            if sys.argv[1] == ("-f" or "--font") and sys.argv[2] in Figlet().getFonts():
                word = input("Input:")
                font = Figlet(font=sys.argv[2])
                print(f"Output: \n{font.renderText(word)}")
                break
            else:
                sys.exit("Invalid usage")
        except IndexError:
            font = random.choice(FigletFont.getFonts())
            word = input("Input:")
            print(f"Output: \n{font.renderText(word)}")
            break

main()
