#!/usr/bin/env python3

import enum

import enumfields
from django.db import models
from typing import Tuple

from . import class_type
from . import dice
from . import equipment
from . import items


@enum.unique
class Attribute(enum.Enum):
    stren = 1
    dex = 2
    con = 3
    intel = 4
    wis = 5
    cha = 6

    @classmethod
    def from_string(cls, string_name: str) -> 'Attribute':
        for attribute in cls:
            if attribute.name == string_name:
                return attribute
        raise ValueError('Invalid {} name.'.format(cls.__name__))


class Character(models.Model):

    # Fields
    class_enum = enumfields.EnumIntegerField(class_type.Classes, default=class_type.Classes.empty)
    utility_enum = enumfields.EnumIntegerField(items.Utilities, default=items.Utilities.empty)
    head_enum = enumfields.EnumIntegerField(items.Heads, default=items.Heads.empty)
    neck_enum = enumfields.EnumIntegerField(items.Necks, default=items.Necks.empty)
    chest_enum = enumfields.EnumIntegerField(items.Chests, default=items.Chests.empty)
    shield_enum = enumfields.EnumIntegerField(items.Shields, default=items.Shields.empty)
    hand_enum = enumfields.EnumIntegerField(items.Hands, default=items.Hands.empty)
    feet_enum = enumfields.EnumIntegerField(items.Feets, default=items.Feets.empty)
    weapon_enum = enumfields.EnumIntegerField(items.Weapons, default=items.Weapons.empty)

    # Class constants
    ap_lvl_mod = 2
    hp_lvl_con_mod = 1.5
    mp_lvl_int_mod = 1
    sp_lvl_int_mod = 1
    starting_mdef = 5
    pred_con_mod = 0.5
    mred_int_mod = 0.5
    starting_reg = 18
    rd_char_mod = 0.25
    speed_dex_mod = 0.5
    vis_con_mod = 0.5
    bpac_lvl_str_mod = 1
    bmac_lvl_cha_mod = 1

    def __str__(self):
        return 'Level {} {}'.format(self.lvl,
                                    self.cls.name)

    @property
    def cls(self) -> class_type.Class:
        return class_type.class_map[self.class_enum]

    @property
    def utility(self) -> equipment.Wearable:
        return items.utilities[self.utility_enum]

    @property
    def head(self) -> equipment.Wearable:
        return items.heads[self.head_enum]

    @property
    def neck(self) -> equipment.Wearable:
        return items.necks[self.neck_enum]

    @property
    def chest(self) -> equipment.Wearable:
        return items.chests[self.chest_enum]

    @property
    def shield(self) -> equipment.Wearable:
        return items.shields[self.shield_enum]

    @property
    def hand(self) -> equipment.Hand:
        return items.hands[self.hand_enum]

    @property
    def feet(self) -> equipment.Wearable:
        return items.feets[self.feet_enum]

    @property
    def weapon(self) -> equipment.Weapon:
        return items.weapons[self.weapon_enum]

    @property
    def wearables(self) -> Tuple[equipment.Wearable, ...]:
        return (self.head, self.neck, self.chest, self.shield, self.hand, self.feet, self.utility,
                self.weapon)

    @property
    def lvl(self):
        return self.levelup_set.count()

    @property
    def stren(self) -> int:
        return (
            sum([level_up.ad_roll == Attribute.stren for level_up in self.levelup_set.all()]) +
            sum([level_up.selected_attribute == Attribute.stren
                 for level_up in self.levelup_set.all()]) +
            sum([wearable.str for wearable in self.wearables]))

    @property
    def dex(self) -> int:
        return (
            sum([level_up.ad_roll == Attribute.dex for level_up in self.levelup_set.all()]) +
            sum([level_up.selected_attribute == Attribute.dex
                 for level_up in self.levelup_set.all()]) +
            sum([wearable.dex for wearable in self.wearables]))

    @property
    def con(self) -> int:
        return (
            sum([level_up.ad_roll == Attribute.con for level_up in self.levelup_set.all()]) +
            sum([level_up.selected_attribute == Attribute.con
                 for level_up in self.levelup_set.all()]) +
            sum([wearable.con for wearable in self.wearables]))

    @property
    def intel(self) -> int:
        return (
            sum([level_up.ad_roll == Attribute.intel for level_up in self.levelup_set.all()]) +
            sum([level_up.selected_attribute == Attribute.intel
                 for level_up in self.levelup_set.all()]) +
            sum([wearable.int for wearable in self.wearables]))

    @property
    def wis(self) -> int:
        return (
            sum([level_up.ad_roll == Attribute.wis for level_up in self.levelup_set.all()]) +
            sum([level_up.selected_attribute == Attribute.wis
                 for level_up in self.levelup_set.all()]) +
            sum([wearable.wis for wearable in self.wearables]))

    @property
    def cha(self) -> int:
        return (
            sum([level_up.ad_roll == Attribute.cha for level_up in self.levelup_set.all()]) +
            sum([level_up.selected_attribute == Attribute.cha
                 for level_up in self.levelup_set.all()]) +
            sum([wearable.cha for wearable in self.wearables]))

    @property
    def ap(self) -> int:
        return (self.cls.starting_ap + (self.ap_lvl_mod * self.lvl) + self.wis + self.cha +
                sum([wearable.ap for wearable in self.wearables]))

    @property
    def hp(self) -> int:
        return round(self.lvl * self.hp_lvl_con_mod * self.con +
                     sum([wearable.hp for wearable in self.wearables]) +
                     sum(level_up.hd_roll for level_up in self.levelup_set.all()))

    @property
    def mp(self) -> int:
        return ((self.lvl * self.mp_lvl_int_mod * self.intel) +
                sum(level_up.md_roll for level_up in self.levelup_set.all()))

    @property
    def sp(self) -> int:
        return (self.lvl * self.sp_lvl_int_mod * self.intel +
                sum([wearable.sp for wearable in self.wearables]) +
                sum(level_up.sd_roll for level_up in self.levelup_set.all()))

    @property
    def pdef(self) -> int:
        return self.cls.pdef + self.dex + sum([wearable.pdef for wearable in self.wearables])

    @property
    def mdef(self) -> int:
        return round(self.starting_mdef + (self.cls.mdef * self.lvl) + self.wis +
                     sum([wearable.mdef for wearable in self.wearables]))

    @property
    def pred(self) -> int:
        return round(self.cls.pred + (self.pred_con_mod * self.con) +
                     sum([wearable.pred for wearable in self.wearables]))

    @property
    def mred(self) -> int:
        return round(self.cls.mred + (self.mred_int_mod * self.intel) +
                     sum([wearable.mred for wearable in self.wearables]))

    @property
    def reg(self) -> int:
        return round(self.starting_reg - (self.cls.reg * self.lvl) - self.cha -
                     sum([wearable.reg for wearable in self.wearables]))

    @property
    def rd(self) -> dice.DiceFormula:
        rd_modifier = round((self.rd_char_mod * self.cha) +
                            sum([wearable.rd for wearable in self.wearables]))
        if self.lvl <= 3:
            reg_dice = dice.Dice.from_str('d2')
        elif 4 <= self.lvl <= 6:
            reg_dice = dice.Dice.from_str('d4')
        elif 7 <= self.lvl <= 9:
            reg_dice = dice.Dice.from_str('d6')
        elif 10 <= self.lvl <= 12:
            reg_dice = dice.Dice.from_str('d8')
        elif 13 <= self.lvl <= 15:
            reg_dice = dice.Dice.from_str('d10')
        else:
            reg_dice = dice.Dice.from_str('d12')

        return dice.DiceFormula(dice_pool=(reg_dice,), modifier=rd_modifier)

    @property
    def speed(self) -> int:
        return round(self.cls.speed + (self.speed_dex_mod * self.dex) +
                     sum([wearable.speed for wearable in self.wearables]))

    @property
    def vis(self) -> int:
        return round(self.cls.vis + (self.vis_con_mod * self.con) +
                     sum([wearable.vis for wearable in self.wearables]))

    @property
    def bpac(self) -> int:
        return round(self.cls.pac + (self.bpac_lvl_str_mod * self.stren) +
                     sum([wearable.bpac for wearable in self.wearables]))

    @property
    def bmac(self) -> int:
        return round(self.cls.mac + (self.bmac_lvl_cha_mod * self.cha) +
                     sum([wearable.bmac for wearable in self.wearables]))

    # TODO: Assigned skill points.
    @property
    def ath(self) -> int:
        return ((self.stren * self.cls.ath) +
                sum([wearable.ath for wearable in self.wearables]))

    @property
    def ste(self) -> int:
        return (self.dex * self.cls.ste) + sum([wearable.ste for wearable in self.wearables])

    @property
    def fort(self) -> int:
        return (self.con * self.cls.fort) + sum([wearable.fort for wearable in
                                                 self.wearables])

    @property
    def apt(self) -> int:
        return ((self.intel * self.cls.apt) +
                sum([wearable.apt for wearable in self.wearables]))

    @property
    def per(self) -> int:
        return (self.wis * self.cls.per) + sum([wearable.per for wearable in self.wearables])

    @property
    def spe(self) -> int:
        return self.cha * self.cls.spe + sum([wearable.spe for wearable in self.wearables])


class LevelUp(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    hd_roll = models.IntegerField(default=0)
    md_roll = models.IntegerField(default=0)
    sd_roll = models.IntegerField(default=0)
    ad_roll = enumfields.EnumIntegerField(Attribute, default=Attribute.stren)
    selected_attribute = enumfields.EnumIntegerField(Attribute, default=Attribute.stren)
