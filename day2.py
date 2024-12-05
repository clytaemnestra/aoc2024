with open("./data/day2.txt") as f:
    data = f.read()
    reports = []
    for line in data.split("\n"):
        line_l = []
        for k in line.split():
            line_l.append(int(k))
        reports.append(line_l)

    safe = 0
    for r in reports:
        increasing = False
        decreasing = False
        diff = False
        for i in range(0, len(r)-1):
            if r[i + 1] < r[i] or r[i + 1] > r[i]:
                if abs(r[i + 1] - r[i]) > 3:
                    diff = True
            if r[i+1] > r[i]:
                increasing = True
            elif r[i+1] < r[i]:
                decreasing = True
            else:
                increasing = True
                decreasing = True
        if diff is False:
            if increasing and not decreasing or decreasing and not increasing:
                safe += 1

    print(safe)

    safe = 0
    for r in reports:
        for j in range(len(r)):
            new_list = r[:j] + r[j + 1:]
            increasing = False
            decreasing = False
            diff = False
            for i in range(0, len(new_list)-1):
                if new_list[i + 1] < new_list[i] or new_list[i + 1] > new_list[i]:
                    if abs(new_list[i + 1] - new_list[i]) > 3:
                        diff = True
                if new_list[i+1] > new_list[i]:
                    increasing = True
                elif new_list[i+1] < new_list[i]:
                    decreasing = True
                else:
                    increasing = True
                    decreasing = True
            if diff is False:
                if increasing and not decreasing or decreasing and not increasing:
                    safe += 1
                    break

    print(safe)