from django.contrib import admin

from sheet.models import character, inventory_slot, level_up, party

admin.site.register(party.Party)
admin.site.register(character.Character)
admin.site.register(character.UnlockedAbility)
admin.site.register(inventory_slot.InventorySlot)
admin.site.register(level_up.LevelUp)
