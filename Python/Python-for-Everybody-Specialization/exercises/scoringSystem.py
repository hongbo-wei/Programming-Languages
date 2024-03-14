score = input("Enter a score between 0.0 and 1.0: ")
try:
    s = float(score)
except:
    print('Wrong Input')
    quit

if s >=0.0 and s <=1.0:
    if s >= 0.9:
        print('A')
    elif s >= 0.8:
        print('B')
    elif s >= 0.7:
        print('C')
    elif s >= 0.6:
        print('D')
    else:
        print('F')
else:
    print('Out of Range')
