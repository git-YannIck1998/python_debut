fname = "mbox-short.txt"

fhand = open(fname)
count = 0
for line in fhand :
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 :
        continue
    if words[0] != "From" :
        continue
    print(words[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
