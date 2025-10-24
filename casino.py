def casino (x,a,b,c):
    y=0

    z=False
    while z==False :
        x-=1
        a+=1
        if x <= 0:
            z =True
        if a == 35:
            x+=30
            a=0
        y+=1
        x-=1
        b+=1
        if x <= 0:
            z =True
        if b == 100:
            x+=60
            b=0
        y+=1
        x-=1
        c+=1
        if x <= 0:
            z =True
        if c == 10:
            x=x+9
            c=0
        y+=1
        if x <= -1:
            y-=1
    print(f"Martha plays {y} times before going broke")
casino(77,4,9,3)