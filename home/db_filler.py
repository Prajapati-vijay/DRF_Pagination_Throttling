from .models import Student
import random
import datetime


def Db_fill(n):
    for i in range(n):
        st=Student.objects.create(first_name=f"Vijay_{random.randint(1,10)}", last_name="Kumar",date_of_birth=datetime.datetime.now(),email="vijay@gail.com", marks=random.randint(30,100))
