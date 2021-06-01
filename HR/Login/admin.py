from django.contrib import admin
from .models import candidate,master_interview,Panel_member

# Register your models here.
admin.site.register(candidate)
admin.site.register(master_interview)
admin.site.register(Panel_member)

