# Assignment 4 - Simple Calculator by Kenisha Randhawa

print("=== SIMPLE CALCULATOR ===")
print("Type 'quit' to exit\n")

while True:
    user_input = input("→ Enter calculation (e.g. 5 + 3): ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    parts = user_input.split()
    if len(parts) != 3:
        print("Error: Type like this → 10 + 5\n")
        continue

    try:
        n1 = float(parts[0])
        op = parts[1]
        n2 = float(parts[2])
    except:
        print("Error: Please use numbers only!\n")
        continue

    if op == "+":
        print(f"Result = {n1 + n2}\n")
    elif op == "-":
        print(f"Result = {n1 - n2}\n")
    elif op == "*":
        print(f"Result = {n1 * n2}\n")
    elif op == "/":
        if n2 == 0:
            print("Error: Cannot divide by zero!\n")
        else:
            print(f"Result = {n1 / n2}\n")
    else:
        print("Error: Use only + - * /\n")