fio = input('ФИО: ').strip()
up = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
ini = ""

for i in range(len(fio)):
    if fio[i] in up:
        ini += fio[i] + "."

print('Инициалы:', ini)
print('Длина (символов):', len(" ".join(fio.split())))
