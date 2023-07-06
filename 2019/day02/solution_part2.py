for x in range(100):
    for y in range(100):

        with open('input.txt', 'r') as f:
            text = f.read().strip()
            data = [int(i) for i in text.split(',')]
            
        data[1] = x
        data[2] = y
        
        for i in range(len(data)):
            
            i *= 4
            
            if data[i] == 99:
                #print('stopping')
                break
            
            elif data[i] == 1:
                
                a, b, loc = data[i+1], data[i+2], data[i+3]
                
                s = data[a] + data[b]
                data[loc] = s
                
            elif data[i] == 2:
                
                a, b, loc = data[i+1], data[i+2], data[i+3]
                
                s = data[a] * data[b]
                data[loc] = s
                
        if data[0] == 19690720:
            print(x)
            print(y)