from django.contrib import admin
from .models import Receita
# Register your models here.


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'pessoa', 'publicada',)
    list_editable = ('publicada',)
    list_display_links = ('nome_receita',)
    search_fields = ('nome_receita', 'ingredientes',)
    list_filter = ('categoria',)
    list_per_page = 25

admin.site.register(Receita, ListandoReceitas)
