with open('input.txt') as f:
    
    lines = f.readlines()
    rules = {}
    
    for line in lines:
        line = line.strip()
        if '->' in line:
            key, value = line.split(' -> ')
            rules[key] = value
        elif line != '':
            template = line

elements = {}
for element in template:
    if element not in elements.keys():
        elements[element] = 1
    else:
        elements[element] += 1
        
pairs = {}
for i in range(len(template)-1):
    pair = template[i:i+2]
    if pair not in pairs.keys():
        pairs[pair] = 1
    else:
        pairs[pair] += 1
        
steps = 40
for i in range(steps):
    
    new_elements = {}
    new_pairs = {}
    
    for pair in list(pairs.keys()):
        if (pair in rules.keys()) & (pairs[pair] != 0):
            
            new_element = rules[pair]
            if new_element not in new_elements.keys():
                new_elements[new_element] = pairs[pair]
            else:
                new_elements[new_element] += pairs[pair]
            
            new_pair_list = [f'{pair[0]}{new_element}', f'{new_element}{pair[1]}']
            for new_pair in new_pair_list:
                if new_pair not in new_pairs.keys():
                    new_pairs[new_pair] = pairs[pair]
                else:
                    new_pairs[new_pair] += pairs[pair]
                    
            pairs[pair] = 0
            
    for new_element, n in new_elements.items():
        if new_element not in elements.keys():
            elements[new_element] = n
        else:
            elements[new_element] += n
            
    for new_pair, n in new_pairs.items():
        if new_pair not in pairs.keys():
            pairs[new_pair] = n
        else:
            pairs[new_pair] += n
                   
print(max(elements.values()) - min(elements.values()))