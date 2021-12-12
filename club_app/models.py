from django.db import models
from django.contrib.auth.models import UserManager
import datetime
from datetime import timedelta
from datetime import datetime




def default_start_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)

# Create your models here.
class Registered_User(models.Model):
    objects =  UserManager()
    User_id = models.AutoField( primary_key=True)
    firstname=models.CharField(max_length=50)
    password =models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    Member_Availed = models.CharField(max_length=50,null=True)
    Membership_Start_time =models.DateField(default=default_start_time)
    Membership_End_time =models.DateField(default=default_start_time)
    Applied_event=models.CharField(max_length=50)
    


class Manager(models.Model):
    id = models.CharField(primary_key=True,max_length=4)
    firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Phone_No =models.CharField(max_length=12)
    password =models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)





class Reservation(models.Model):
    Court_Types = models.CharField(max_length=50)
    Court_Person = models.CharField(max_length=50)
    Court_Id =models.IntegerField()
    Date =models.DateField()
    Start_Time= models.TimeField()
    End_Time= models.TimeField()
    payment=models.IntegerField(default=0)
    Reserved_person = models.CharField(max_length=50,default=None)
    Reserved=models.BooleanField()

class feedback(models.Model):
    user_email=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    rating1 =models.IntegerField()
    rating2 = models.IntegerField()
    rating = models.CharField(max_length=50)
    commentText =models.CharField(max_length=100)

class events(models.Model):
    Name=models.CharField(max_length=50)
    Description=models.CharField(max_length=100)
    Appling_Fee = models.IntegerField(default=0)
    Date=models.DateField(default=datetime.now)
    image = models.ImageField(upload_to='club_app/images', default="")



class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class Payment(models.Model):
    email=models.CharField(max_length=50)
    reser_id=models.IntegerField()
    original_amount =models.IntegerField()
    paid_amount=models.IntegerField(default=0)
    Date=models.DateField(default=datetime.now)
    

