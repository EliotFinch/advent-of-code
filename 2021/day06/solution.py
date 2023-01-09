with open('input.txt') as f:
    ages = [int(age) for age in f.readlines()[0].split(',')]
    
age_dict = {}
for age in range(-1,9):
    age_dict[age] = ages.count(age)
    
days = 256

for _ in range(days):
    
    # Shift all ages down by one
    for age in age_dict.keys():
        if age != 8:
            age_dict[age] = age_dict[age+1]
        else:
            age_dict[8] = 0
    
    # Move all age -1 entries to age 6
    new_fish = age_dict[-1]
    age_dict[-1] = 0
    age_dict[6] += new_fish
    age_dict[8] += new_fish
    
print(sum(list(age_dict.values())))