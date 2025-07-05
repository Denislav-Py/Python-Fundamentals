# Write a program that keeps the information about companies and their employees.
#
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
#
# Print the company name and each employee's id in the following format:
#
# "{company_name}
#
# -- {id1}
#
# -- {id2}
#
# …
#
# -- {idN}"

company_details = {}

while True:
    command = input()
    if command == "End":
        break
    company, employee_id = command.split(" -> ")
    if company not in company_details.keys():
        company_details[company] = []

    if employee_id not in company_details[company]:
        company_details[company].append(employee_id)

for company in company_details.keys():
    print(f"{company}")
    for employee in company_details[company]:
        print(f"-- {employee}")
