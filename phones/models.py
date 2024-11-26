from django.db import models

class Phone(models.Model):
    brand = models.CharField(max_length=60)
    display = models.IntegerField()
    battery = models.IntegerField()
    price_blr = models.IntegerField()

    def __str__(self):
        return f'{self.brand} | {self.display} | {self.battery}мАч | {self.price_blr}руб'