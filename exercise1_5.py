# first step is download the package

# import module
from prettytable import PrettyTable

# Specify the Column Names while initializing the Table
myTable = PrettyTable(["First Name", "Year of birth", "Salary", "Tax percentage"])

# Add rows
myTable.add_row(["Matt", "1970", "2000", "22.8"])
myTable.add_row(["Maria", "1980", "2500", "27.7"])
myTable.add_row(["Bob", "1990", "1000", "19.7"])

print(myTable)



