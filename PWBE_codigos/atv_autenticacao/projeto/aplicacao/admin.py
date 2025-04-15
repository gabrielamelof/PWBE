from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


# Register your models here.

class UsuarioAdmin(UserAdmin):
    # O que vai ser exibido na tela para o usuário 
    list_display = ('biografia', 'idade', 'telefone', 'endereco', 'animais', 'escolaridade')

    # Mostra apenas os atributos passados quando clicacdo
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('biografia', 'idade', 'telefone', 'endereco', 'escolaridade')}),
    )

    # Na criação de um novo uuário, mostra os atributos padrão e os atributos passados no add_fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('biografia', 'idade', 'telefone', 'endereco', 'animais', 'escolaridade')}),
    )


admin.site.register(Usuario, UsuarioAdmin)