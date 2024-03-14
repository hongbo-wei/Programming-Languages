# 5-6 Stages of Life
age = 29

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddle'
elif age < 13:
    stage = 'child'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print(f'You are at the {stage} stage of life')