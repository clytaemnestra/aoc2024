from itertools import product

with open("./data/day7.txt") as f:
    data = f.read().strip().splitlines()
    nums = {}
    for line in data:
        first, rest = line.split(":", 1)
        nums[int(first)] = list(map(int, rest.split()))

    operators = ['+', '*', '||']
    sum = 0
    for k, v in nums.items():
        all_combinations = product(operators, repeat=len(v)-1)
        found = False
        for combination in all_combinations:

            result = v[0]
            expression = f"{v[0]}"

            for i in range(len(combination)):
                operator = combination[i]
                number = v[i + 1]

                if operator == '+':
                    result += number
                elif operator == '*':
                    result *= number
                elif operator == '||':
                    result = int(str(result) + str(number))

                expression += f" {operator} {number}"

            if result == k:
                sum += k
                found = True
                break

            if found:
                break

print(sum)




