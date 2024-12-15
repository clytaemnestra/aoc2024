stones = [0, 89741, 316108, 7641, 756, 9, 7832357, 91]

for i in range(25):
    result = []
    for s in stones:
        digits = []
        if s == 0:
            result.append(1)
        else:
            s_str = str(s)
            if len(s_str) % 2 == 0:
                mid = len(s_str) // 2
                left = int(s_str[:mid])
                right = int(s_str[mid:])
                result.extend([left, right])
            else:
                result.append(s * 2024)

    stones = result

print(len(stones))

from collections import Counter

stones = [0, 89741, 316108, 7641, 756, 9, 7832357, 91]

stone_counts = Counter(stones)

for i in range(75):
    new_stone_counts = Counter()

    for s, count in stone_counts.items():
        if s == 0:
            new_stone_counts[1] += count
        else:
            s_str = str(s)
            if len(s_str) % 2 == 0:
                mid = len(s_str) // 2
                left = int(s_str[:mid])
                right = int(s_str[mid:])
                new_stone_counts[left] += count
                new_stone_counts[right] += count
            else:
                new_stone_counts[s * 2024] += count

    stone_counts = new_stone_counts
print(sum(stone_counts.values()))
