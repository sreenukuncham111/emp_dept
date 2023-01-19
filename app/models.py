from django.db import models

# Create your models here.
class Emp(models.Model):
    e_name=models.CharField(max_length=100)
    deptno=models.IntegerField()

    def __str__(self):
        return self.e_name

class Dept(models.Model):
    no=models.IntegerField()
    d_name=models.CharField(max_length=100)

    def __str__(self):
        return self.d_name

