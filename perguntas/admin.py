from django.contrib import admin
from .models import Pergunta

class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_pergunta')

admin.site.register(Pergunta, PerguntaAdmin)
