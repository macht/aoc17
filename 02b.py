total = 0

with open('input/02_input.txt', 'r') as file:
    for line in file:
        row = sorted([int(i) for i in line.split()], key=None, reverse=True)
        for dividend in row:
            mod = [divisor for divisor in row if dividend % divisor == 0 and dividend != divisor]
            if mod:
                total += dividend / mod.pop()
print(total)
