def move(n,a,b,c):
    #a,b,c分别是三根柱子，n为套在a柱上的圆圈个数
    if n==1:
        print(a,'-->',c)
        return
    move(n-1,a,c,b)
    move(1,a,b,c)
    move(n-1,b,a,c)
    move(3,'A','B','C')  
