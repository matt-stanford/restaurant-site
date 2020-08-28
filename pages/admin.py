from django.contrib import admin
from .models import Enquiry, Customer, Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date', 'time', 'guests']
    list_display_links = ['customer', ]
    list_editable = ['date', 'time', 'guests']

admin.site.register(Enquiry)
admin.site.register(Customer)
admin.site.register(Reservation, ReservationAdmin)
