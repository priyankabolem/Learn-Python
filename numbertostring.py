digittoword = {
    "0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
}

def numbertostringconv(number) :
    number_string = str(number)
    digittostr = [digittoword[digit] for digit in number_string]
    return ' ' .join(digittostr)

inputnum = input("Please enter your number : " )
result = numbertostringconv(inputnum)
print("Your output is : ", result)