fname = "mbox-short.txt"
fhand = open(fname)
counts = dict()
lst = list()
for line in fhand :
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 :
        continue
    if words[0] != "From" :
        continue
    lst.append(words[1])
#print(lst)
for word in lst:
    counts[word] = counts.get(word, 0) + 1
#print(counts)
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword, bigcount)
