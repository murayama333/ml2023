numbers = ["One", "Two", "Three", "Four", "Five"]
for i, number in enumerate(numbers):
    if i % 2 == 0:
        print(number.upper())
    else:
        print(number.lower())
