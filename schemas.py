from pydantic import BaseModel

class createUser(BaseModel):
    name:str

class student_out(BaseModel):
    id:int
    name:str

class Course_create(BaseModel):
    name:str

class Course_out(BaseModel):
    id:int
    name:str