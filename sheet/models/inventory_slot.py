from django.core import validators
from django.db import models
import enumfields

from . import character, equipment, items


class InventorySlot(models.Model):
    character = models.ForeignKey(character.Character, on_delete=models.CASCADE)
    slot = enumfields.EnumIntegerField(verbose_name='Slot', enum=equipment.Slot)
    quantity = models.IntegerField(default=1, validators=[validators.MinValueValidator(1)])
    item_index = models.IntegerField()

    def item(self) -> equipment.Item:
        return items.get_item(self.slot, self.item_index)
