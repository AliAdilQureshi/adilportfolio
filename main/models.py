from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=1500)
    message_date = models.DateField()
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.name + self.email
