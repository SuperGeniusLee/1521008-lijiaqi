n = int(input("输入初始化时A塔上盘子的个数n：\n"))  
def move( n , A , B ,C ):     
    if n == 1 :         
        print( "%s is moved to %s" %(A ,C) )  
    else :  
        move( n-1 , A , C , B )     
        move( 1 , A , B , C )  
        move( n-1 , B , A , C )  
move( n ,'A' , 'B' , 'C')     
