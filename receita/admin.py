from django.contrib import admin
from .models import Receita
# Register your models here.


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('nome_receita', 'slug', 'categoria', 'pessoa', 'publicada',)
    prepopulated_fields = {"slug": ("nome_receita", )}
    list_editable = ('publicada',)
    list_display_links = ('nome_receita',)
    search_fields = ('nome_receita', 'ingredientes',)
    list_filter = ('categoria',)
    list_per_page = 25

admin.site.register(Receita, ListandoReceitas)
