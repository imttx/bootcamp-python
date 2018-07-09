total, num = 0, 1

while num <= 100:
    total += num
    num += 1
else:
    print('1+2+3+...+100 = ', total)


aa = 1
while aa < 3:
    print('aa is: ', aa)
    aa += 1
else:
    print('while end')


# aa = True

# while aa: print('test code')


num = 1 

while num < 10:
    if num == 6:
        break
    print('num is:', num)
    num += 1


l = [1,2,3]
for x in l:
    print(x, end='\t')
else:
    print('for end')

while True:
    pass

for x in [1,2]:
    pass

print('end')