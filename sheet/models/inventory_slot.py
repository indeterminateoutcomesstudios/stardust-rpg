from django.core import validators
from django.db import models
import enumfields

from . import character, equipment, items


class ItemQuantity(models.Model):
    class Meta:
        abstract = True

    slot = enumfields.EnumIntegerField(verbose_name='Slot', enum=equipment.Slot)
    quantity = models.IntegerField(default=1, validators=[validators.MinValueValidator(1)])
    item_index = models.IntegerField()

    @property
    def item(self) -> equipment.Item:
        return items.get_item(self.slot, self.item_index)


class InventorySlot(ItemQuantity):
    character = models.ForeignKey(character.Character, on_delete=models.CASCADE)

    @property
    def sel_value(self) -> int:
        return int(self.quantity * self.item.price * (self.character.sel / 100))

    @property
    def can_equip(self) -> bool:
        item = self.item
        if isinstance(item, equipment.MinAttributeItem):
            if self.character.get_attribute(item.min_attribute) >= item.min_attribute_value:
                return True
            else:
                return False
        else:
            return True
