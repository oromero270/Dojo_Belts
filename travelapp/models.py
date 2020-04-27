from django.db import models
import re
import bcrypt


class usermanager (models.Manager):
    # This is for my landing page validation on the register side
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = " Name should be at least 3 characters"
        if len(postData['uname']) < 3:
            errors["uname"] = "Username should be at least 3 characters"
        if len(postData['pw']) < 8:
            errors["pw"] = "Password should be at least 8 characters"
        if postData['pw'] != postData ['cpw']:
            errors["confirm"] = "Password and confirm password must match"
        return errors

    def login_validator(self,postData):
        errors = {}
        if len( postData ['uname'] )< 1:
            errors['uname'] = 'Username is required'
        activenames = users.objects.filter(username=postData['uname'])
        if len (activenames) ==0:
            errors['usernotfound']= 'This user does not seem to be in our database, please register in order to log in.'
        else:
            user=activenames[0]
            if not bcrypt.checkpw(postData['pw'].encode(),user.password.encode()):
                errors['pw']='Wrong password'
        if len(postData['pw']) < 1:
            errors["pw"] = "Password required"
        return errors
class tripManager (models.Manager):

    def newtrip_validator(self,postData):
        errors = {}
        if len( postData ['location'] )< 1:
            errors['location'] = 'location is required'
        if len(postData['info']) < 1:
            errors["info"] = "Information on location is required."
        start=postData['sdate']
        end=postData['edate']
        if end < start:
            errors['date'] = "Check your dates"
        return errors

class users (models.Model):
    first_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = usermanager()

class trips (models.Model):
    destination= models.CharField(max_length=255)
    description= models.CharField(max_length=455)
    startdate = models.DateField()
    enddate = models.DateField()
    uploader =models.ForeignKey(users, related_name='trips_uploaded', on_delete = models.CASCADE)
    attedning=models.ManyToManyField(users, related_name='going')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = tripManager()