hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40:
    total = h * r
else:
    total = (h-40)*r*1.5+40*r
print(total)
