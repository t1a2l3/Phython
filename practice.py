num1=int(input('enter a number: '))
k=0
if num1==0 or num1==1:
    print('num1 is not a prime number')
else:
    i=2
    while(i<num1):
        if num1%i==0:
            k=k+1
        i+=1
    if k==0:
        print(num1,'is a prime number')
    else:
        print('not a prime number ')