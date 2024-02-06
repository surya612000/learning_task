from fastapi import  FastAPI,Depends
from database import  engine,get_db
# from routers import Customer,Customer_refer,Product,Productvariations,Order,Orderitems,login
import models
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


app=FastAPI()

@app.get("/users")
def get_user(id:int):
    return {"id":id}

@app.get("/users/{id}")
def create_user(id:int,db:Session=Depends(get_db)):
    db_user=db.query(models.Student).filter(models.Student.id==id).first()
    return db_user