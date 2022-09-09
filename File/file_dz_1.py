a=['5','7']
f=open('input.txt', 'w')
f.write(a[0] + ' '+ a[1])
f.close()

fr= open('output.txt', 'w')
b=int(a[1])-int(a[0])
fr.write(str(b))
fr.close()
