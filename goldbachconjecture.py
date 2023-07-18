from tools import prime
from tools import even
a=int(input("Enter the range to test:"))
def gdbch(i):
    x = 1
    c=1
    for a in range(1,i+1):

        if even(a):
            for x in range(1,a+1):
                if prime(x):
                    y=a-x
                    if prime(y):
                        print(str(y)+"+"+str(x)+"="+str(a))
                        x=x+1
                        c=c+1
                        break
    if c==0:
        print("Exception found as"+ str(a)+" is not the sum of "+str(x)+" and "+str(y)+" ! ")
    else:
        print("No exception found!")
gdbch(a)
