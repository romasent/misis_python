min = int(input('Минуты: '))
hours = 0
minos = 0
while min > 60:
    hours += 1
    min -= 60
print(str(hours) + ':' + str(min))