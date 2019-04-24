from django.contrib import admin

# Register your models here.

# from . import models
from displayer.models import Algorithm_template


# @admin.site.register(models.Algorithm_template)
class Algorithm_template_Admin(admin.ModelAdmin):
    list_display = ("name","name_en","pattern","category")

admin.site.register(Algorithm_template, Algorithm_template_Admin)