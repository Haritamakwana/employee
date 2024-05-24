from django.db import models

# Create your models here.
class employee(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=100)
    eemail=models.EmailField(unique=True)
    econtact=models.BigIntegerField()

class Meta:
    db_table="emp"
