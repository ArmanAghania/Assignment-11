import numpy as np

def generate_rug(n: int):
    
    rug = np.zeros((n,n)) + n//2
    ind = 1
    while ind < n//2:
        for i in range(ind,n-ind):
            for j in range(ind,n-ind): 
                rug[i][j] = n//2 - ind 
        ind += 1
    rug[n//2][n//2] = 0
        

    return rug

print(generate_rug(17))