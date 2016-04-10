#!/usr/bin/env python3

"""Temporary module to store items until database solution is created."""

from . import equipment

empty_utility = equipment.Wearable(slot=equipment.Slot.utility, name='Empty')

empty_head = equipment.Wearable(slot=equipment.Slot.head, name='Empty')

empty_neck = equipment.Wearable(slot=equipment.Slot.neck, name='Empty')

empty_chest = equipment.Wearable(slot=equipment.Slot.chest, name='Empty')

empty_shield = equipment.Wearable(slot=equipment.Slot.shield, name='Empty')

empty_hand = equipment.Hand(slot=equipment.Slot.hand, name='Empty')

empty_feet = equipment.Wearable(slot=equipment.Slot.feet, name='Empty')

empty_weapon = equipment.Weapon(name='Empty', min_range=0, max_range=0,
                                shape=equipment.Shape.point, attacks=0, pac=0,
                                damage_type=equipment.DamageType.slashing, cran=0, cdam=0)
