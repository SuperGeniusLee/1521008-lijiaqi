def move(n,l,m,r):
    if n==1:
        print(l,'->',r)
    else:
        move(n-1,l,r,m)
        move(1,l,m,r)
        move(n-1,m,l,r)


