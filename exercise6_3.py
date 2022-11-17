# task: application allows the user to calculate statistics
# based on exam results by students

# importing the statistics module
from statistics import median

# ask how many students
students = input("How many students?\n")
students = int(students)

summary = 0
new_list = []
# ask to input grade
for x in range(students):
    grade = input("Student grade:\n")
    grade = float(grade)
    new_list.append(grade)


# calculate average, round and print it
average = sum(new_list) / len(new_list)
average = round(average, 2)
print(f"Average grade: {average}")

# print a text description of the average
if 0 <= average < 1:
    print("Bad result")
elif 1 <= average < 2:
    print("Weak result")
elif 2 <= average < 3:
    print("Average result")
elif 3 <= average < 4:
    print("Good result")
elif 4 <= average < 5:
    print("Excellent result")

# Calculate and print the median value of grades
print(f"Median value: {median(new_list)}")

# calculate the most common grade
def most_common(new_list):
    return max(set(new_list), key=new_list.count)
# print the most common grade
print(f"The most common grade: {most_common(new_list)}")