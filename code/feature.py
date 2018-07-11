l = list(range(10))

print(l[0:3])

for i,v  in enumerate([1,2,3]):
    print(i, v)


d = {'a':1, 'b':2, 'c':3}

for k in d:
    print(k)

for k, v in enumerate(range(5)):
    print(k, v)

for k, v in enumerate([0,1,2,3,4]):
    print(k, v)