import re
h = open('RegEx_Sum_1689130.txt')
lst = list()
t = 0

for line in h:
    i = re.findall('[0-9]+', line)
    if len(i) == 0: continue
    for index in range(len(i)):
        n = int(i[index])
        lst.append(n)
        t += 1

total = sum(lst)
print(t, total)
