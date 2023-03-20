fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)
time = None
lst = list()
counts = dict()

for line in fhandle :
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 :
        continue
    if words[0] != "From" :
        continue
    time = words[5]
    hours = time.split(":")
    hour = hours[0]
    lst.append(hour)

for h in lst:
    counts[h] = counts.get(h, 0) + 1

for k,v in sorted(counts.items()):
    print(k,v)
