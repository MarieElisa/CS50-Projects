def main():
    face = input("Smile for me a little: ")
    print(convert(face))

def convert(emozi):
    return emozi.replace(":)", "🙂").replace(":(", "🙁")

main()