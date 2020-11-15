from django.contrib import admin

from . import models as mdls

admin.site.register(mdls.Person)