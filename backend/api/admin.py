from django.contrib import admin
from .models import ITTeam, UserRequest, RequestService

# Register your models to manage through admin interface.

admin.site.register(ITTeam)
admin.site.register(UserRequest)
admin.site.register(RequestService)