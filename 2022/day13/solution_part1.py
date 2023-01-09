with open('input.txt') as f:
    pairs = [line.split('\n') for line in f.read().split('\n\n')]
    
def compare(l1, l2):
    
    for i in range(len(l1)):
        
        e1 = l1[i]
        try:
            e2 = l2[i]
        except:
            # Right side ran out of items, so inputs are not in the right order
            print('Right side ran out of items, so inputs are not in the right order')
            return 0
        
        print(f'Comparing {e1} and {e2}')
        
        if (type(e1) == int) & (type(e2) == int):
            if e1 < e2:
                print(f'{e1} < {e2}: right order')
                return 1
            elif e1 > e2:
                print(f'{e1} > {e2}: wrong order')
                return 0
            else:
                pass
            
        if (type(e1) == list) & (type(e2) == list):
            result = compare(e1, e2)
            if result == 1:
                return 1
            elif result == 0:
                return 0
        
        if (type(e1) == int) & (type(e2) == list):
            e1 = [e1]
            result = compare(e1, e2)
            if result == 1:
                return 1
            elif result == 0:
                return 0
            
        if (type(e1) == list) & (type(e2) == int):
            e2 = [e2]
            result = compare(e1, e2)
            if result == 1:
                return 1
            elif result == 0:
                return 0
    
    if len(l1) == len(l2):
        pass
    else:
        # Left side ran out of items, so inputs are in the right order
        print('Left side ran out of items, so inputs are in the right order')
        return 1
    
indices = []
for i, pair in enumerate(pairs):
    
    print(i)

    l1 = eval(pair[0])
    l2 = eval(pair[1])
    
    if compare(l1, l2):
        indices.append(i+1)

print('')
print(sum(indices))