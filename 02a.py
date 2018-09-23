total = 0

with open('input/02_input.txt', 'r') as file:
    for line in file:
        row = [int(i) for i in line.split()]
        total += max(row) - min(row)

print(total)
