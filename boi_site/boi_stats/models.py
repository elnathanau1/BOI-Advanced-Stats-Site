from django.db import models

# Create your models here.
class Run(models.Model):
    user = models.CharField(max_length = 50)
    seed = models.CharField(max_length = 10)

    class Meta:
        db_table = 'runs'
        unique_together = (('user', 'seed'),)
        managed = True

    def __str__(self):
        return (self.user + ", " + self.seed)
