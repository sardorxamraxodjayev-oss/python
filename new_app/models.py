from django.db import models
from django.contrib.auth.models import User

# class admin(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.IntegerField()
#     contains_sugar = models.BooleanField()
#     image = models.ImageField()


class ariza(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kimga = models.CharField(max_length= 211)
    qisqacha_shikoyat_matni = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




# class authentificate (models.Model):
#     username = models.CharField(max_length= 255)
#     email = models.CharField(max_length=244)
#     pasword = models.CharField()
#     pasword2 = models.CharField()



# class login (models.Model):
#     username = models.CharField()
#     login = models.CharField()




