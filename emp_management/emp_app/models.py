from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        """__str__."""
        return  str(self.name) 
    
class Role(models.Model):
    role_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        """__str__."""
        return  str(self.role_name)    
    
class Employee(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    hired_date = models.DateField()
    
    def __str__(self):
        """__str__."""
        return str(self.first_name) + " || " + str(self.last_name) + " || " + str(self.role)