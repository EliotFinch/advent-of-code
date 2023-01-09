with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

open_chars = ['(', '[', '{', '<']
close_chars = [')', ']', '}', '>']

illegal_characters = {key: 0 for key in close_chars}
scores_pt1 = {key: score for key, score in zip(close_chars, [3,57,1197,25137])}

corrupted_lines = []

for i, line in enumerate(data):
    opened = []
    for c in line:
        if c in close_chars:
            matching_open = open_chars[close_chars.index(c)]
            if opened[-1] == matching_open:
                opened.pop()
            else:
                illegal_characters[c] += 1
                corrupted_lines.append(i)
                break
        else:
            opened.append(c)
            
score = 0
for key, value in illegal_characters.items():
    score += value*scores_pt1[key]
print(score)

incomplete_lines = [line for i, line in enumerate(data) if i not in corrupted_lines]
completion_strings = []

scores_pt2 = {key: score for key, score in zip(close_chars, [1,2,3,4])}

for line in incomplete_lines:
    opened = []
    for c in line:
        if c in close_chars:
            matching_open = open_chars[close_chars.index(c)]
            opened.pop()
        else:
            opened.append(c)
    completion_strings.append([close_chars[i] for i in [open_chars.index(c) for c in opened[::-1]]])
    
scores = []
for completion_string in completion_strings:
    score = 0
    for c in completion_string:
        score = 5*score + scores_pt2[c]
    scores.append(score)
    
print(sorted(scores)[int(len(scores)/2)])