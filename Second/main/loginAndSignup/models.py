from django.db import models

# Create your models here.
class user_detail(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return f'${self.username}'