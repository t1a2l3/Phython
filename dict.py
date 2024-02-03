#try:
    def digit_func(number):
        digits={
    "1":"one",
    "2": "two",
    "3": "three",
    "4": "four"

        }
        output=''
        for ch in number:
            output+=digits.get(ch,'!')+" "
        return output

#except ValueError:
    print("incorrect")
    number=int(input('Phone: '))
    print(digit_func(number))


