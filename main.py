from fastapi import  FastAPI
from database import  engine,get_db
# from routers import Customer,Customer_refer,Product,Productvariations,Order,Orderitems,login
import models


models.Base.metadata.create_all(bind=engine)


app=FastAPI()