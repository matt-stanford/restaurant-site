from django.contrib import admin
from .models import Enquiry, Customer, Reservation, Dietary, MenuItem

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date', 'time', 'guests']
    list_editable = ['date', 'time', 'guests']

admin.site.register(Enquiry)
admin.site.register(Customer)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Dietary)
admin.site.register(MenuItem)
