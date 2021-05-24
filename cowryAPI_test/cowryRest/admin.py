from django.contrib import admin

# Register your models here.
from .models import RandomUUID

class RandomUUIDAdmin(admin.ModelAdmin):
    list_display =('cowrytest_name', 'timestamp', 'time')
admin.site.register(RandomUUID, RandomUUIDAdmin)