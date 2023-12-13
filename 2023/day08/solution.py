with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

instructions = lines[0]

node_dict = {}
for line in lines[2:]:
    node, left_right = line.split(' = ')
    left, right = left_right[1:-1].split(', ')
    node_dict[node] = (left, right)

# Part 1
# ------

current_node = 'AAA'
n_steps = 0

while current_node != 'ZZZ':

    instruction = instructions[n_steps%len(instructions)]
    
    if instruction == 'L':
        current_node = node_dict[current_node][0]
    else:
        current_node = node_dict[current_node][1]
    
    n_steps += 1

print(n_steps)

# Part 2
# ------

# Get all nodes that end with an A
current_nodes = []
for node in node_dict:
    if node.endswith('A'):
        current_nodes.append(node)

# It turns out that each of these nodes goes to exactly one node that ends with
# a Z, and it always revisits that node after a fixed number of steps. So we 
# can just find the number of steps it takes to get to a Z node from each A 
# node, and then find the lowest common multiple of those numbers.

# The path length from each A node to a Z node
path_lengths = []

for current_node in current_nodes:
    n_steps = 0
    while not current_node.endswith('Z'):
        instruction = instructions[n_steps%len(instructions)]
        if instruction == 'L':
            current_node = node_dict[current_node][0]
        else:
            current_node = node_dict[current_node][1]
        n_steps += 1
    path_lengths.append(n_steps)

# Find the least common multiple of the path lengths

def prime_factorization(n):
    """Return the prime factorization of a positive integer n as a dictionary
    with prime factors as keys and their counts as values."""

    # Initialize an empty dictionary to store prime factors and their counts
    factors = {}
    
    # Start with the smallest prime factor (2)
    i = 2
    
    # Iterate until the factor is greater than the number
    while i <= n:

        # Check if the current factor divides the number
        if n % i == 0:
            # If the factor is not in the dictionary, add it with a count of 1
            if i not in factors:
                factors[i] = 1
            else:
                # If the factor is already in the dictionary, increment its 
                # count
                factors[i] += 1
            
            # Divide the number by the factor
            n /= i

        else:
            # If the current factor does not divide the number, move to the 
            # next one
            i += 1
    
    # Return the dictionary containing prime factors and their counts
    return factors

def find_lcm(numbers):
    """Return the least common multiple of a list of positive integers."""

    # Get the prime factors with the greatest exponents for each number
    lcm_factors = {}
    for number in numbers:
        factors = prime_factorization(number)
        for factor, count in factors.items():
            if factor not in lcm_factors or count > lcm_factors[factor]:
                lcm_factors[factor] = count

    # Multiply the factors to get the least common multiple
    lcm = 1
    for factor, count in lcm_factors.items():
        lcm *= factor**count

    return lcm

print(find_lcm(path_lengths))