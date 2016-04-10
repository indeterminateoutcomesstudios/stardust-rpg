#!/usr/bin/env python3

import enum

import autoenum
import enumfields
from django.db import models
from frozendict import frozendict


@enum.unique
class Attribute(enum.Enum):
    strength = 1
    dexterity = 2
    constitution = 3
    intelligence = 4
    wisdom = 5
    charisma = 6


class Slot(autoenum.AutoEnum):
    item = ()
    utility = ()
    weapon = ()
    head = ()
    neck = ()
    chest = ()
    shield = ()
    hand = ()
    feet = ()

slot_min_attribute = frozendict(
    {Slot.item: None,
     Slot.utility: Attribute.intelligence,
     Slot.weapon: Attribute.dexterity,
     Slot.head: Attribute.intelligence,
     Slot.neck: Attribute.wisdom,
     Slot.chest: Attribute.strength,
     Slot.shield: Attribute.strength,
     Slot.hand: Attribute.charisma,
     Slot.feet: Attribute.strength}
)


class Rarity(autoenum.AutoEnum):
    common = ()
    rare = ()
    unique = ()
    set = ()


class Style(autoenum.AutoEnum):
    melee = ()
    ranged = ()
    magic = ()


class Type(enum.Enum):
    light = ()
    medium = ()
    heavy = ()


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


class DamageType(autoenum.AutoEnum):
    slashing = ()
    piercing = ()
    bludgeoning = ()
    fire = ()
    cold = ()
    lightning = ()
    acid = ()
    poison = ()
    force = ()
    psychic = ()


class Equipment(models.Model):
    slot = enumfields.EnumIntegerField(Slot)
    name = models.TextField()
    rarity = enumfields.EnumField(Rarity, default=Rarity.common)
    price = models.IntegerField(default=0)
    effect = models.TextField(default='')


class Wearable(Equipment):
    type = enumfields.EnumIntegerField(Type, default=Type.light)

    stren = models.IntegerField(default=0)
    dex = models.IntegerField(default=0)
    con = models.IntegerField(default=0)
    intel = models.IntegerField(default=0)
    wis = models.IntegerField(default=0)
    cha = models.IntegerField(default=0)
    ath = models.IntegerField(default=0)
    ste = models.IntegerField(default=0)
    fort = models.IntegerField(default=0)
    apt = models.IntegerField(default=0)
    per = models.IntegerField(default=0)
    spe = models.IntegerField(default=0)
    ap = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    mp = models.IntegerField(default=0)
    sp = models.IntegerField(default=0)
    pdef = models.IntegerField(default=0)
    mdef = models.IntegerField(default=0)
    pred = models.FloatField(default=0)
    mred = models.FloatField(default=0)
    reg = models.IntegerField(default=0)
    rd = models.IntegerField(default=0)
    speed = models.FloatField(default=0)
    vis = models.IntegerField(default=0)
    bpac = models.IntegerField(default=0)
    bmac = models.IntegerField(default=0)


class Hand(Wearable):
    is_two_handed = models.BooleanField(default=False)


class Weapon(Hand):
    min_range = models.IntegerField(default=1)
    max_range = models.IntegerField(default=1)
    shape = enumfields.EnumField(Shape, max_length=100)
    attacks = models.IntegerField(default=1)
    pac = models.IntegerField(default=0)
    damage_type = enumfields.EnumIntegerField(DamageType)
    cran = models.IntegerField(default=0)
    cdam = models.IntegerField(default=0)
    pdam = models.TextField(default='')
    mdam = models.TextField(default='')
