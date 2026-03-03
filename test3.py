names = ['Arjun', 'Sita', 'Kiran']
employees = dict.fromkeys(names, "Probation")
# Result: {'Arjun': 'Probation', 'Sita': 'Probation', 'Kiran': 'Probation'}

print(employees.copy())