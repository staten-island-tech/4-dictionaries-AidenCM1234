def casino (x,a,b,c):
    y=0
    x+=1
    while not x<=1:
        y+=1
        a+=1
        if a == 35:
            x+=30
            a=0
        x-=1
        print(x)
        y+=1
        b+=1
        if b == 100:
            x+=60
            b=0
        x-=1
        print(x)
        y+=1
        c+=1
        if c == 10:
            x=x+9
            c=0
        x-=1
        print(x)
    print(f"Martha plays {y} times before going broke")
casino(77,4,9,3)
#casino(48,3,10,4)