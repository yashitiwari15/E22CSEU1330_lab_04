
employees = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000},
]


parameters = {
    "1": "Age",
    "2": "Name",
    "3": "Salary (PM)",
}


choice = input("Choose the sorting parameter (1. Age, 2. Name, 3. Salary): ")


sorted_employees = sorted(employees, key=lambda x: x[parameters[choice]])


for employee in sorted_employees:
    print(employee)
