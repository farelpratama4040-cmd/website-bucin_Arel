j = 0

for i in range(5):
    j = j + 2
    print ('i = ', i, ', j =', j)
    if j == 6:
        continue
    print ('i will be skipped over if j=6')