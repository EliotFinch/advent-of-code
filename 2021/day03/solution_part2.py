with open('input.txt') as f:
    data = [entry.rstrip() for entry in f.readlines()]
    
n_bits = len(data[0])
    
def find_most_common(data, bit_number):
    n_entries = len(data)
    count = 0
    
    for entry in data:
        count += int(entry[bit_number])
        
    # print(count)
        
    if count >= n_entries/2:
        return 1
    else:
        return 0

# Find oxygen generator rating
# ============================

O_list = data.copy()

for bit_number in range(n_bits):
    most_common = find_most_common(O_list, bit_number)
    O_list = [entry for entry in O_list if int(entry[bit_number]) == most_common]
    if len(O_list) == 1:
        break
                
# Find C02 scrubber rating
# ========================

C02_list = data.copy()

for bit_number in range(n_bits):
    least_common = 1-find_most_common(C02_list, bit_number)
    C02_list = [entry for entry in C02_list if int(entry[bit_number]) == least_common]
    if len(C02_list) == 1:
        break
                
print(f'Oxygen generator rating = {O_list}')
print(f'C02 scrubber rating = {C02_list}')

print(int(O_list[0], 2) * int(C02_list[0], 2))