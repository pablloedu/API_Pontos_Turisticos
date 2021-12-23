from django.contrib import admin
from .models import Comentario

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'aprovado')
    list_display_links = ('id','usuario')
    list_editable = ('aprovado',)




admin.site.register(Comentario, ComentarioAdmin)