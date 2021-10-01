from django.db import models


class Message(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.date_created.strftime('%Y-%m-%d %H:%M:%S')}"


class Profile(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.title
