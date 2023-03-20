text = "X-DSPAM-Confidence:    0.8475"
num = text.find(':')
print(num)
ntext = text[num + 1:]
print(ntext)
fnum = float(ntext)
print(fnum)
