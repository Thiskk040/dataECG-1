def f(n):
    if(n>0):
        f(n-1)
        print(n+"")
        f(n-1)

ans  = f(4)
print(ans)