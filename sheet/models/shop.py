from typing import Tuple

from django.db import models

from . import equipment, inventory_slot, party


class Shop(models.Model):
    party = models.ForeignKey(party.Party, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    visible = models.BooleanField(default=False)

    def _slot_items(self, slot: equipment.Slot) -> Tuple[equipment.Item]:
        return tuple([shop_slot for shop_slot in self.shopslot_set.all()
                      if shop_slot.slot is slot])

    @property
    def item_slots(self) -> Tuple[equipment.Item]:
        return self._slot_items(equipment.Slot.item)

    @property
    def utility_slots(self) -> Tuple[equipment.Utility]:
        return self._slot_items(equipment.Slot.utility)

    @property
    def weapon_slots(self) -> Tuple[equipment.Weapon]:
        return self._slot_items(equipment.Slot.weapon)

    @property
    def head_slots(self) -> Tuple[equipment.Head]:
        return self._slot_items(equipment.Slot.head)

    @property
    def neck_slots(self) -> Tuple[equipment.Neck]:
        return self._slot_items(equipment.Slot.neck)

    @property
    def chest_slots(self) -> Tuple[equipment.Chest]:
        return self._slot_items(equipment.Slot.chest)

    @property
    def shield_slots(self) -> Tuple[equipment.Shield]:
        return self._slot_items(equipment.Slot.shield)

    @property
    def hand_slots(self) -> Tuple[equipment.Hand]:
        return self._slot_items(equipment.Slot.hand)

    @property
    def feet_slots(self) -> Tuple[equipment.Feet]:
        return self._slot_items(equipment.Slot.feet)

    def __str__(self) -> str:
        return f'{self.name} Shop: {self.id}'


class ShopSlot(inventory_slot.ItemQuantity):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
