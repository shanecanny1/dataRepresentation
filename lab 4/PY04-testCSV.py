## Lab Week 3 Creating a CSV File ##
## Shane Canny ##
## 28 Oct 2019 ##


import csv
employee_file = open('employee_file.csv', mode='w') ## opening i.e. creating a file named employee_file.csv ##
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) ## writing to the file, identifying the delimiter and the quote character ##
employee_writer.writerow(['John Smith', 'Accounting', 'November']) ## Writing a row into the file ##
employee_writer.writerow(['Erica Meyers', 'IT', 'March']) ## Writing another row to the file ##
employee_writer.writerow(['Shane Canny', 'Shop Keeper', 'April']) ## Writing my own row to the file ##
employee_file.close() ## Closing the file after all entries ##
