with open('input/01_input.txt', 'r') as file:
    data = file.read()  

data = data.rstrip()    # strip newline char
num_list = list(data)   
sum = 0
j = int(len(num_list) / 2)

for i, v in enumerate(num_list, start=0):
    if i+1 > j:
        if int(v) == int(num_list[i%j]):
            sum = sum + int(v)
    elif int(v) == int(num_list[i+j]):
        sum = sum + int(v)

print(sum)
