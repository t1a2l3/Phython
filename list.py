numbers=[5,7,5,4,3,4,5]
unix=[]
for number in numbers:
    if number not in unix:
        unix.append(number)
print(unix)


#numbers = (1,2,3) #tuple not change in list 
cordinates=(1,2,3) #either a list or a tuple
x, y ,z = cordinates # we can also use in tuple or a list
print(x)
