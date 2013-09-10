from django.contrib import admin
from street_faces.core.models import place_category, place_unchecked, place_checked

admin.site.register(place_category)
admin.site.register(place_unchecked)
admin.site.register(place_checked)
