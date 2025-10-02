from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int]=None
    email: EmailStr
    cgpa: float=Field(gt=0, lt=10,default=5, description='cgpa score of the student')

#emailstr ===email validation with pydantic
# data type validation===pydantic
#Field=======constraints with pydantic ---(lt= less than) and (gt= grater-than) and

new_student={'name': 'chandra', 'email':'chandra@gmail.com'}

student=Student(**new_student)

print(type(student))
print("\n",student)

# convert pydantic object to dictionary 
student_dict=student.model_dump()
print(student_dict['age'])


#convert pydantic object to json
student_json=student.model_dump_json()
print(student_json)
