for i in range(7):  
    
    multiples = [str(i * j) for j in range(i + 1)]
    
    print(' '.join(multiples))
