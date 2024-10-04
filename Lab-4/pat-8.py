number = 1 

for i in range(1, 5, 2): 
    print(' ' * ((5 - i) // 2), end='')  
    for j in range(i):  
        print(number, end=' ')
        number += 1
    print()  
