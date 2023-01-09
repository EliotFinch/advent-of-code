with open('input.txt') as f:
    data = [entry.rstrip() for entry in f.readlines()]

n_entries = len(data)
n_digits = len(data[0])
counts = [0]*n_digits

for entry in data:
    for i, digit in enumerate(entry):
        counts[i] += int(digit)

most_common_list = [count//int(n_entries/2) for count in counts]

gamma_rate = ''
epsilon_rate = ''

for digit in most_common_list:
    gamma_rate += str(digit)
    epsilon_rate += str(abs(digit-1))
    
print(int(gamma_rate, 2) * int(epsilon_rate, 2))