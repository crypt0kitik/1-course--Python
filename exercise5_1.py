# prints the numbers 1-50 on separate lines using while
counter = 0
while counter <= 49:
    counter = counter + 1
    print(counter)

# prints the numbers 1-50 on separate lines using for
for number in range(50):
    number = number + 1
    print(number)

# loop which sums up all numbers in the range of 1-30. Print ONLY the end result
for x in range(31):
    total = sum(range(31))

print(f"Sum: {total}")

# prints all years between 2005 and 2010 on the same line
text = ""
for year in range(2005, 2011):
    text = text + str(year) + " "
print(text)