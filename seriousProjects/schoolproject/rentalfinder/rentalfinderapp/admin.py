from django.contrib import admin
from rentalfinderapp.models import Rental, Images


class RentalAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Rental, RentalAdmin)
admin.site.register(Images)
