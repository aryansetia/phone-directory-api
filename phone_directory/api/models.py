from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255, null=False)
    contact_number = models.CharField(max_length=12, null=False)
    email = models.EmailField(max_length=255, null=True, blank=True) #as it is optional
    is_spam = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MapUserContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.user)+", "+str(self.contact)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=12, null=False, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True) #as it is optional
    is_spam = models.BooleanField(default=False)

    def __str__(self):
        return self.user