rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print "", ;
        j += 1
    k = i
    while k <= rows - 1:
        print '*',;
        k += 1
    print ""
    i += 1
i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print "",;
        j += 1
    k = i
    while k <= rows - 1:
        print '*', ;
        k += 1
    print ""
    i -= 1
