# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        line = line.rstrip()
        count = count + 1
        ntext = line.find(":")
        num = line[ntext + 1:]
        fnum = float(num)
        total = total + fnum
    #print(add/count)
print("Average spam confidence:", total/count)
