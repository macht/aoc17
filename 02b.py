with open('input/02_input.txt', 'r') as file:
    data = [[int(x) for x in row.split()] for row in file]

print(sum(x//y for r in data for x in r for y in r if x != y and x % y == 0))
