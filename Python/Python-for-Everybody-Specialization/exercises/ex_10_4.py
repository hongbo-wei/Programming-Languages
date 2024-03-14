name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        time = words[5].split(':')
        h = time[0]
        counts[h] = counts.get(h, 0) + 1

for k,v in sorted(counts.items()):
    print(k,v)

# The upper for-loop code prints out the same thing with less code.
# lst = list()
# for k,v in counts.items():
#     newtup = (k,v)
#     lst.append(newtup)
# lst = sorted(lst)
# for k,v in lst:
#     print(k,v)


