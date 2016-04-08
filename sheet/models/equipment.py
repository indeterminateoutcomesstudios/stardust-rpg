#!/usr/bin/env python3

import enum
import itertools

from . import dice

_enum_value = itertools.count(1)


@enum.unique
class Slot(enum.Enum):
    item = next(_enum_value)
    utility = next(_enum_value)
    weapon = next(_enum_value)
    head = next(_enum_value)
    neck = next(_enum_value)
    chest = next(_enum_value)
    shield = next(_enum_value)
    hand = next(_enum_value)
    feet = next(_enum_value)

_enum_value = itertools.count(1)


@enum.unique
class Rarity(enum.Enum):
    common = next(_enum_value)
    rare = next(_enum_value)
    unique = next(_enum_value)
    set = next(_enum_value)

_enum_value = itertools.count(1)


@enum.unique
class Style(enum.Enum):
    melee = next(_enum_value)
    ranged = next(_enum_value)
    magic = next(_enum_value)

_enum_value = itertools.count(1)


@enum.unique
class Type(enum.Enum):
    light = next(_enum_value)
    medium = next(_enum_value)
    heavy = next(_enum_value)


_enum_value = itertools.count(1)


@enum.unique
class Attribute(enum.Enum):
    strength = 1
    dexterity = 2
    constitution = 3
    intelligence = 4
    wisdom = 5
    charisma = 6


@enum.unique
class Shape(enum.Enum):
    point = 'http://i.imgur.com/Snx8fr2.png'
    multi_point = 'http://i.imgur.com/IB4CXeb.png'
    line = 'http://i.imgur.com/CbqMJ3N.png'
    double_line = 'https://i.imgur.com/roFRLYp.png'
    dual_line = 'http://i.imgur.com/FEjIzJH.png'
    volatile_line = 'http://i.imgur.com/45eHyTK.png'
    overloaded_line = 'http://i.imgur.com/4H9ZLTK.png'
    circle = 'http://i.imgur.com/OgukZ2z.png'
    cluster = 'http://i.imgur.com/2oCm5ny.png'
    square = 'http://i.imgur.com/HFNR3fs.png'
    cone = 'http://i.imgur.com/Ievab1N.png'
    wave = 'http://i.imgur.com/CejaQ8C.png'
    x = 'http://i.imgur.com/anYlNRb.png'
    melee_point = 'http://i.imgur.com/oLGyQrf.png'
    line_2 = 'http://i.imgur.com/8m66T5y.png'
    line_3 = 'http://i.imgur.com/j9RpR23.png'
    side_line_2 = 'http://i.imgur.com/lxlckBh.png'
    side_line_3 = 'http://i.imgur.com/W7jZB1R.png'
    halo = 'http://i.imgur.com/vp8K3ou.png'
    side_multi_point = 'http://i.imgur.com/4n7lbv1.png'
    melee_x = 'http://i.imgur.com/6jpEhfb.png'
    t = 'http://i.imgur.com/P4kpZox.png'
    y = 'http://i.imgur.com/vmb2P3N.png'
    range_point = 'http://i.imgur.com/CsJDRVa.png'
    range_multi_point = 'http://i.imgur.com/ldZwwVO.png'
    range_circle = 'http://i.imgur.com/bTYrZBc.png'
    cone_3 = 'http://i.imgur.com/5qYh6je.png'

_enum_value = itertools.count(1)


@enum.unique
class DamageType(enum.Enum):
    slashing = next(_enum_value)
    piercing = next(_enum_value)
    bludgeoning = next(_enum_value)
    fire = next(_enum_value)
    cold = next(_enum_value)
    lightning = next(_enum_value)
    acid = next(_enum_value)
    poison = next(_enum_value)
    force = next(_enum_value)
    psychic = next(_enum_value)


class Stats:
    def __init__(self, stren: int=0, dex: int=0, con: int=0, intel: int=0, wis: int=0, cha: int=0,
                 ath: int=0, ste: int=0, fort: int=0, apt: int=0, per: int=0, spe: int=0,
                 ap: int=0, hp: int=0, mp: int=0, sp: int=0, pdef: int=0, mdef: int=0,
                 pred: float=0.0, mred: float=0.0, reg: int=0, rd: int=0, speed: float=0,
                 vis: int=0, bpac: int=0, bmac: int=0):
        self.str = stren
        self.dex = dex
        self.con = con
        self.int = intel
        self.wis = wis
        self.cha = cha
        self.ath = ath
        self.ste = ste
        self.fort = fort
        self.apt = apt
        self.per = per
        self.spe = spe
        self.ap = ap
        self.hp = hp
        self.mp = mp
        self.sp = sp
        self.pdef = pdef
        self.mdef = mdef
        self.pred = pred
        self.mred = mred
        self.reg = reg
        self.rd = rd
        self.speed = speed
        self.vis = vis
        self.bpac = bpac
        self.bmac = bmac


class Equipment:
    def __init__(self, slot: Slot, name: str, rarity: Rarity, price: int, effect: str):
        self.slot = slot
        self.name = name
        self.rarity = rarity
        self.price = price
        self.effect = effect


class Wearable(Equipment):
    def __init__(self, slot: Slot, name: str, rarity: Rarity, price: int, effect: str,
                 equip_type: Type, stats: Stats, min_attribute: Attribute):
        self.type = equip_type
        self.min_attribute = min_attribute
        self.stats = stats
        super().__init__(slot=slot, name=name, rarity=rarity, price=price, effect=effect)


class Utility(Wearable):
    def __init__(self, name: str, rarity: Rarity, price: int, effect: str,
                 equip_type: Type, stats: Stats):
        super().__init__(slot=Slot.utility, name=name, rarity=rarity, price=price, effect=effect,
                         equip_type=equip_type, stats=stats, min_attribute=Attribute.intelligence)


class Head(Wearable):
    def __init__(self, name: str, rarity: Rarity, price: int, effect: str,
                 equip_type: Type, stats: Stats):
        super().__init__(slot=Slot.head, name=name, rarity=rarity, price=price, effect=effect,
                         equip_type=equip_type, stats=stats, min_attribute=Attribute.intelligence)


class Neck(Wearable):
    def __init__(self, name: str, rarity: Rarity, price: int, effect: str,
                 equip_type: Type, stats: Stats):
        super().__init__(slot=Slot.neck, name=name, rarity=rarity, price=price, effect=effect,
                         equip_type=equip_type, stats=stats, min_attribute=Attribute.wisdom)


class Chest(Wearable):
    def __init__(self, name: str, rarity: Rarity, price: int, effect: str,
                 equip_type: Type, stats: Stats):
        super().__init__(slot=Slot.chest, name=name, rarity=rarity, price=price, effect=effect,
                         equip_type=equip_type, stats=stats, min_attribute=Attribute.strength)


class Shield(Wearable):
    def __init__(self, name: str, rarity: Rarity, price: int, effect: str,
                 equip_type: Type, stats: Stats):
        super().__init__(slot=Slot.shield, name=name, rarity=rarity, price=price, effect=effect,
                         equip_type=equip_type, stats=stats, min_attribute=Attribute.strength)


class Feet(Wearable):
    def __init__(self, name: str, rarity: Rarity, price: int, effect: str,
                 equip_type: Type, stats: Stats):
        super().__init__(slot=Slot.feet, name=name, rarity=rarity, price=price, effect=effect,
                         equip_type=equip_type, stats=stats, min_attribute=Attribute.strength)


class Hand(Wearable):
    def __init__(self, name: str, rarity: Rarity, price: int, effect: str,
                 equip_type: Type, stats: Stats, is_two_handed: bool=False):
        self.is_two_handed = is_two_handed
        super().__init__(slot=Slot.hand, name=name, rarity=rarity, price=price, effect=effect,
                         equip_type=equip_type, stats=stats, min_attribute=Attribute.charisma)


class Weapon(Hand):
    def __init__(self, name: str, rarity: Rarity, price: int, effect: str,
                 equip_type: Type, stats: Stats, is_two_handed: bool,
                 min_range: int, max_range: int, shape: Shape, attacks: int,
                 pac: int, damage_type: DamageType, cran: int, cdam: int,
                 pdam: dice.DiceFormula=None, mdam: dice.DiceFormula=None):
        self.min_range = min_range
        self.max_range = max_range
        self.shape = shape
        self.attacks = attacks
        self.pac = pac
        self.damage_type = damage_type
        self.cran = cran
        self.cdam = cdam
        self.pdam = pdam
        self.mdam = mdam
        super().__init__(name=name, rarity=rarity, price=price, effect=effect,
                         equip_type=equip_type, stats=stats, is_two_handed=is_two_handed)
