# a = 'HjkLM' zIAfHoqFG
s = input("Введите буквы разного регистра: ")
a='eyuioa'
b='EYUIOA'
d=0
r=0
# w=0
# y=0
for i in s:
    if i in a or i in b:
        d+=1
    else:
        r+=1
print('Всего букв: ',len(s))
print('Гласных: ',d)
print('Согласных: ',r)

y = 0
w = 0
for i in range(1, len(s)):
    # print(s[i - 1], s[i])
    if s[i - 1].islower() and s[i].islower():
        y += 1
    if s[i - 1].isupper() and s[i].isupper():
        w += 1
print('Количество пар верхнего регистра:', w)
print('Количество пар нижнего регистра:', y)








