from fastapi import  FastAPI,Depends
from database import  engine,get_db
# from routers import Customer,Customer_refer,Product,Productvariations,Order,Orderitems,login
import models,schemas
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


app=FastAPI()

@app.get("/users")
def get_user(id:int):
    return {"id":id}

@app.get("/users/{id}")
def get_user(id:int,db:Session=Depends(get_db)):
    db_user=db.query(models.Student).filter(models.Student.id==id).first()
    return db_user

@app.post("/users_create/")
def create_user(request:schemas.createUser,db:Session=Depends(get_db)):
    db_student=models.Student(**request.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"detail":"student is successfully inserted","student_detail":db_student}