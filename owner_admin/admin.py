from django.contrib import admin
from owner_admin.models import Offers


class OffersAdmin(admin.ModelAdmin):
    list_display = ('offer', 'date_added', 'date', 'price', 'spots_available', 'status')
    search_fields = ('offer', 'description', 'date_added', 'date', 'image', 'price')


admin.site.register(Offers, OffersAdmin)
