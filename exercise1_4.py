# Ask minutes, convert them to hours and show the result

total_minutes = input("Give minutes: ")
total_minutes = int(total_minutes)
hours = total_minutes / 60
hours = int(hours)
minutes = total_minutes - (60 * hours)
time = "{}h {}min".format(hours, minutes)
print(time)