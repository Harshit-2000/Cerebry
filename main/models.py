from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    comment = models.TextField()

    # Each employee can have only one company.
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees', null = True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
