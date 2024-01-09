import database as db


r1 = db.new_employee("Timur Shagimardanov", "1966-01-12", "developer", 1500050)
r2 = db.new_employee("Almat Utenov", "1975-03-11", "developer", 1700070)
r3 = db.new_employee("Aleksandr Nezhelsky", "2001-03-17", "CTO", 2500800)
r4 = db.new_employee("Saniya Becktasova", "2005-01-01", "CEO", 5000050)
r5 = db.new_employee("Arhyn Lyckerov", "1995-11-28", "consultant", 1700070)

# r5 = db.fire_employee(4)
print(db.get_employee_id("Almat"))

# print(database)

fired_list = db.getEmployeeList(lambda x: x['firedDate'] != '')
print(f'Fired employees: {fired_list}')

rich_list = db.getEmployeeList(lambda x: x['salary'] >= 5000)
salaries = [x['salary'] for x in rich_list]
print(f'Best_salaries: {salaries}')