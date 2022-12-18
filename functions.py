# print text
def show_personal_info():
    print("Emiliia Zemskova")
    print("Rovaniemi")
    print("Software Developer")


# convert time to seconds
def count_seconds(hours, minutes, seconds):
    result = (hours * 3600) + (minutes * 60) + seconds
    return result


# check if serial number correct
def magazine_serial_check(serial):
    okay = True
    #check dash in the middle
    if serial[4] != "-":
        okay = False

    #remove dash
    serial = serial.replace("-", "")

    # chech number of numbers
    if len(serial) != 8:
        okay = False
    # check if there is a letter
    if any(c.isalpha() for c in serial):
        okay = False
    return okay


# calculator application for three
# different volume calculations
def box_volume(width, height, depth):
    result = width * height * depth
    result = round(result, 2)
    return result


def ball_volume(radius):
    import math
    result = (4 * math.pi * radius ** 3) / 3
    result = round(result, 2)
    return result


def pipe_volume(radius, length):
    import math
    result = math.pi * radius ** 2 * length
    result = round(result, 2)
    return result


# a function to reverse text
def reverse_string(text):
    return text[::-1]


# a function to check if given text was a palindrome
def check_palindrome(text):
    reversed_text = reverse_string(text)
    if text == reversed_text:
        return True
    else:
        return False


#  function prints the title text first,
#  and then print a numbered list
def show_numbered_list(title, people):
    print()
    print(title,": ")
    for i in range(len(people)):
         print(i + 1, ".", people[i])
