from django.db import models

NATIONALITY_CHOICES = (
        {'BRAZIL', 'Brasil'},
        {'USA', 'Estados Unidos'},
        {'ESPANHA', 'Espanha'},
        {'CANADA', 'Canadá'}
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES)

    def __str__(self):
        return self.name
    