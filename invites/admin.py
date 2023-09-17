from django.contrib import admin
from .models import Invite

# Register your models here.

class InviteAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'code',
    )

    fields = (
        'email',
    )

    ordering = ('email',)

admin.site.register(Invite, InviteAdmin)