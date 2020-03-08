from django.contrib import admin
from .models import Resposta

class RespostaAdmin(admin.ModelAdmin):
    list_display = ('pergunta', 'resp_texto')

admin.site.register(Resposta, RespostaAdmin)
