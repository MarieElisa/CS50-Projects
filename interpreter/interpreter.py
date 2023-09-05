expression = input("Arithmetic Expression: ").strip()
x, y, z = expression.split(" ")
x, z = float(x), float(z)

match y:
    case "+":
        w = x + z
    case "-":
        w = x - z
    case "*":
        w = x * z
    case "/":
        w = x / z

print(f"{w:.1f}")
