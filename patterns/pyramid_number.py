n_row = 4

n_space = n_row - 1
n_num = 1

for i in range(0,n_row):
    for j in range(0, n_space):
        print(end="  ")

    n_space -= 1
    
    for k in range(0,n_num):
        print(i+1,end=" ")
    n_num += 2

    print("")

    
