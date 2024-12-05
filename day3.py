import re

with open("./data/day3.txt") as f:
    data = f.read()
    matches = re.findall(r"mul\((\d+),(\d+)\)", data)
    numbers = [(int(first), int(second)) for first, second in matches]
    total = 0
    for first, second in numbers:
        total += first * second
    print(total)
    tokens = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)

    enabled = True
    results = []

    for token in tokens:
        if token == "do()":
            enabled = True
        elif token == "don't()":
            enabled = False
        elif token.startswith("mul") and enabled:
            first, second = map(int, re.findall(r"\d+", token))
            results.append((first, second))

    total = 0
    for first, second in results:
        total += first * second
    print(total)