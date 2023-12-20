i =5
is_sep = False
while i<20:
    if is_sep:
        print("-", end="")
    else:
        is_sep = True
    print(i, end="")
    i += 2