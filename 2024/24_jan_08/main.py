import data_def


r1 = data_def.new_employee("Timur Shagimardanov", "1966-01-12", "developer", 1500050)
r2 = data_def.new_employee("Almat Utenov", "1975-03-11", "developer", 1700070)
r3 = data_def.new_employee("Aleksandr Nezhelsky", "2001-03-17", "CTO", 2500800)
r4 = data_def.new_employee("Saniya Becktasova", "2005-01-01", "CEO", 5000050)
r5 = data_def.new_employee("Arhyn Lyckerov", "1995-11-28", "consultant", 1700070)

# r5 = fire_employee(4)
print(data_def.get_employee_id("Almat"))

# print(database)