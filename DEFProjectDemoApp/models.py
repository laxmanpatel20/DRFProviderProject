from django.db import models

class Department(models.Model):
    DeptName = models.CharField(max_length=50)
    LocationName = models.CharField(max_length=50)

    def __str__(self):
        return self.DeptName

class Country(models.Model):
    CountryName = models.CharField(max_length=50)

    def __str__(self):
        return self.CountryName


class Employee(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    TitleName = models.CharField(max_length=30)
    HasPassport = models.BooleanField()
    Salary = models.IntegerField()
    HireDate = models.DateField()
    Notes = models.CharField(max_length=200)
    Email = models.EmailField(default='',max_length=50)
    PhoneNumber = models.IntegerField()
    Department = models.ForeignKey("Department", default=0, on_delete=models.CASCADE,related_name="Departments")
    Country = models.ForeignKey("Country", default=0, on_delete=models.CASCADE,related_name="Countries")

    def __str__(self):
        return self.FirstName