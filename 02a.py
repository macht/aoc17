total = 0

with open('input/2a_input.txt', 'r') as file:
    for line in file:
        low = high = None
        row = line.split()
        for i in row:
            if low is None:
                low = high = int(i)
            else:
                low = min(low, int(i))
                high = max(high, int(i))
        total += high - low

print(total)
