# ask salary and tax
salary = input("Your monthly salary: \n")
salary = float(salary)
tax = input("Your tax percentage: \n")
tax = float(tax)

# calculate earnings and taxes, round into two decimals
taxes = salary * (tax / 100)
taxes = round(taxes, 2)
earnings = salary - taxes
earnings = round(earnings, 2)

print(f"Earnings: {earnings} euro")
print(f"Taxes: {taxes} euro")