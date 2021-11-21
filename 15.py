rows = 14
print "*" * rows, "\n"
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print "*" * i,;
        print "_" * j,;
        print "*" * i,"\n"
        i = i - 1
        j = j + 2
