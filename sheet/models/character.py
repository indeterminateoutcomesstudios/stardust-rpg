#!/usr/bin/env python3

import enum

import enumfields
from django.db import models
from typing import Tuple

from . import class_type
from . import equipment
from . import items


@enum.unique
class Attribute(enum.Enum):
    strength = 1
    dexterity = 2
    constitution = 3
    intelligence = 4
    wisdom = 5
    charisma = 6


class Character(models.Model):
    class_type = enumfields.EnumIntegerField(class_type.Classes, default=class_type.Classes.empty)
    utility_type = enumfields.EnumIntegerField(items.Utilities, default=items.Utilities.empty)
    head_type = enumfields.EnumIntegerField(items.Heads, default=items.Heads.empty)
    neck_type = enumfields.EnumIntegerField(items.Necks, default=items.Necks.empty)
    chest_type = enumfields.EnumIntegerField(items.Chests, default=items.Chests.empty)
    shield_type = enumfields.EnumIntegerField(items.Shields, default=items.Shields.empty)
    hand_type = enumfields.EnumIntegerField(items.Hands, default=items.Hands.empty)
    feet_type = enumfields.EnumIntegerField(items.Feets, default=items.Feets.empty)
    weapon_type = enumfields.EnumIntegerField(items.Weapons, default=items.Weapons.empty)

    def __str__(self):
        return 'Level {} {}'.format(self.lvl,
                                    class_type.class_map[self.class_type].name)

    @property
    def cls(self):
        return class_type.class_map[self.class_type]

    @property
    def utility(self):
        return items.utilities[self.utility_type]

    @property
    def head(self):
        return items.heads[self.head_type]

    @property
    def neck(self):
        return items.necks[self.neck_type]

    @property
    def chest(self):
        return items.chests[self.chest_type]

    @property
    def shield(self):
        return items.shields[self.shield_type]

    @property
    def hand(self):
        return items.hands[self.hand_type]

    @property
    def feet(self):
        return items.feets[self.feet_type]

    @property
    def weapon(self):
        return items.weapons[self.weapon_type]

    @property
    def wearables(self) -> Tuple[equipment.Wearable, ...]:
        return (self.head, self.neck, self.chest, self.shield, self.hand, self.feet, self.utility,
                self.weapon)

    @property
    def lvl(self):
        return self.levelup_set.count()

    @property
    def str(self) -> int:
        return (
            sum([level_up.ad_roll == Attribute.strength for level_up in self.levelup_set.all()]) +
            sum([level_up.selected_attribute == Attribute.strength
                 for level_up in self.levelup_set.all()]) +
            sum([wearable.str for wearable in self.wearables]))

    @property
    def pdef(self) -> int:
        # TODO: + self.dex
        return self.cls.pdef + sum([wearable.pdef for wearable in self.wearables])


class LevelUp(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    hd_roll = models.IntegerField(default=0)
    md_roll = models.IntegerField(default=0)
    sd_roll = models.IntegerField(default=0)
    ad_roll = enumfields.EnumIntegerField(Attribute, default=Attribute.strength)
    selected_attribute = enumfields.EnumIntegerField(Attribute, default=Attribute.strength)

# class Character(models.Model):
#     atp_lvl_mod = 2
#     ap_lvl_mod = 2
#     hp_lvl_con_mod = 1.5
#     mp_lvl_int_mod = 1
#     sp_lvl_int_mod = 1
#     pred_con_mod = 0.5
#     mred_int_mod = 0.5
#     starting_reg = 18
#     rd_char_mod = 0.25
#     speed_dex_mod = 0.5
#     vis_con_mod = 0.5
#     bpac_lvl_str_mod = 1
#     bmac_lvl_cha_mod = 1
#
#     lvl = models.IntegerField(default=0)
#
#
#     slot_min_attribute = frozendict(
#         {equipment.Slot.item: None,
#          equipment.Slot.utility: Attribute.intelligence,
#          equipment.Slot.weapon: Attribute.dexterity,
#          equipment.Slot.head: Attribute.intelligence,
#          equipment.Slot.neck: Attribute.wisdom,
#          equipment.Slot.chest: Attribute.strength,
#          equipment.Slot.shield: Attribute.strength,
#          equipment.Slot.hand: Attribute.charisma,
#          equipment.Slot.feet: Attribute.strength}
#     )
#
#     def __init__(self, cls: class_type.Class=class_type.Class(), lvl: int=0,
#                  utilities: Tuple[equipment.Wearable, equipment.Wearable, equipment.Wearable,
#                                   equipment.Wearable]=(
#                          items.empty_utility, items.empty_utility, items.empty_utility,
#                          items.empty_utility),
#                  head: equipment.Wearable=items.empty_head,
#                  neck: equipment.Wearable=items.empty_neck,
#                  chest: equipment.Wearable=items.empty_chest,
#                  shield: equipment.Wearable=items.empty_shield,
#                  feet: equipment.Wearable=items.empty_feet,
#                  right_hand: equipment.Hand=items.empty_hand,
#                  left_hand: equipment.Hand=items.empty_hand,
#                  weapons: Tuple[equipment.Weapon, equipment.Weapon, equipment.Weapon]=(
#                          items.empty_weapon, items.empty_weapon, items.empty_weapon),
#                  level_ups: Tuple[LevelUp, ...]=None):
#         self.cls = cls
#         self.lvl = lvl
#         self.head = head
#         self.neck = neck
#         self.chest = chest
#         self.shield = shield
#         self.right_hand = right_hand
#         self.left_hand = left_hand
#         self.feet = feet
#         self.utility1 = utilities[0]
#         self.utility2 = utilities[1]
#         self.utility3 = utilities[2]
#         self.utility4 = utilities[3]
#         self.weapon1 = weapons[0]
#         self.weapon2 = weapons[1]
#         self.weapon3 = weapons[2]
#
#         if level_ups is not None:
#             self.level_ups = level_ups
#         else:
#             self.level_ups = tuple()  # type: Tuple[LevelUp, ...]
#
#         # TODO: Misc attributes.

    # @property
    # def wearables(self) -> Tuple[equipment.Wearable, ...]:
    #     return (self.head, self.neck, self.chest, self.shield, self.right_hand, self.left_hand,
    #             self.feet, self.utility1, self.utility2, self.utility3, self.utility4,
    #             self.weapon1, self.weapon2, self.weapon3)
    #
    # @property
    # def stren(self) -> int:
    #     return (sum([roll == Attribute.strength.value for roll in self.ad_rolls]) +
    #             sum([attribute == Attribute.strength
    #                  for attribute in self.selected_attributes]))
    #
    # @property
    # def dex(self) -> int:
    #     return (sum([roll == Attribute.dexterity.value for roll in self.ad_rolls]) +
    #             sum([attribute == Attribute.dexterity
    #                  for attribute in self.selected_attributes]))
    #
    # @property
    # def con(self) -> int:
    #     return (sum([roll == Attribute.constitution.value for roll in self.ad_rolls]) +
    #             sum([attribute == Attribute.constitution
    #                  for attribute in self.selected_attributes]))
    #
    # @property
    # def intel(self) -> int:
    #     return (sum([roll == Attribute.intelligence.value for roll in self.ad_rolls]) +
    #             sum([attribute == Attribute.intelligence
    #                  for attribute in self.selected_attributes]))
    #
    # @property
    # def wis(self) -> int:
    #     return (sum([roll == Attribute.wisdom.value for roll in self.ad_rolls]) +
    #             sum([attribute == Attribute.intelligence
    #                  for attribute in self.selected_attributes]))
    #
    # @property
    # def cha(self) -> int:
    #     return (sum([roll == Attribute.charisma.value for roll in self.ad_rolls]) +
    #             sum([attribute == Attribute.intelligence
    #                  for attribute in self.selected_attributes]))
    #
    # @property
    # def max_atp(self) -> int:
    #     return self.lvl * self.atp_lvl_mod
    #
    # @property
    # def ap(self) -> int:
    #     return (self.cls.starting_ap + (self.ap_lvl_mod * self.lvl) + self.wis + self.cha +
    #             sum([wearable.ap for wearable in self.wearables]))
    #
    # @property
    # def hp(self) -> int:
    #     return round(self.lvl * self.hp_lvl_con_mod * self.con +
    #                  sum([wearable.hp for wearable in self.wearables]) + sum(self.hd_rolls))
    #
    # @property
    # def mp(self) -> int:
    #     return (self.lvl * self.mp_lvl_int_mod * self.intel) + sum(self.md_rolls)
    #
    # @property
    # def max_sp(self) -> int:
    #     return (self.lvl * self.sp_lvl_int_mod * self.intel +
    #             sum([wearable.sp for wearable in self.wearables]) + sum(self.sd_rolls))
    #
    # @property
    # def pdef(self) -> int:
    #     return self.cls.pdef + self.dex + sum([wearable.pdef for wearable in self.wearables])
    #
    # @property
    # def mdef(self) -> int:
    #     return round(self.cls.mdef * self.lvl +
    #                  sum([wearable.mdef for wearable in self.wearables]))
    #
    # @property
    # def pred(self) -> int:
    #     return round(self.cls.pred + (self.pred_con_mod * self.con) +
    #                  sum([wearable.pred for wearable in self.wearables]))
    #
    # @property
    # def mred(self) -> int:
    #     return round(self.cls.mred + (self.mred_int_mod * self.intel) +
    #                  sum([wearable.mred for wearable in self.wearables]))
    #
    # @property
    # def reg(self) -> int:
    #     return round(self.starting_reg - (self.cls.reg * self.lvl) - self.cha -
    #                  sum([wearable.reg for wearable in self.wearables]))
    #
    # @property
    # def rd(self) -> dice.DiceFormula:
    #     rd_modifier = round((self.rd_char_mod * self.cha) +
    #                         sum([wearable.rd for wearable in self.wearables]))
    #     if self.lvl <= 3:
    #         reg_dice = dice.Dice.from_str('d2')
    #     elif 4 <= self.lvl <= 6:
    #         reg_dice = dice.Dice.from_str('d4')
    #     elif 7 <= self.lvl <= 9:
    #         reg_dice = dice.Dice.from_str('d6')
    #     elif 10 <= self.lvl <= 12:
    #         reg_dice = dice.Dice.from_str('d8')
    #     elif 13 <= self.lvl <= 15:
    #         reg_dice = dice.Dice.from_str('d10')
    #     else:
    #         reg_dice = dice.Dice.from_str('d12')
    #
    #     return dice.DiceFormula(dice_pool=(reg_dice,), modifier=rd_modifier)
    #
    # @property
    # def speed(self) -> int:
    #     return round(self.cls.speed + (self.speed_dex_mod * self.dex) +
    #                  sum([wearable.speed for wearable in self.wearables]))
    #
    # @property
    # def vis(self) -> int:
    #     return round(self.cls.vis + (self.vis_con_mod * self.con) +
    #                  sum([wearable.vis for wearable in self.wearables]))
    #
    # @property
    # def bpac(self) -> int:
    #     return round(self.cls.pac + (self.bpac_lvl_str_mod * self.stren) +
    #                  sum([wearable.bpac for wearable in self.wearables]))
    #
    # @property
    # def bmac(self) -> int:
    #     return round(self.cls.mac + (self.bmac_lvl_cha_mod * self.cha) +
    #                  sum([wearable.bmac for wearable in self.wearables]))
    #
    # @property
    # def ath(self) -> int:
    #     return ((self.stren * self.cls.ath) +
    #             sum([wearable.ath for wearable in self.wearables]))
    #
    # @property
    # def ste(self) -> int:
    #     return (self.dex * self.cls.ste) + sum([wearable.ste for wearable in self.wearables])
    #
    # @property
    # def fort(self) -> int:
    #     return (self.con * self.cls.fort) + sum([wearable.fort for wearable in
    #                                              self.wearables])
    #
    # @property
    # def apt(self) -> int:
    #     return ((self.intel * self.cls.apt) +
    #             sum([wearable.apt for wearable in self.wearables]))
    #
    # @property
    # def per(self) -> int:
    #     return (self.wis * self.cls.per) + sum([wearable.per for wearable in self.wearables])
    #
    # @property
    # def spe(self) -> int:
    #     return self.cha * self.cls.spe + sum([wearable.spe for wearable in self.wearables])
