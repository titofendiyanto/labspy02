a=int (input("bilangan1 = "))
b=int (input("bilangan2 = "))
c=int (input("bilangan3 = "))

if a>b and a>c:
    print ('bilangan1, lebih besar dari bilangan2 dan bilangan3')
elif b>a and b>c:
    print ('bilangan2, lebih besar dari bilangan1 dan bilangan3')
else:
    print ('bilangan3,lebih besar dari bilangan1 dan bilangan2')
