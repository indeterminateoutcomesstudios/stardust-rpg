#!/usr/bin/env python3

import enumfields
from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from typing import Tuple

from . import abilities
from . import ability
from . import class_type
from . import classes
from . import combos
from . import dice
from . import equipment
from . import items
from .equipment import Attribute


class Character(models.Model):
    # TODO: Vulnerabilities and resistances.

    # Fields
    user = models.ForeignKey(User, unique=False)

    class_enum = enumfields.EnumIntegerField(classes.Classes, default=classes.Classes.empty)
    utility_enum = enumfields.EnumIntegerField(items.Utilities, default=items.Utilities.empty)
    head_enum = enumfields.EnumIntegerField(items.Heads, default=items.Heads.empty)
    neck_enum = enumfields.EnumIntegerField(items.Necks, default=items.Necks.empty)
    chest_enum = enumfields.EnumIntegerField(items.Chests, default=items.Chests.empty)
    shield_enum = enumfields.EnumIntegerField(items.Shields, default=items.Shields.empty)
    hand_enum = enumfields.EnumIntegerField(items.Hands, default=items.Hands.empty)
    feet_enum = enumfields.EnumIntegerField(items.Feets, default=items.Feets.empty)
    weapon_enum = enumfields.EnumIntegerField(items.Weapons, default=items.Weapons.empty)

    assigned_ath = models.IntegerField(verbose_name='Assigned ATH', default=0,
                                       validators=[validators.MinValueValidator(0)])
    assigned_ste = models.IntegerField(verbose_name='Assigned STE', default=0,
                                       validators=[validators.MinValueValidator(0)])
    assigned_for = models.IntegerField(verbose_name='Assigned FOR', default=0,
                                       validators=[validators.MinValueValidator(0)])
    assigned_apt = models.IntegerField(verbose_name='Assigned APT', default=0,
                                       validators=[validators.MinValueValidator(0)])
    assigned_per = models.IntegerField(verbose_name='Assigned PER', default=0,
                                       validators=[validators.MinValueValidator(0)])
    assigned_spe = models.IntegerField(verbose_name='Assigned SPE', default=0,
                                       validators=[validators.MinValueValidator(0)])

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
    extra_max_sp_per_skill = 3

    def __str__(self):
        return '{}: Level {} {}'.format(self.id, self.lvl, self.cls.name)

    @property
    def cls(self) -> class_type.Class:
        return classes.classes[self.class_enum]

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
    def non_weapon_wearables(self) -> Tuple[equipment.Wearable, ...]:
        return self.head, self.neck, self.chest, self.shield, self.hand, self.feet, self.utility

    @property
    def lvl(self):
        return self.levelup_set.count()

    def get_attribute(self, attribute: Attribute) -> int:
        if attribute is Attribute.stren:
            return self.stren
        elif attribute is Attribute.dex:
            return self.dex
        elif attribute is Attribute.con:
            return self.con
        elif attribute is Attribute.intel:
            return self.intel
        elif attribute is Attribute.wis:
            return self.wis
        elif attribute is Attribute.cha:
            return self.cha

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
    def available_ap(self) -> int:
        return self.ap - self.unlockedability_set.count()

    @property
    def abilities(self) -> Tuple[ability.Ability]:
        return [unlocked_ability.ability for unlocked_ability in self.unlockedability_set.all()]

    @property
    def combos(self) -> Tuple[combos.Combo]:
        # TODO: Make this part of cls?  Import issues.
        character_combos = []
        for combo in combos.combos:
            if self.cls.__class__ in combo.classes:
                character_combos.append(combo)
        return tuple(character_combos)

    @property
    def hp(self) -> int:
        return round(self.lvl * self.hp_lvl_con_mod * self.con +
                     sum([wearable.hp for wearable in self.wearables]) +
                     sum(level_up.hd_roll for level_up in self.levelup_set.all()))

    @property
    def mp(self) -> int:
        return ((self.lvl * self.mp_lvl_int_mod * self.intel) +
                sum([wearable.mp for wearable in self.wearables]) +
                sum(level_up.md_roll for level_up in self.levelup_set.all()))

    @property
    def sp(self) -> int:
        return (self.lvl * self.sp_lvl_int_mod * self.intel +
                sum([wearable.sp for wearable in self.wearables]) +
                sum(level_up.sd_roll for level_up in self.levelup_set.all()))

    @property
    def available_sp(self) -> int:
        return (self.sp - self.assigned_ath - self.assigned_ste - self.assigned_apt -
                self.assigned_for - self.assigned_per - self.assigned_spe)

    @property
    def max_sp_per_skill(self) -> int:
        return self.lvl + self.extra_max_sp_per_skill

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

    @property
    def ath(self) -> int:
        return ((self.stren * self.cls.ath) + self.assigned_ath +
                sum([wearable.ath for wearable in self.wearables]))

    @property
    def ste(self) -> int:
        return ((self.dex * self.cls.ste) + self.assigned_ste +
                sum([wearable.ste for wearable in self.wearables]))

    @property
    def fort(self) -> int:
        return ((self.con * self.cls.fort) + self.assigned_for +
                sum([wearable.fort for wearable in self.wearables]))

    @property
    def apt(self) -> int:
        return ((self.intel * self.cls.apt) + self.assigned_apt +
                sum([wearable.apt for wearable in self.wearables]))

    @property
    def per(self) -> int:
        return ((self.wis * self.cls.per) + self.assigned_per +
                sum([wearable.per for wearable in self.wearables]))

    @property
    def spe(self) -> int:
        return ((self.cha * self.cls.spe) + self.assigned_spe +
                sum([wearable.spe for wearable in self.wearables]))

    @property
    def can_use_weapon(self) -> bool:
        if self.weapon.style is equipment.Style.melee:
            if self.weapon.type is equipment.Type.light:
                return self.cls.use_melee_light
            elif self.weapon.type is equipment.Type.medium:
                return self.cls.use_melee_medium
            elif self.weapon.type is equipment.Type.heavy:
                return self.cls.use_melee_heavy
        elif self.weapon.style is equipment.Style.ranged:
            if self.weapon.type is equipment.Type.light:
                return self.cls.use_ranged_light
            elif self.weapon.type is equipment.Type.medium:
                return self.cls.use_ranged_medium
            elif self.weapon.type is equipment.Type.heavy:
                return self.cls.use_ranged_heavy
        elif self.weapon.style is equipment.Style.magic:
            if self.weapon.type is equipment.Type.light:
                return self.cls.use_magic_light
            elif self.weapon.type is equipment.Type.medium:
                return self.cls.use_magic_medium
            elif self.weapon.type is equipment.Type.heavy:
                return self.cls.use_magic_heavy


class UnlockedAbility(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    ability_enum = enumfields.EnumIntegerField(abilities.Abilities)

    @property
    def ability(self) -> ability.Ability:
        return abilities.abilities[self.ability_enum]
