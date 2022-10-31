# ask data from user
work_hour = input("How many hours you worked? \n")
work_hour = float(work_hour)
hour_wage = input("What is your salary for 1 hour? \n")
hour_wage = float(hour_wage)

# checking if there is overtime; and if yes, add them to the summary
if work_hour > 40:
    overtime_hours = work_hour - 40
    weekly_wage = hour_wage * 40 + (overtime_hours * hour_wage * 1.5)
    weekly_wage = round(weekly_wage, 2)
    print(f"Your weekly wage is {weekly_wage} euro")
else:
    weekly_wage = hour_wage * work_hour
    weekly_wage = round(weekly_wage, 2)
    print(f"Your weekly wage is {weekly_wage} euro")