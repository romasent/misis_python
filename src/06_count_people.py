cnt = int(input())
och = 0
zaoch = 0

for _ in range(cnt):  # Исправили n на cnt
    info = input().split()
    last_info = info[-1]
    if last_info == "True":
        och += 1
    else:
        zaoch += 1

print(och, zaoch)