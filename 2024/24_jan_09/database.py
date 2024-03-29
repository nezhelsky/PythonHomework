database = []

{
    "id": 0,
    "firstName": "",
    "lastName": "",
    "birthDate": "",
    "hiredDate": "",
    "firedDate": "",
    "position": "",
    "salary": 0
}

def new_employee(full_name: str, birth_date: str, position: str, salary: int):
    first_name, last_name = full_name.split(" ", 1)
    if salary <= 0:
        return {"id": -1, "errorDesc": "Salary not correct"}
    if not birth_date:
        return {"id": -1, "errorDesc": "Birthdate not correct"}
    if not position:
        return {"id": -1, "errorDesc": "Position not correct"}
    newcome = {
        "id": len(database),
        "firstName": first_name,
        "lastName": last_name,
        "birthDate": birth_date,
        "hiredDate": "yesterday",
        "firedDate": "",
        "position": position,
        "salary": salary
    }
    database.append(newcome)
    return{"id": newcome["id"], "errorDesc": ""}

def fire_employee(id: int):
    if 0 <= id < len(database):
        database[id]["firedDate"] = "today"
        return {"id": id, "errorDesc": ""}
    return {"id": -1, "errorDesc": "Id not correct"}

def get_employee_id(name: str):
    for n in database:
        if n["firstName"] == name or n["lastName"] == name:
            return n["id"]
    return {-1}


def getEmployeeList(selector):
    result = []
    for record in database:
        if selector(record) == True: # эту строку можно записать так: if selector(record):
            result.append(record)
    return result