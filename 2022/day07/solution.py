with open('input.txt') as f:
    terminal_output = [line.strip() for line in f.readlines()]

# Create a "directory sizes" dictionary with keys for every possible file 
# path, in which we store the sum of the file sizes for that directory

current_dir = ''
dir_sizes = {}

for command in terminal_output:
    
    command_split = command.split()
    
    # User input:
    if command_split[0] == '$':
        
        # The user input is either 'cd' or 'ls'. 
        
        # If it is 'cd' then command_split has length 3 - the third element is 
        # a directory name
        
        # If it is 'ls', then the following lines will be files and 
        # directories
        
        # Update the current_dir string
        if command_split[1] == 'cd':
            new_dir = command_split[2]
            
            if new_dir == '..':
                # Remove the last folder in the string
                if current_dir.count('/') == 1:
                    current_dir = '/'
                else:
                    current_dir = current_dir[:-current_dir[::-1].find('/')-1]
                    
            else:
                # Add the new folder to the string
                if current_dir in ['', '/']:
                    current_dir += f'{new_dir}'
                else:
                    current_dir += f'/{new_dir}'
        
        # Initialise the sum of file sizes for this directory
        if command_split[1] == 'ls':
            dir_sizes[current_dir] = 0
    
    # Terminal output:
    else: 
        if command_split[0] != 'dir':
            # Add to the file size associated with this directory
            dir_sizes[current_dir] += int(command_split[0])

# Create a "recursive" version of the dir_sizes dictionary. This has the same 
# keys as dir_sizes (i.e. a key for every file path), but now the file size
# for each directory includes the size of sub-directories.
recursive_dir_sizes = dir_sizes.copy()
for directory in dir_sizes.keys():
    for second_directory in dir_sizes.keys():
        if (directory in second_directory) and (directory != second_directory):
            recursive_dir_sizes[directory] += dir_sizes[second_directory]

# Part 1
# ======

small_size_subset = []
for size in recursive_dir_sizes.values():
    if size <= 100000:
        small_size_subset.append(size)

print(sum(small_size_subset))

# Part 2
# ======

total_space = 70000000
required_space = 30000000

used_space = recursive_dir_sizes['/']
free_space = total_space - used_space

extra_space_needed = required_space - free_space

big_size_subset = []
for size in recursive_dir_sizes.values():
    if size >= extra_space_needed:
        big_size_subset.append(size)

print(sorted(big_size_subset)[0])