from django.contrib import admin
from .models import Folder
from .forms import AdminMenuForm


@admin.register(Folder)
class MenuAdmin(admin.ModelAdmin):
    form = AdminMenuForm

