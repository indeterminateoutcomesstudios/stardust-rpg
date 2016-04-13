from django.contrib import admin

from sheet.models import character

admin.site.register(character.Character)
admin.site.register(character.LevelUp)
