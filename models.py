from django.db import models

# Create your models here.
class signupform(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.email

class loginform(models.Model):
    lemail=models.EmailField(max_length=100)
    lpassword=models.CharField(max_length=50)
    def __str__(self):
        return self.lemail
class railway1(models.Model):
    track_length=models.CharField(max_length=4)
    def __str__(self):
        return self.track_length
class tourismm(models.Model):
    yeart=models.CharField(max_length=4)
    def __str__(self):
        return self.yeart
class educationm(models.Model):
    yeare=models.CharField(max_length=4)
    def __str__(self):
        return self.yeare
class fertilizerm(models.Model):
    yeaf=models.CharField(max_length=4)
    def __str__(self):
        return self.yearf


