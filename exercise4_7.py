# TASK: Create an application that converts numbers into words
# and converts words to numbers

# help dictionary for conversion
help_dict = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
	'zero': '0'
}

help_dict_2 = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero',
}


value = True

# make not a list, make a string
# because in this case it will print correctly
result = ''

while value:
    data = input("Write here what you want to convert: \n")
    # need to delete space to consider string as alpha
    if data.replace(' ','').isalpha():
        print("The original text is : " + data)
        # loop for converting
        result = ''.join(help_dict[ele] for ele in data.split())
        # print results
        print("The text in numbers: " + result)
        # break while
        value = False

    # if input is numberes
    elif data.isnumeric():
        value = len(data)
        # check amount of numbers
        if value > 5:
            print(f"Too many characters! You have {value} characters!")
            print("We accept maximum 5. Try again!")
            print()
        elif 1 <= value <= 5:
            print("The original numbers are : " + data)
            # make a loop for conversion
            for ele in data:
                result = result + help_dict_2[ele]
                result = result + ' '
            print("The text in numbers:", result)
            # break while
            value = False
