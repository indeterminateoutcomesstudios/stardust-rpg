#!/usr/bin/env python3

import aenum

from .dice import DiceFormula
from .equipment import (Chest, DamageType, Feet, Hand, Head, Neck, Shape, Shield, Style, Utility,
                        Weapon, WeaponPicture)


class Utilities(aenum.AutoNumberEnum):
    empty = ()
    candle = ()

utilities = {
    Utilities.empty: Utility(name=Utilities.empty.name),
    Utilities.candle: Utility(
        name=Utilities.candle.name, price=15, vis=1,
        effect='8APT to light, burns 5RND when dropped')
}


class Heads(aenum.AutoNumberEnum):
    empty = ()
    mako_hood = ()

heads = {
    Heads.empty: Head(name=Heads.empty.name),
    Heads.mako_hood: Head(name=Heads.mako_hood.name, mp=2)
}


class Necks(aenum.AutoNumberEnum):
    empty = ()
    mako_amulet = ()

necks = {
    Necks.empty: Neck(name=Necks.empty.name),
    Necks.mako_amulet: Neck(name=Necks.mako_amulet.name, mp=2)
}


class Chests(aenum.AutoNumberEnum):
    empty = ()
    spurclaw_scale = ()

chests = {
    Chests.empty: Chest(name=Chests.empty.name),
    Chests.spurclaw_scale: Chest(name=Chests.spurclaw_scale.name, hp=1)
}


class Shields(aenum.AutoNumberEnum):
    empty = ()
    bronze_buckler = ()

shields = {
    Shields.empty: Shield(name=Shields.empty.name),
    Shields.bronze_buckler: Shield(name=Shields.bronze_buckler.name, hp=1)
}


class Hands(aenum.AutoNumberEnum):
    empty = ()
    bronze_gauntlets = ()

hands = {
    Hands.empty: Hand(name=Hands.empty.name),
    Hands.bronze_gauntlets: Hand(
        name=Hands.bronze_gauntlets.name, pdef=1, is_two_handed=True)
}


class Feets(aenum.AutoNumberEnum):
    empty = ()
    nighthawke_boots = ()

feets = {
    Feets.empty: Feet(name=Feets.empty.name),
    Feets.nighthawke_boots: Feet(name=Feets.nighthawke_boots.name, ste=3)
}


class Weapons(aenum.AutoNumberEnum):
    empty = ()
    fists = ()
    bronze_shuriken = ()

weapons = {
    Weapons.empty: Weapon(name=Weapons.empty.name, picture=WeaponPicture.hands, style=Style.melee),
    Weapons.fists: Weapon(
        name=Weapons.fists.name, picture=WeaponPicture.hands,
        style=Style.melee, is_two_handed=True,
        shape=Shape.melee_point,
        pdam=DiceFormula.from_str('d4'), damage_type=DamageType.bludgeoning),
    Weapons.bronze_shuriken: Weapon(
        name=Weapons.bronze_shuriken.name, picture=WeaponPicture.grey_shuriken,
        style=Style.ranged, is_two_handed=True,
        min_range=1, max_range=6, shape=Shape.range_point,
        attacks=2, pac=0, pdam=DiceFormula.from_str('d4'), damage_type=DamageType.piercing,
        cran=0, cdam=2)
}
