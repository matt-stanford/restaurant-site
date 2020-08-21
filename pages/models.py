from django.db import models

class Enquiry(models.Model):
    TIME_CHOICES = [(f'{i}:00 AM', f'{i}:00 AM') for i in range(9, 12)] + [('12:00 PM', '12:00 PM')] + [(f'{i}:00 PM', f'{i}:00 PM') for i in range(1, 10)]
    GUEST_CHOICES = [(f'{i} guests', f'{i} guests') for i in range(2, 21)]
    
    date = models.DateField()
    time = models.CharField(max_length=8, choices=TIME_CHOICES)
    guests = models.CharField(max_length=12, choices=GUEST_CHOICES)

    def __str__(self):
        return f'{self.date} - {self.time} - {self.guests}'

    objects = models.Manager()
