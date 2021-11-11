from django.contrib import admin
from .models import Answer, Question, Game, UserVote, Category, UserPoints

import uuid


# Register your models here.
@admin.register(Answer, Question, UserVote, Category, UserPoints)
class PersonAdmin(admin.ModelAdmin):
    pass


class GameAdmin(admin.ModelAdmin):
    list_display = ('event', 'expiration_date', 'is_active')


admin.site.register(Game, GameAdmin)

