from django.db import models

# Create your models here.


class Contact(models.Model):

    name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    message = models.TextField(max_length=700, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + '___' + self.subject
