from django.db import models
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

# Create your models here.
class Students(models.Model):
    student_id=models.IntegerField(primary_key=True)
    student_name=models.CharField(max_length=80,null=True)
    email=models.CharField(max_length=80,null=True)
    mobile=models.CharField(max_length=20,null=True)
    data=(('On','On'),('Off', 'Off'),)
    mode=models.CharField(max_length=10,null=True,choices=data)

class Admissions(models.Model):
    # student_id=models.IntegerField()

    cnx = mysql.connector.connect(user='root', password='new123', database='students')
    cursor = cnx.cursor()
    query = "select student_name,student_name from Fees_students order by student_name"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    cnx.close()

    student_name=models.CharField(max_length=80,choices=students)

    cnx = mysql.connector.connect(user='root', password='new123', database='students')
    cursor = cnx.cursor()
    query = "select course,course from Fees_course order by course"
    cursor.execute(query)
    courses = cursor.fetchall()
    cursor.close()
    cnx.close()

    course=models.CharField(max_length=80,choices=courses)

    cnx = mysql.connector.connect(user='root', password='new123', database='students')
    cursor = cnx.cursor()
    query = "select batch_name,batch_name from Fees_batch order by batch_name"
    cursor.execute(query)
    batches = cursor.fetchall()
    cursor.close()
    cnx.close()
    present_batch_name=models.CharField(max_length=30,choices=batches,null=True)
    original_batch_name=models.CharField(max_length=30,choices=batches,null=True)
    standard_Fees=models.IntegerField(default=0)
    fees_allotted=models.IntegerField(default=0)
    fees_received=models.IntegerField(default=0)
    fees_balance=models.IntegerField(default=0)

class Course(models.Model):
    course_id=models.IntegerField(null=True,default=None)
    course=models.CharField(max_length=80,null=True)
    standard_Fees=models.FloatField(null=True)

class Batch(models.Model):
    batch_id=models.IntegerField(primary_key=True)

    cnx = mysql.connector.connect(user='root', password='new123', database='students')
    cursor = cnx.cursor()
    query = "select course,course from Fees_course order by course"
    cursor.execute(query)
    courses = cursor.fetchall()
    cursor.close()
    cnx.close()

    course=models.CharField(max_length=80,null=True,choices=courses)
    batch_name=models.CharField(max_length=80,null=True)
    from_date=models.DateField()
    upto_date=models.DateField()

class Fees(models.Model):
    id=models.IntegerField(primary_key=True)
    cnx = mysql.connector.connect(user='root', password='new123', database='students')
    cursor = cnx.cursor()
    query = "select student_name,student_name from fees_admissions group by student_name"
    cursor.execute(query)
    names = cursor.fetchall()
    cursor.close()
    cnx.close()

    student_name=models.CharField(max_length=80,null=True,default=None,choices=names)
    course=models.CharField(max_length=80,null=True)
    present_batch_name=models.CharField(max_length=50,null=True)
    payment_date=models.DateField()
    amount=models.IntegerField()
    UTR_UPI_No=models.CharField(max_length=50)