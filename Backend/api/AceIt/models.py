from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
import os
from django.core.validators import MaxValueValidator, MinValueValidator

class Table(models.Model):
    name = models.CharField(max_length = 400)
    user_id = models.ForeignKey("auth.User", on_delete = models.CASCADE)

    def to_dict(self):
        return{
        "table_id": self.id,
        "name":self.name,
        "user_id":self.user_id
        }


class Row(models.Model):
    table_id = models.ForeignKey("Table",on_delete = models.CASCADE)

    def to_dict(self):
        return{
        "row_id": self.id,
        }


class Column(models.Model):
    name = models.CharField(max_length = 400)
    table_id = models.ForeignKey("Table",on_delete = models.CASCADE)

    def to_dict(self):
        return{
        "column_id": self.id,
        "text": self.name,
        }

class Cell(models.Model):
    row_id = models.ForeignKey("Row", on_delete = models.CASCADE)  
    column_id = models.ForeignKey("Column", on_delete = models.CASCADE)
    text = models.CharField(max_length = 400, null=True)

    def getPK(self):
        return (self.column_id,self.row_id)
    
    def to_dict(self):
        return{
        "row_id": self.row_id.to_dict(),
        "text": self.text,
        "column_id": self.column_id.to_dict(),
        }
class Expert(models.Model):
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    rating = models.IntegerField(null = False,validators=(MinValueValidator(0), MaxValueValidator(100)))
    rate = models.IntegerField(null = False)
    name = models.CharField(max_length=100, null = False)
    email = models.EmailField(max_length = 254, null= False)
    experience = models.IntegerField(null = False)
    about_me = models.TextField(null = False)
    profile_picture = models.ImageField(null = True, upload_to = 'assets/Expert_imgs')
    approved = models.BooleanField(default = True)
    linkedIn = models.URLField(max_length=200)

    def to_dict(self):
        return{
            'name': self.name,
            'email': self.email,
            'field': self.field.to_dict(),
            'rating': self.rating,
            'rate': self.rate,
            'about_me': self.about_me,
            'experience': self.experience,
            'profile_picture': os.path.basename(self.profile_picture.name),
            'linkedIn': self.linkedIn
        }
class Field(models.Model):
    name = models.CharField(max_length=100, null = False)

    def to_dict(self):
        return {
            'name':self.name,
            'id': self.id
        }