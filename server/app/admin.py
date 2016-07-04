from django.contrib import admin

from .models import Application, Version

class ApplicationAdmin(admin.ModelAdmin):
    pass

class VersionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Version, VersionAdmin)
