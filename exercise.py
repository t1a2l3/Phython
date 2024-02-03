weight=int(input("weight:"))
type=input('(L)bs or (K)bss: ')

if type.upper()=='L' :
    convert=weight*0.45
else:
    convert=weight / 0.45
print(convert)
  

