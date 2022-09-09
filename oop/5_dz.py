class MyClass:
    a = 'Good day'# public
    s = 7 # public
    f = 5 # public
    _b = s + f # protected
    _d = s * f # protected
    __c = len(a)  # private
    n = ', my friend' # public
    __k = a + n # private
ex = MyClass()
print(ex.a)
print(ex._b)
print(ex._d)
print(ex._MyClass__c)
print(ex.n)
print(ex._MyClass__k)
print(len(ex._MyClass__k))