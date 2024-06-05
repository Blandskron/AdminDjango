from django.contrib import admin
from .models import Autor, Libro

class LibroAdmin(admin.ModelAdmin):
    list_filter = ('autor', 'fecha')
    search_fields = ['titulo', 'autor__nombre']

admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor)