with open('input.txt') as f:
    input_list = f.read().split('\n\n')


class monkey:
    
    def __init__(self, number, items, operation, test):
        
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
    
        self.inspections = 0
        
    def interact(self, item):
        
        self.inspections += 1
        
        return eval(self.operation.replace('old', str(item)))


def create_classes():
    
    monkeys = []
    for i, monkey_input in enumerate(input_list):
        
        # For each monkey we store the number used in the division test, and
        # the monkeys the item is passed onto as 
        # [division number, true monkey, false monkey]
        test = []
        
        lines = [line.strip() for line in monkey_input.splitlines()]
        for line in lines:
            
            if 'Starting' in line:
                items = [int(item) for item in line.split(':')[-1].split(',')]
            
            elif 'Operation' in line:
                operation = line.split(':')[-1].split('=')[-1].strip()
            
            if any(word in line for word in ['Test', 'true', 'false']):
                test.append(int(line.split()[-1]))
            
        monkeys.append(monkey(i, items, operation, test))
        
    return monkeys
    
# Part 1
# ------

monkeys = create_classes()
    
for _ in range(20):
    for m in monkeys:
        for item in m.items:
            worry_level = m.interact(item)//3
            if worry_level%m.test[0] == 0:
                monkeys[m.test[1]].items.append(worry_level)
            else:
                monkeys[m.test[2]].items.append(worry_level)
        m.items = []
        
monkey_business = 1
for i in sorted([m.inspections for m in monkeys])[-2:]:
    monkey_business *= i
    
print(monkey_business)

# Part 2
# ------

monkeys = create_classes()

# We need to avoid large worry values. Modding by the product of all the
# numbers we divide by does the trick...
mod_factor = 1
for m in monkeys:
    mod_factor *= m.test[0]

for _ in range(10000):
    for m in monkeys:
        for item in m.items:
            worry_level = m.interact(item)%mod_factor
            if worry_level%m.test[0] == 0:
                monkeys[m.test[1]].items.append(worry_level)
            else:
                monkeys[m.test[2]].items.append(worry_level)
        m.items = []
        
monkey_business = 1
for i in sorted([m.inspections for m in monkeys])[-2:]:
    monkey_business *= i
    
print(monkey_business)