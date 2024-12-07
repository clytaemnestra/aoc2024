with open("./data/day5.txt") as f:
    data = f.read().strip().splitlines()
    rules = []
    sequences = []
    for d in data:
        if len(d) == 5:
            split = d.split("|")
            rules.append((int(split[0]), int(split[1])))
        else:
            sequence = [int(i) for i in d.split(',') if i.strip()]
            if sequence:
                sequences.append(sequence)

    safe_sequences = []
    unsafe = []
    for seq in sequences:
        safe = True
        for i in range(len(seq)-1):
            if (seq[i+1], seq[i]) in rules:
                safe = False
                unsafe.append(seq)
                break
        if safe:
            safe_sequences.append(seq)

    sum = 0
    for s in safe_sequences:
        mid = len(s) // 2
        sum += s[mid]

    print(sum)

    for seq in unsafe:
        for j in range(100):
            for i in range(len(seq) - 1):
                if (seq[i + 1], seq[i]) in rules:
                    seq[i], seq[i + 1] = seq[i + 1], seq[i]

    sum = 0
    for s in unsafe:
        mid = len(s) // 2
        sum += s[mid]

    print(sum)
