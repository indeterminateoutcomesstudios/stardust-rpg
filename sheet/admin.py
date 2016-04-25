from django.contrib import admin

from sheet.models import character, level_up

admin.site.register(character.Character)
admin.site.register(character.UnlockedAbility)
admin.site.register(level_up.LevelUp)
