from django.db import models
from django import forms

# Create your models here.
class Account(models.Model):
    account = models.CharField(max_length=200, help_text='Account')
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=200, help_text='Name')
    age = models.CharField(max_length=10, help_text='Age')
    GENDER_CHOICES = (
        ('M')
        ('F')
        ('Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    add = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    open_account_date = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=200)

    def __str__(self)
        return self.name



class Weddinginfo(models.Model):
    groom = models.CharField(max_length=200, help_text='Groom')
    bride = models.CharField(max_length=200, help_text='Bride')
    groom_dad = models.CharField(max_length=200, help_text='Groom Father')
    groom_mom = models.CharField(max_length=200, help_text='Groom Mother')
    bride_dad = models.CharField(max_length=200, help_text='Bride Father')
    bride_mom = models.CharField(max_length=200, help_text='Bride Mother')
    add_restaurant = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    receive_email = models.CharField(max_length=200)
    account =models.ForeignKey(Account, on_delete = models.PROTECT)
    def __class__
        return self.account
    