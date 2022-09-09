# # 1 вариант
# import random
# def factorial(a,s,d,f,g,h,j,k,l,r):
#     y=a+s+d+f+g+h+j+k+l+r
#     print([a,s,d,f,g,h,j,k,l,r])
#     return ('Сумма: ',y)
# print(factorial(random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)))

# 2 вариант
import random
a = []
for i in range(11):
    a.append(random.randint(1,101))
def factorial(n, fact, sum=0):
    if n == 1:
        return sum
    sum += fact[n-1]
    return factorial(n-1, fact, sum)
print(factorial(len(a), a))
a.remove(a[0])
print(a)