from fastapi import FastAPI

app = FastAPI()




endpoints = {
    "schools": {
        1: {
            "school_id": 1,
            "school_name": "Sunrise High School",
            "school_localization": "Gabriela Narutowicza 55b"
        }
    },
    "classes": {
        1: {
            "class_id": 1,
            "school_id": 1,
            "class_name": "Class A",
            "supervising_teacher_id": 10
        }
    },
    "students": {
            1: {
                "student_id": 1,
                "student_name": "John",
                "student_last_name": "Doe",
                "student_age": 16,
                "class_id": 1
            }
    },
    "teachers": {
        1: {
            "teacher_id": 10,
            "teacher_name": "Jane",
            "teacher_last_name": "Smith"
        }
    }
}


@app.get("/schools")
async def read_schools():
    return list(endpoints["schools"].values())


@app.get("/classes")
async def read_classes():
    return list(endpoints["classes"].values())

@app.get("/students")
async def read_students():
    return list(endpoints["students"].values())


@app.get("/teachers")
async def read_teachers():
    return list(endpoints["teachers"].values())

# @app.post("/add_datas")
# async def add_datas(endpoint:str,datas_by_space:str):
#     datas = datas_by_space.split(" ")
#
#     obj = {}
#     for i in datas:
#         obj[i] = i
#     endpoints[endpoint][len(endpoints[endpoint] + 1)] = obj


@app.post("/add_student")
async def add_student(
        studentid: int,
        studentname: str,
        studentlastname: str,
        student_age: int,
        class_id: int
):
    new_student = {
        "student_id": studentid,
        "student_name": studentname,
        "student_last_name": studentlastname,
        "student_age": student_age,
        "class_id": class_id
    }
    endpoints["students"][studentid] = new_student
    return {"message": "Student added successfully", "student": new_student}


@app.post("/add_class")
async def add_class(
        class_id: int,
        school_id: str,
        class_name: str,
        supervising_teacher_id:int
):
    new_class = {
        "class_id": class_id,
        "school_id": school_id,
        "class_name":class_name,
        "supervising_teacher_id":supervising_teacher_id
    }
    endpoints["classes"][class_id] = new_class
    return {"message": "Class added successfully", "class": new_class}



@app.delete("/delete_obj")
async def delete_obj(endpoint: str, obj_id: int):
    try:
        endpoints[endpoint].pop(obj_id)
    except Exception as e:
        return  {"Message": e}


@app.put("/modify_obj")
async def modify_obj(endpoint: str, obj_id: int, string_name: str, new_value: str):
    global endpoints
    try:


        print(endpoints[endpoint][obj_id][string_name],"ksks")
        endpoints[endpoint][obj_id][string_name] = new_value
        return {
            "message": "Object modified successfully.",
            "object": endpoints[endpoint][obj_id]
        }
    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=4444)
