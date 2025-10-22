def casino (x,a,b,c):
    y=0
    while not x<=0:
        x-=1
        a+=1
        y+=1
        if a == 35:
            x+=30
            a=0
        
        x-=1
        b+=1
        y+=1
        if b == 100:
            x+=60
            b=0
        
        x-=1
        c+=1
        y+=1
        if c == 10:
            x+=9
            c=0
    print(y)
casino(48,3,10,6)