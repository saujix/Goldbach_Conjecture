def prime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c=c+1

    if c==2:
        status=True
    else:
        status=False
    return status

def even(num):
    if num%2==0:
        status=True
    else:
        status=False
    return status
