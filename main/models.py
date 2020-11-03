from django.db import models
from django.contrib.auth.models import User


class CompanyInfo(models.Model):

    name_of_company = models.CharField(max_length=30)
    email_of_company = models.CharField(max_length=30, unique=True)
    password_of_company=models.CharField(max_length=20)
    activation_code=models.CharField(max_length=30)

    def __str__(self):
        return self.email_of_company
