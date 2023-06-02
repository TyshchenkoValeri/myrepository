import json

with open('group_people.json') as f:
    data = json.load(f)


max_group_id = None
max_female_count = 0

for group in data:
    female_count = 0
    for person in group['people']:
        if person['gender'] == 'Female' and person['year'] > 1977:
            female_count += 1
    if female_count > max_female_count:
        max_group_id = group['id_group']
        max_female_count = female_count

print(max_group_id, max_female_count)


