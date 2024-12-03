with open("./data/day1.txt") as f:
    data = f.read()
    first_l = []
    second_l = []
    for line in data.split("\n"):
        first, second = map(int, line.split())
        first_l.append(first)
        second_l.append(second)

    s = 0
    for i, j in zip(sorted(first_l), sorted(second_l)):
        s += abs(i-j)

    print(s)

    sim = 0
    for i in first_l:
        if i in second_l:
            sim += (i * second_l.count(i))
    print(sim)