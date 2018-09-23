with open('input/1a_input.txt', 'r') as file:
    data = file.read()  

data = data.rstrip()    # strip newline char
num_list = list(data)   
sum = 0

for i, v in enumerate(num_list, start=0):
    if i+1 == len(num_list):
        if int(v) == int(num_list[0]):
            sum = sum + int(v)
    elif int(v) == int(num_list[i+1]):
        sum = sum + int(v)

print(sum)
