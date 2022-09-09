# 3 задача
with open("dz_3.txt") as file:
    a_sum = a_count = 0
    for i in file.readlines():
        i = i.rstrip("\n")
        a_count += 1
        c = int(i[-1])
        a_sum += c
        if c < 3:
            print("Ученик, чья оценка меньше 3-х:", i[:-1])
print("Средний балл по группе:", a_sum / a_count)