def schet(maxday):
    i = 1
    sum = 0
    while(i<=maxday):
        numstr = f"{i}"
        if (i >= 10):
            sum += int(numstr[0]) + int(numstr[1])
        else: 
            sum += i

        i += 1
    return sum

year = float(input("Введите год: \n"))
mass = 1,2
strs = f"{year / 4.0}"
if( strs[len(strs)-1] == '0'):
    mass = 31,29,31,30,31,30,31,31,30,31,30,31
else:
    mass = 31,28,31,30,31,30,31,31,30,31,30,31
summa = 0
for month in mass:
    summa += schet(month)
print(f"\n{summa}")