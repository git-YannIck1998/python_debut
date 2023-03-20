def computepay(h,r):
    if h > 40.0:
        reg = 40.0 * r
        otp = (h - 40.0) * (r * 1.5)
        p = reg + otp
        return p
    else:
        p = h * r
        return p

nh = input('Enter Hours: ') #45
nr = input('Enter Rate: ') #10.50

fh = float(nh)
fr = float(nr)

xp = computepay(fh,fr)
print('Pay', xp)
