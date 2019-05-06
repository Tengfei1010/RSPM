from mongoengine import (connect)

from rspm.constants import DataBase


mdb = connect(
    db=DataBase.DBNAME,
    host=DataBase.HOST,
    port=DataBase.PORT
)
