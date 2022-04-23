n_row = 5

n_space = n_row - 1

for i in range(0,n_row):
    for j in range(0, n_space):
        print(end=" ")

    n_space -= 1
    
    for k in range(0,i+1):
        print(end="* ")

    print("")

    
