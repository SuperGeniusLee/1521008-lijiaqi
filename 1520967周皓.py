def move(n,a,b,c):
    if n==1:
        print('将%s上的%s从%s->%s'%(a,n,a,c))
    else:
        move(n-1,a,c,b)     
        print('将%s上的%s从%s->%s'%(a,n,a,c)) 
        move(n-1,b,a,c) 
