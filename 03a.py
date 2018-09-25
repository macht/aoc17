input_value = 277678

square = next (x for x in range(10000) if input_value <= (sum(8*n for n in range(0, x+1)) + 1))
max_value = sum(8*n for n in range(0, square+1)) + 1
moves = 2*square - (max_value-input_value) % (2*square)
print(moves)
