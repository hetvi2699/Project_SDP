from django.db import models
from django.db.models import Model
import datetime
from decimal import Decimal
#from payments.models import BasePayment
# Create your models here.



class Register(models.Model):
    AppId = models.CharField(max_length=12, primary_key=True)
    Name = models.CharField(max_length=50)
    FatherName = models.CharField(max_length=50)
    MotherName = models.CharField(max_length=50)
    DOB = models.DateField()
    Gender = models.CharField(max_length=9)
    Rollno = models.CharField(max_length=8)
    Category = models.CharField(max_length=10)
    PwdStatus = models.CharField(max_length=40)
    Password = models.CharField(max_length=8)
    SecureQue = models.CharField(max_length=500)
    SecureAns = models.CharField(max_length=50)


class Contact(models.Model):
    AppId = models.CharField(max_length=12, primary_key=True)
    Residence = models.CharField(max_length=20)
    Address1 = models.CharField(max_length=100)
    Address2 = models.CharField(max_length=100, default="")
    City = models.CharField(max_length=30)
    District = models.CharField(max_length=30)
    Pincode = models.CharField(max_length=6)
    State = models.CharField(max_length=30)
    Nationality = models.CharField(max_length=25)
    EmailId = models.CharField(max_length=50)
    MobileNo = models.CharField(max_length=12)


class Education(models.Model):
    AppId = models.CharField(max_length=12, primary_key=True)
    TenthStatus = models.CharField(max_length=5)
    TenthYear = models.IntegerField()
    TenthBoard = models.CharField(max_length=10)
    TenthRollNo = models.CharField(max_length=7)
    TenthResultMode = models.CharField(max_length=15)
    TenthResult = models.CharField(max_length=6)
    TwelfthStatus = models.CharField(max_length=5)
    TwelfthYear = models.IntegerField()
    TwelfthBoard = models.CharField(max_length=10)
    TwelfthRollNo = models.CharField(max_length=7)
    TwelfthResultMode = models.CharField(max_length=15)
    TwelfthResult = models.CharField(max_length=6)


class Exam(models.Model):
    AppId = models.CharField(max_length=12, primary_key=True)
    Time = models.DateTimeField()


class Payment(models.Model):
    AppId = models.CharField(
        max_length=12, primary_key=True, default='SOME STRING')
    Fees = models.IntegerField(null=True)
    TxId = models.CharField(max_length=50, null=True)
    DateOfSubmission = models.DateField(null=True)
    DateOfTx = models.DateField(null=True)
		

class Upload(models.Model):
    AppId = models.CharField(max_length=12, primary_key=True)
    Photo = models.ImageField(upload_to='images/', null=True, verbose_name="")
    Signature = models.ImageField(
        upload_to='images/', null=True, verbose_name="")



class Question(models.Model):
    QuestionId = models.CharField(max_length=5, primary_key=True)
    Question = models.CharField(max_length=500)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Answer = models.CharField(max_length=100)


class Result(models.Model):
    AppId = models.CharField(max_length=12, primary_key=True)
    CorrectAns = models.IntegerField()
    IncorrectAns = models.IntegerField()
    Result = models.CharField(max_length=3)
    Rank = models.CharField(max_length=3)

class Admin(models.Model):
    AdminId = models.CharField(max_length=10, primary_key=True)
    Password = models.CharField(max_length=10)
    Name = models.CharField(max_length=20)


class Manager(models.Model):
    ManagerId = models.CharField(max_length=10, primary_key=True)
    Password = models.CharField(max_length=10)
    Name = models.CharField(max_length=20)
