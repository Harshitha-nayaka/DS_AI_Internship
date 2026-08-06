def multiplication_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n}*{i}={n * i}")

try:
    number = int(input("Enter a number: ").strip())
    length = int(input("Enter table length: ").strip())
    multiplication_table(number, length)
except ValueError:
    print("Please enter a valid integer.")