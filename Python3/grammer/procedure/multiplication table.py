for i in range(1,10):
    for j in range(1,i+1):
        print("%2d*%2d=%2d"%(j,i,j*i),end=' ')
    print(end="\n")
