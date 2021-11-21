rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        # display space
        print ' ',;
        j += 1
    k = 1
    while k <= i:
        print '*',;
        k += 1
    print''
    i += 1

i = rows
while i >= 1:
    j = i
    while j <= rows:
        print ' ',;
        j += 1
    k = 1
    while k < i:
        print '*',;
        k += 1
    print('')
    i -= 1
