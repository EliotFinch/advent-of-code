with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

result_dict = {}
for line in lines:
    card_number = int(line.split()[1][:-1])
    numbers_you_have, winning_numbers = line.split(':')[1].split('|')
    numbers_you_have = {int(number) for number in numbers_you_have.split()}
    winning_numbers = {int(number) for number in winning_numbers.split()}
    result_dict[card_number] = (numbers_you_have, winning_numbers)
    
# Part 1
# ------

points_list = []
for numbers_you_have, winning_numbers in result_dict.values():
    point_numbers = numbers_you_have.intersection(winning_numbers)
    if len(point_numbers) > 0:
        points_list.append(2**(len(point_numbers)-1))
    else:
        points_list.append(0)

print(sum(points_list))

# Part 2
# ------

points_list = []
for numbers_you_have, winning_numbers in result_dict.values():
    points_list.append(len(numbers_you_have.intersection(winning_numbers)))

copies_dict = {i: 1 for i in range(len(points_list))}

for i, points in enumerate(points_list):
    for _ in range(copies_dict[i]):
        for j in range(i+1, i+1+points):
            copies_dict[j] += 1

print(sum(copies_dict.values()))