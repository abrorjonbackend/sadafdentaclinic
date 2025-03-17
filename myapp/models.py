from django.db import models

class BasePost(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDate = models.DateField()
    address = models.CharField(max_length=255)
    appointmentDate = models.DateField()
    appointmentTime = models.TimeField()
    doctor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    givenPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tel = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        abstract = True  # Bu model faqat meros olish uchun

class GeneralPost(BasePost):
    created_at = models.DateTimeField(auto_now_add=True)

class SardorPost(BasePost):
    created_at = models.DateTimeField(auto_now_add=True)

class ZoirPost(BasePost):
    created_at = models.DateTimeField(auto_now_add=True)

class JasurPost(BasePost):
    created_at = models.DateTimeField(auto_now_add=True)
