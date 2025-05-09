from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomerManager(BaseUserManager):
    def create_user(self, email, company_name, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            company_name=company_name,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=255)
    address = models.TextField(blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["company_name"]

    objects = CustomerManager()

    def __str__(self):
        return f"{self.company_name} ({self.email})"


class Product(models.Model):
    name = models.CharField(max_length=250)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
    )
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    supplier = models.CharField(max_length=250)
