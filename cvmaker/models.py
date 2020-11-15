from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # city = models.ForeignKey(
    #     City, related_name="clients", on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    webpage = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"