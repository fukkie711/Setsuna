list_max = [23,45,67,89,98]
max_max = len(list_max)
count = 0

print("残り" + str(max_max))

for x in list_max:
    now = x
    print(now)
    count = count + 1
    print(str(count) + "/" + str(max_max) + "変換終了")
