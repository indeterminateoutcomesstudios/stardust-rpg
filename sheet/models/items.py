#!/usr/bin/env python3

"""Temporary module to store items until database solution is created."""

from . import equipment

empty_utility = equipment.Utility(name='Empty', rarity=equipment.Rarity.common, price=0,
                                  effect='', equip_type=equipment.Type.light,
                                  stats=equipment.Stats())

empty_head = equipment.Head(name='Empty', rarity=equipment.Rarity.common, price=0,
                            effect='', equip_type=equipment.Type.light,
                            stats=equipment.Stats())

empty_neck = equipment.Neck(name='Empty', rarity=equipment.Rarity.common, price=0,
                            effect='', equip_type=equipment.Type.light,
                            stats=equipment.Stats())

empty_chest = equipment.Chest(name='Empty', rarity=equipment.Rarity.common, price=0,
                              effect='', equip_type=equipment.Type.light,
                              stats=equipment.Stats())

empty_shield = equipment.Shield(name='Empty', rarity=equipment.Rarity.common, price=0,
                                effect='', equip_type=equipment.Type.light,
                                stats=equipment.Stats())

empty_hand = equipment.Hand(name='Empty', rarity=equipment.Rarity.common, price=0,
                            effect='', equip_type=equipment.Type.light,
                            stats=equipment.Stats())

empty_feet = equipment.Feet(name='Empty', rarity=equipment.Rarity.common, price=0,
                            effect='', equip_type=equipment.Type.light,
                            stats=equipment.Stats())

empty_weapon = equipment.Weapon(name='Empty', rarity=equipment.Rarity.common, price=0,
                                effect='', equip_type=equipment.Type.light,
                                stats=equipment.Stats(),
                                is_two_handed=False, min_range=0, max_range=0,
                                shape=equipment.Shape.point, attacks=0, pac=0,
                                damage_type=equipment.DamageType.slashing, cran=0, cdam=0)
