a = int(input("Введите 7-значное число: "))
a = str(a)
b = 0
c = 0
for i in a:
    if int(i) % 2 == 0:
        b+=1
    else:
        c+=1
if b>c:
    p = (int(a[0]))
    v = (int(a[1]))
    g = (int(a[2]))
    q = (int(a[3]))
    m = (int(a[4]))
    w = (int(a[5]))
    e = (int(a[6]))
    print('Чётных больше. Сумма всех цифр: ', (p+v+g+q+m+w+e))
else:
    p=(int(a[0]))
    g=(int(a[2]))
    q=(int(a[3]))
    print('Нечётных больше. Произведение 1,3 и 6 цифры: ', (p*g*q))