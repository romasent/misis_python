a = input('a: ')
if a.count(',') > 0:
    a = float(str(a).replace(',','.'))
else:
    a = float(a)

b = input('b: ')
if b.count(',') > 0:
    b = float(str(b).replace(',','.'))
else:
    b = float(b)
print('sum=' + str(a+b), ';', 'avg=', round((a+b)/2,2))