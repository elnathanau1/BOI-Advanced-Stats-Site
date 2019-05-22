from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(primary_key = True, max_length = 50)

    class Meta:
        db_table = 'users'
        managed = True

    def __str__(self):
        return (self.name)
