from django.db import models

class employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=10)
    esalary=models.DecimalField(max_digits=10,decimal_places=2)
    ejoiningdate=models.DateField()
    eclosingdate=models.DateField()