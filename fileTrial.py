fname = input('Enter file name: ')
try:
    fhand = open(fname, 'r')
except:
    print('File cannot be opened:', fname)
    quit()
rfile = fhand.read()
rfile = rfile.strip()
print(rfile.upper())
