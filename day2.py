with open("./data/day2.txt") as f:
    data = f.read()
    reports = []
    for line in data.split("\n"):
        line_l = []
        for l in line.split("\n"):
            for j in l.split("\n"):
                for k in j.split():
                    line_l.append(int(k))
        reports.append(line_l)

    safe = 0
    for r in reports:
        s = False
        increasing = False
        decreasing = False
        diff = 0
        for i in range(len(r)-1):
            if r[i + 1] - r[i]:
                a = abs(r[i + 1] - r[i])
                if a > diff:
                    diff += a
            elif r[i + 1] + r[1]:
                a = abs(r[i + 1] - r[i])
                if a > diff:
                    diff += a
            if r[i+1] > r[i]:
                increasing = True
            elif r[i+1] < r[i]:
                decreasing = True
        if diff < 3 and increasing is True and decreasing is False:
            safe += 1
            s = True
        elif diff < 3 and increasing is False and decreasing is True:
            safe += 1
            s = True

    print(safe)



