nh = input("Enter Hours: ")
nr = input("Enter Rate: ")
try:
    fh = float(nh)
    fr = float(nr)
except:
    print("Error, please enter numerical values.")
    quit()
if fh > 40.0:
    reg = 40 * fr
    otp = (fh - 40.0) * (fr * 1.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:", xp)
