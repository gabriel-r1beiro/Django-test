from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'categoria','data_criacao')
    list_display_links = ('nome', 'sobrenome',)
    list_per_page = 10
    search_fields  = ('nome','sobrenome', 'categoria')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
