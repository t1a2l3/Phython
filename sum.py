num=int(input('enter a number: '))
r=0
s=0
while(num!=0):
    r=num%10
    s=s+r
    num=num//10
print(s)
    