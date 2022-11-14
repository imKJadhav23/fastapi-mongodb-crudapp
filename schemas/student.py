#schema helps to serialize and helps
#to convert mongodb json format
#to UI needed json format

def StudentEntity(db_item) -> dict:
    return {
        "id":str(db_item["_id"]),
        "name":db_item["student_name"],
        "email":db_item["student_email"],
        "phone":db_item["student_phone"]
    }

def listOfStudentEntity(db_item_list) -> list:
    list_student_entity=[]
    for item in db_item_list:
        list_student_entity.append(StudentEntity(item))

    return list_student_entity