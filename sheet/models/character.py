import copy
from typing import Optional, Tuple

from django.contrib.auth.models import User
from django.db import models
import enumfields

from . import abilities, ability, class_type, classes, combos, dice, equipment, items, party
from .abilities import round_up
from .equipment import Attribute


class Character(models.Model):
    # Fields
    user = models.ForeignKey(User, unique=False)
    name = models.CharField(max_length=25)
    party = models.ForeignKey(party.Party, unique=False)

    class_enum = enumfields.EnumIntegerField(classes.Classes,
                                             verbose_name='Class',
                                             default=classes.Classes.paladin)
    head_enum = enumfields.EnumIntegerField(items.Heads,
                                            verbose_name='Head',
                                            default=items.Heads.empty)
    neck_enum = enumfields.EnumIntegerField(items.Necks,
                                            verbose_name='Neck',
                                            default=items.Necks.empty)
    chest_enum = enumfields.EnumIntegerField(items.Chests,
                                             verbose_name='Chest',
                                             default=items.Chests.empty)
    shield_enum = enumfields.EnumIntegerField(items.Shields,
                                              verbose_name='Shield',
                                              default=items.Shields.empty)
    right_hand_enum = enumfields.EnumIntegerField(items.Hands,
                                                  verbose_name='Right Hand',
                                                  default=items.Hands.empty)
    left_hand_enum = enumfields.EnumIntegerField(items.Hands,
                                                 verbose_name='Left Hand',
                                                 default=items.Hands.empty)
    feet_enum = enumfields.EnumIntegerField(items.Feets,
                                            verbose_name='Feet',
                                            default=items.Feets.empty)
    weapon_enum = enumfields.EnumIntegerField(items.Weapons,
                                              verbose_name='Weapon',
                                              default=items.Weapons.empty)

    assigned_ath = models.PositiveIntegerField(verbose_name='Assigned ATH', default=0)
    assigned_ste = models.PositiveIntegerField(verbose_name='Assigned STE', default=0)
    assigned_for = models.PositiveIntegerField(verbose_name='Assigned FOR', default=0)
    assigned_apt = models.PositiveIntegerField(verbose_name='Assigned APT', default=0)
    assigned_per = models.PositiveIntegerField(verbose_name='Assigned PER', default=0)
    assigned_spe = models.PositiveIntegerField(verbose_name='Assigned SPE', default=0)

    # Class constants
    ap_lvl_mod = 2
    hp_lvl_con_mod = 1.5
    mp_lvl_int_mod = 1
    sp_lvl_int_mod = 1
    starting_mdef = 5
    pred_con_mod = 0.5
    mred_int_mod = 0.5
    rd_char_mod = 0.25
    speed_dex_mod = 0.5
    vis_con_mod = 0.5
    extra_max_sp_per_skill = 3
    light_weapon_str_damage_mod = 0.5
    medium_weapon_str_damage_mod = 1.0
    heavy_weapon_str_damage_mod = 1.5
    cha_buy_mod = 7
    """Percent."""

    base_sel = 50
    int_sel_mod = 10
    """Percent."""

    def __str__(self):
        return f'{self.name}: LVL {self.lvl} {self.cls.name}'

    @property
    def cls(self) -> class_type.Class:
        return classes.classes[self.class_enum]

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
    def right_hand(self) -> equipment.Hand:
        return items.hands[self.right_hand_enum]

    @property
    def left_hand(self) -> equipment.Hand:
        return items.hands[self.left_hand_enum]

    @property
    def feet(self) -> equipment.Wearable:
        return items.feets[self.feet_enum]

    @property
    def weapon(self) -> equipment.Weapon:
        return items.weapons[self.weapon_enum]

    @property
    def inventory_items(self) -> Tuple[equipment.Item, ...]:
        return tuple([inventory_slot.item for inventory_slot in self.inventoryslot_set.all()])

    @property
    def utilities(self) -> Tuple[equipment.Utility, ...]:
        utilities = []
        for item in self.inventory_items:
            if isinstance(item, equipment.Utility):
                if self.get_attribute(item.min_attribute) >= item.min_attribute_value:
                    utilities.append(item)
        return tuple(utilities)

    @property
    def wearables(self) -> Tuple[equipment.Wearable, ...]:
        return (self.head, self.neck, self.chest, self.shield, self.right_hand, self.left_hand,
                self.feet, self.weapon)

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
    def ap_formula(self) -> str:
        return (f'{self.cls.starting_ap}[Starting AP] + ({self.ap_lvl_mod} * {self.lvl}[LVL]) + '
                f'{self.wis}[WIS] + {self.cha}[CHA] + '
                f'{sum([wearable.ap for wearable in self.wearables])}[Wearables]')

    @property
    def ap(self) -> int:
        return (self.cls.starting_ap + (self.ap_lvl_mod * self.lvl) + self.wis + self.cha +
                sum([wearable.ap for wearable in self.wearables]))

    @property
    def available_ap(self) -> int:
        return self.ap - self.unlockedability_set.count()

    @property
    def unlocked_abilities(self) -> Tuple[ability.Ability, ...]:
        return tuple([unlocked_ability.ability
                      for unlocked_ability in self.unlockedability_set.all()])

    @property
    def available_to_unlock_abilities(self) -> Tuple[ability.Ability, ...]:
        available_abilities = []
        unlocked_abilities = self.unlocked_abilities  # Avoid multiple database reads.
        for class_ability in self.cls.abilities:
            is_available = True
            for prerequisite in class_ability.prerequisites:
                if prerequisite not in unlocked_abilities:
                    is_available = False
            if is_available:
                available_abilities.append(class_ability)
        return tuple(available_abilities)

    @property
    def class_combos(self) -> Tuple[combos.Combo, ...]:
        # TODO: Make this part of cls?  Import issues.
        character_combos = []
        for combo in combos.combos:
            if self.cls.__class__ in combo.classes:
                character_combos.append(combo)
        return tuple(character_combos)

    @property
    def party_members(self) -> Tuple['Character', ...]:
        """Other Characters other than this one in the Party."""
        party_members = []
        for party_member in self.party.character_set.all():
            if party_member != self:
                party_members.append(party_member)
        return tuple(party_members)

    @property
    def party_combos(self) -> Tuple[combos.Combo, ...]:
        character_party_combos = []
        for combo in self.class_combos:
            for party_member in self.party_members:
                if ((self.cls.__class__ is combo.classes[0] and
                     party_member.cls.__class__ is combo.classes[1]) or
                    (self.cls.__class__ is combo.classes[1] and
                     party_member.cls.__class__ is combo.classes[0])):
                    character_party_combos.append(combo)
                    continue
        return tuple(character_party_combos)

    @property
    def unlocked_combos(self) -> Tuple[combos.Combo, ...]:
        unlocked_combos = []
        for combo in self.party_combos:
            if self.lvl >= combo.prerequisite_lvl:
                unlocked_combos.append(combo)
        return tuple(unlocked_combos)

    @property
    def hp_formula(self) -> str:
        return (f'({self.lvl}[LVL] * {self.hp_lvl_con_mod} * {self.con}[CON]) + '
                f'{sum([wearable.hp for wearable in self.wearables])}[Wearables] + '
                f'{sum(level_up.hd_roll for level_up in self.levelup_set.all())}[HD rolls]')

    @property
    def hp(self) -> int:
        return round_up(self.lvl * self.hp_lvl_con_mod * self.con +
                        sum([wearable.hp for wearable in self.wearables]) +
                        sum(level_up.hd_roll for level_up in self.levelup_set.all()))

    @property
    def mp_formula(self) -> str:
        return (f'({self.lvl}[LVL] * {self.mp_lvl_int_mod} * {self.intel}[INT]) + '
                f'{sum([wearable.mp for wearable in self.wearables])}[Wearables] + '
                f'{sum(level_up.md_roll for level_up in self.levelup_set.all())}[MD rolls]')

    @property
    def mp(self) -> int:
        return ((self.lvl * self.mp_lvl_int_mod * self.intel) +
                sum([wearable.mp for wearable in self.wearables]) +
                sum(level_up.md_roll for level_up in self.levelup_set.all()))

    @property
    def sp_formula(self) -> str:
        return (f'({self.lvl}[LVL] * {self.mp_lvl_int_mod} * {self.intel}[INT]) + '
                f'{sum([wearable.sp for wearable in self.wearables])}[Wearables] + '
                f'{sum(level_up.sd_roll for level_up in self.levelup_set.all())}[SD rolls]')

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
    def max_sp_per_skill_formula(self) -> str:
        return f'{self.lvl}[LVL] + {self.extra_max_sp_per_skill}'

    @property
    def max_sp_per_skill(self) -> int:
        return self.lvl + self.extra_max_sp_per_skill

    @property
    def pdef_formula(self) -> str:
        return (f'{self.cls.pdef}[Class PDEF] + {self.dex}[DEX] + '
                f'{sum([wearable.pdef for wearable in self.wearables])}[Wearables]')

    @property
    def pdef(self) -> int:
        return self.cls.pdef + self.dex + sum([wearable.pdef for wearable in self.wearables])

    @property
    def mdef_formula(self) -> str:
        return (f'{self.starting_mdef}[Starting MDEF] + '
                f'({self.cls.mdef}[Class MDEF] * {self.lvl}[LVL]) + {self.wis}[WIS] + '
                f'{sum([wearable.mdef for wearable in self.wearables])}[Wearables]')

    @property
    def mdef(self) -> int:
        return round_up(self.starting_mdef + (self.cls.mdef * self.lvl) + self.wis +
                        sum([wearable.mdef for wearable in self.wearables]))

    @property
    def pred_formula(self) -> str:
        return (f'{self.cls.pred}[Class PRED] + ({self.pred_con_mod} * {self.con}[CON]) + '
                f'{sum([wearable.pred for wearable in self.wearables])}[Wearables]')

    @property
    def pred(self) -> int:
        return round_up(self.cls.pred + (self.pred_con_mod * self.con) +
                        sum([wearable.pred for wearable in self.wearables]))

    @property
    def mred_formula(self) -> str:
        return (f'{self.cls.mred}[Class MRED] + ({self.mred_int_mod} * {self.intel}[INT]) + '
                f'{sum([wearable.mred for wearable in self.wearables])}[Wearables]')

    @property
    def mred(self) -> int:
        return round_up(self.cls.mred + (self.mred_int_mod * self.intel) +
                        sum([wearable.mred for wearable in self.wearables]))

    @property
    def reg_formula(self) -> str:
        return (f'({self.cls.reg}[Class REG] * {self.lvl}[LVL]) + {self.cha}[CHA] + '
                f'{sum([wearable.reg for wearable in self.wearables])}[Wearables]')

    @property
    def reg(self) -> int:
        return round_up((self.cls.reg * self.lvl) + self.cha +
                        sum([wearable.reg for wearable in self.wearables]))

    @property
    def rd_formula(self) -> str:
        return (f'LVL 1-3=d2, LVL 4-6=d4, LVL 7-9=d6, LVL 10-12=d8, LVL 13-15=d10, LVL 16+=d12\n'
                f'({self.rd_char_mod} * {self.cha}[CHA]) + '
                f'{sum([wearable.rd for wearable in self.wearables])}[Wearables]')

    @property
    def rd(self) -> dice.DiceFormula:
        rd_modifier = round_up((self.rd_char_mod * self.cha) +
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
    def speed_formula(self) -> str:
        return (f'{self.cls.speed}[Class SPEED] + ({self.speed_dex_mod} * {self.dex}[DEX]) + '
                f'{sum([wearable.speed for wearable in self.wearables])}[Wearables]')

    @property
    def speed(self) -> int:
        return round_up(self.cls.speed + (self.speed_dex_mod * self.dex) +
                        sum([wearable.speed for wearable in self.wearables]))

    @property
    def vis_formula(self) -> str:
        return (f'{self.cls.vis}[Class VIS] + ({self.vis_con_mod} * {self.con}[CON]) + '
                f'{sum([wearable.vis for wearable in self.wearables])}[Wearables]')

    @property
    def vis(self) -> int:
        return round_up(self.cls.vis + (self.vis_con_mod * self.con) +
                        sum([wearable.vis for wearable in self.wearables]))

    @property
    def bpac_formula(self) -> str:
        return (f'({self.cls.pac}[Class PAC] * {self.lvl}[LVL]) + {self.stren}[STR] + '
                f'{sum([wearable.bpac for wearable in self.wearables])}[Wearables]')

    @property
    def bpac(self) -> int:
        return round_up((self.cls.pac * self.lvl) + self.stren +
                        sum([wearable.bpac for wearable in self.wearables]))

    @property
    def bmac_formula(self) -> str:
        return (f'({self.cls.mac}[Class MAC] * {self.lvl}[LVL]) + {self.cha}[CHA] + '
                f'{sum([wearable.bmac for wearable in self.wearables])}[Wearables]')

    @property
    def bmac(self) -> int:
        return round_up((self.cls.mac * self.lvl) + self.cha +
                        sum([wearable.bmac for wearable in self.wearables]))

    @property
    def cran(self) -> int:
        return sum([wearable.cran for wearable in self.wearables])

    @property
    def ath_formula(self) -> str:
        return (f'({self.cls.ath}[Class ATH] * {self.stren}[STR]) + '
                f'{self.assigned_ath}[Assigned ATH] + '
                f'{sum([wearable.ath for wearable in self.wearables])}[Wearables]')

    @property
    def ath(self) -> int:
        return ((self.cls.ath * self.stren) + self.assigned_ath +
                sum([wearable.ath for wearable in self.wearables]))

    @property
    def ste_formula(self) -> str:
        return (f'({self.cls.ste}[Class STE] * {self.dex}[DEX]) + '
                f'{self.assigned_ste}[Assigned STE] + '
                f'{sum([wearable.ste for wearable in self.wearables])}[Wearables]')

    @property
    def ste(self) -> int:
        return ((self.cls.ste * self.dex) + self.assigned_ste +
                sum([wearable.ste for wearable in self.wearables]))

    @property
    def for_formula(self) -> str:
        return (f'({self.cls.fort}[Class FOR] * {self.con}[CON]) + '
                f'{self.assigned_for}[Assigned FOR] + '
                f'{sum([wearable.fort for wearable in self.wearables])}[Wearables]')

    @property
    def fort(self) -> int:
        return ((self.cls.fort * self.con) + self.assigned_for +
                sum([wearable.fort for wearable in self.wearables]))

    @property
    def apt_formula(self) -> str:
        return (f'({self.cls.apt}[Class APT] * {self.intel}[INT]) + '
                f'{self.assigned_apt}[Assigned APT] + '
                f'{sum([wearable.apt for wearable in self.wearables])}[Wearables]')

    @property
    def apt(self) -> int:
        return ((self.cls.apt * self.intel) + self.assigned_apt +
                sum([wearable.apt for wearable in self.wearables]))

    @property
    def per_formula(self) -> str:
        return (f'({self.cls.per}[Class PER] * {self.wis}[WIS]) + '
                f'{self.assigned_per}[Assigned PER] + '
                f'{sum([wearable.per for wearable in self.wearables])}[Wearables]')

    @property
    def per(self) -> int:
        return ((self.cls.per * self.wis) + self.assigned_per +
                sum([wearable.per for wearable in self.wearables]))

    @property
    def spe_formula(self) -> str:
        return (f'({self.cls.spe}[Class SPE] * {self.cha}[CHA]) + '
                f'{self.assigned_spe}[Assigned SPE] + '
                f'{sum([wearable.spe for wearable in self.wearables])}[Wearables]')

    @property
    def spe(self) -> int:
        return ((self.cls.spe * self.cha) + self.assigned_spe +
                sum([wearable.spe for wearable in self.wearables]))

    @property
    def buy_formula(self) -> str:
        return f'{self.cha_buy_mod} * {self.cha}[CHA]'

    @property
    def buy(self) -> int:
        return min(self.cha_buy_mod * self.cha, 100)

    @property
    def buy_fraction(self) -> float:
        """Returns a value that can be multiplied by a cost to get the cost of an item for
        this character."""
        return 1.0 - (self.buy / 100)

    @property
    def sel_formula(self) -> str:
        return f'{self.base_sel}[Base SEL] + ({self.int_sel_mod} * {self.intel}[INT])'

    @property
    def sel(self) -> int:
        return min(self.base_sel + self.int_sel_mod * self.intel, 100)

    @property
    def sel_fraction(self) -> float:
        """Returns a value that can be multiplied by a cost to get the SEL value of an item for
        this character."""
        return self.sel / 100

    @property
    def vul_set(self) -> equipment.VulnerabilitySet:
        vul_set = equipment.VulnerabilitySet()

        for wearable in self.wearables:
            vul_set.merge(wearable.vul_set)

        return vul_set

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

    def can_use_wearable(self, wearable: equipment.Wearable) -> bool:
        if wearable.type is equipment.Type.light and self.cls.use_light_armor:
            return True
        elif wearable.type is equipment.Type.medium and self.cls.use_medium_armor:
            return True
        elif wearable.type is equipment.Type.heavy and self.cls.use_heavy_armor:
            return True
        else:
            return False

    @property
    def _str_damage(self) -> int:
        str_damage = 0
        if self.weapon.type is equipment.Type.light:
            str_damage = round_up(self.light_weapon_str_damage_mod * self.stren)
        elif self.weapon.type is equipment.Type.medium:
            str_damage = round_up(self.medium_weapon_str_damage_mod * self.stren)
        elif self.weapon.type is equipment.Type.heavy:
            str_damage = round_up(self.heavy_weapon_str_damage_mod * self.stren)
        return str_damage

    @property
    def weapon_pdam(self) -> Optional[dice.DiceFormula]:
        if self.weapon.pdam is None:
            return None
        else:
            pdam_dice = copy.deepcopy(self.weapon.pdam)
            pdam_dice.modifier += self._str_damage
            return pdam_dice

    @property
    def weapon_pdam_dps(self) -> int:
        if self.weapon_pdam is not None:
            return round(self.weapon.attacks * self.weapon_pdam.mean(), 1)
        else:
            return 0

    @property
    def weapon_mdam(self) -> Optional[dice.DiceFormula]:
        if self.weapon.mdam is None:
            return None
        else:
            mdam_dice = copy.deepcopy(self.weapon.mdam)
            mdam_dice.modifier += self._str_damage
            return mdam_dice

    @property
    def weapon_mdam_dps(self) -> int:
        if self.weapon_mdam is not None:
            return round(self.weapon.attacks * self.weapon_mdam.mean(), 1)
        else:
            return 0


class UnlockedAbility(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    ability_enum = enumfields.EnumIntegerField(abilities.Abilities)

    @property
    def ability(self) -> ability.Ability:
        return abilities.abilities[self.ability_enum]

    def __str__(self) -> str:
        return f'{self.character} {self.ability.name}'
