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
        # print('Left side ran out of items, so inputs are in the right order')
        return 1

# Convert pairs to a list of packets
packets = []

for pair in pairs:

    l1 = eval(pair[0])
    l2 = eval(pair[1])
    
    packets.append(l1)
    packets.append(l2)

# Include divider packets
divider_packets = [[[2]], [[6]]]
for packet in divider_packets:
    packets.append(packet)

# Sort
swaps = 1
while swaps > 0:
    
    new_packets = []
    swaps = 0
    
    for i in range(len(packets)-1):
        
        if i == 0:
            p1 = packets[i]
            
        p2 = packets[i+1]
        
        if i == len(packets) - 2:
            if compare(p1,p2):
                new_packets += [p1,p2]
            else:
                swaps += 1
                new_packets += [p2,p1]
            
        else:
            if compare(p1,p2):
                new_packets.append(p1)
                p1 = p2
            else:
                swaps += 1
                new_packets.append(p2)
                
    packets = new_packets
    
decoder_key = 1
for i, packet in enumerate(packets):
    if packet in divider_packets:
        decoder_key *= (1+i)
        
print('')
print(decoder_key)
