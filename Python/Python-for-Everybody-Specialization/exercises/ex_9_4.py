name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word, 0) + 1

Maxword = None
Maxcount = None
for word,count in counts.items():
    if Maxcount is None or count > Maxcount:
        Maxcount = count
        Maxword = word
print(Maxword,Maxcount)
