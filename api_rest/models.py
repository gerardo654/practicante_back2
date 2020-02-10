from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200,blank=False)
    last_name = models.CharField(max_length=200,blank=False)
    username = models.CharField(max_length=200,blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=200,blank=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['first_name']

    def __str__(self):
        return self.first_name
