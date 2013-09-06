from django.contrib import admin
from street_faces.core.models import place, place_no_moderator

admin.site.register(place)
admin.site.register(place_no_moderator)
