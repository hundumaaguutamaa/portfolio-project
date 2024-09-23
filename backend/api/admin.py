from django.contrib import admin
from .models import ExpertiseArea, ITTeam, RequestService, UserRequest

# Register your models to manage through admin interface.
admin.site.register(ExpertiseArea)
admin.site.register(ITTeam)
admin.site.register(RequestService)
admin.site.register(UserRequest)

