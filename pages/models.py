from django.db import models

class Enquiry(models.Model):

    def time_slots():
        times = []
        for idx, val in enumerate(range(18,24)):
            if idx % 2 == 0:
                times.append((f'{val // 2}:00 AM', f'{val // 2}:00 AM'))
            else:
                times.append((f'{val // 2}:30 AM', f'{val // 2}:30 AM'))

        times.extend([('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM')])

        for idx, val in enumerate(range(2,21)):
            if idx % 2 == 0:
                times.append((f'{val // 2}:00 PM', f'{val // 2}:00 PM'))
            else:
                times.append((f'{val // 2}:30 PM', f'{val // 2}:30 PM'))
        return times

    TIME_CHOICES = time_slots()
    GUEST_CHOICES = [(f'{i} guests', f'{i} guests') for i in range(2, 21)]
    
    date = models.DateField()
    time = models.CharField(max_length=8, choices=TIME_CHOICES, default='7:00 PM')
    guests = models.CharField(max_length=12, choices=GUEST_CHOICES, default='2 guests')

    def __str__(self):
        return f'{self.date} - {self.time} - {self.guests}'

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    objects = models.Manager()


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    objects = models.Manager()

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    objects = models.Manager()

class Dietary(models.Model):
    tags = models.CharField(max_length=2)

    def __str__(self):
        return self.tags

    objects = models.Manager()

class MenuItem(models.Model):
    COURSE_CHOICES = [
        ('Starter', 'Starter'),
        ('Main', 'Main'),
        ('Side', 'Side'),
        ('Dessert', 'Dessert')
    ]

    name = models.CharField(max_length=255)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    dietary_tags = models.ManyToManyField(Dietary, blank=True)

    def __str__(self):
        return self.name

    objects = models.Manager()