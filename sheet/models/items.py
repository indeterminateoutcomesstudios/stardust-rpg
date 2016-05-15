#!/usr/bin/env python3

import aenum

from .dice import DiceFormula
from .equipment import (Chest, DamageType, Feet, Hand, Head, Item, Neck, Rarity, Shape, Shield,
                        Style, Type, Utility, Weapon, WeaponPicture)


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
    cursed_helm = ()
    mako_hood = ()
    adept_hood = ()
    adamantine_circlet = ()
    hero_mask = ()
    mako_helm = ()
    techno_eyepiece = ()
    apprentice_helm = ()
    lunafabric_hood = ()
    telescoping_lenses = ()
    volcanic_helm = ()
    rusty_bucket = ()
    circlet_of_healing = ()
    circlet_of_power = ()
    circlet_of_telepathy = ()
    mako_guard = ()
    mithril_earrings = ()
    mithril_headband = ()
    adamantine_helmet = ()
    avenger_circlet = ()
    sapphire_circlet = ()
    obsidian_tiara = ()
    lunatech_helm = ()
    lunafiber_hood = ()
    lunaburn_circlet = ()
    mithril_tiara = ()
    mithril_coronet = ()

heads = {
    Heads.empty: Head(name=Heads.empty.name),
    Heads.cursed_helm: Head(name=Heads.cursed_helm.name, price=0, min_int=0, reg=2,
                            rarity=Rarity.set, effect='+2PDAM per ATT. Resist corruption 2RND'),
    Heads.mako_hood: Head(name=Heads.mako_hood.name, price=50, mp=2),
    Heads.adept_hood: Head(name=Heads.adept_hood.name, price=125, reg=1),
    Heads.adamantine_circlet: Head(name=Heads.adamantine_circlet.name, price=125, mdef=1),
    Heads.hero_mask: Head(name=Heads.hero_mask.name, price=350, min_int=1,
                          effect='+5STE when disguising, +5 SPE with common'),
    Heads.mako_helm: Head(name=Heads.mako_helm.name, price=450, min_int=1, bmac=1),
    Heads.techno_eyepiece: Head(name=Heads.techno_eyepiece.name, price=450, min_int=1,
                                effect='See in low light, Dwarf only'),
    Heads.apprentice_helm: Head(name=Heads.apprentice_helm.name, price=500, min_int=1, ap=1),
    Heads.lunafabric_hood: Head(name=Heads.lunafabric_hood.name, price=550, min_int=1, mp=12,
                                reg=-3),
    Heads.telescoping_lenses: Head(name=Heads.telescoping_lenses.name, price=550, min_int=1,
                                   effect='+8Range on Siege Tech, Dwarf only'),
    Heads.volcanic_helm: Head(name=Heads.volcanic_helm.name, price=800, min_int=1, bmac=1,
                              rarity=Rarity.set, effect='+1 Fire MDAM to Fire Magic'),
    Heads.rusty_bucket: Head(name=Heads.rusty_bucket.name, price=1000, min_int=2,
                             rarity=Rarity.unique, ap=3, vis=-1, per=-1),
    Heads.circlet_of_healing: Head(name=Heads.circlet_of_healing.name, price=1200, min_int=2,
                                   rarity=Rarity.rare, effect='+2HP to healing abilities'),
    Heads.circlet_of_power: Head(name=Heads.circlet_of_power.name, price=1350, min_int=2,
                                 rarity=Rarity.rare, effect='+2MDAM to telekinetic abilities'),
    Heads.circlet_of_telepathy: Head(name=Heads.circlet_of_telepathy.name, price=1350, min_int=2,
                                     rarity=Rarity.rare,
                                     effect='+1RND Duration on telepathic abilities'),
    Heads.mako_guard: Head(name=Heads.mako_guard.name, price=1150, min_int=2, bmac=2, mdef=2),
    Heads.mithril_earrings: Head(name=Heads.mithril_earrings.name, price=1450, min_int=2,
                                 effect='+2RAD on abilities'),
    Heads.mithril_headband: Head(name=Heads.mithril_headband.name, price=1250, min_int=2,
                                 effect='+3Range on abilities'),
    Heads.adamantine_helmet: Head(name=Heads.adamantine_helmet.name, price=1350, min_int=2,
                                  equip_type=Type.medium, mred=1),
    Heads.avenger_circlet: Head(name=Heads.avenger_circlet.name, price=1500, min_int=2,
                                rarity=Rarity.rare, effect='When below 25% maximum HP, REG 2x MP'),
    Heads.sapphire_circlet: Head(name=Heads.sapphire_circlet.name, price=1850, min_int=2,
                                 effect='Use MDEF instead of PDEF to defend physical attacks'),
    Heads.obsidian_tiara: Head(name=Heads.obsidian_tiara.name, price=1850, min_int=2, mdef=2,
                               mred=2, rarity=Rarity.set, effect='0 Max MP'),
    Heads.lunatech_helm: Head(name=Heads.lunatech_helm.name, price=1600, min_int=3,
                              equip_type=Type.medium, rarity=Rarity.set,
                              effect='Ruby: Adds 1d4 MDAM to weapon, critical hit adds 1d20 Fire '
                                     'MDAM'),
    Heads.lunafiber_hood: Head(name=Heads.lunafiber_hood.name, price=2400, min_int=2, mred=1,
                               rarity=Rarity.set,
                               effect='+1RAD and +1Range to abilities, +1 to ability rolls'),
    Heads.lunaburn_circlet: Head(name=Heads.lunaburn_circlet.name, price=2450, min_int=3,
                                 effect='Can cast an ability that requires a StdA as a FreeA for '
                                        '+100% MP Cost'),
    Heads.mithril_tiara: Head(name=Heads.mithril_tiara.name, price=2700, min_int=3,
                              effect='+1RND Duration on abilities'),
    Heads.mithril_coronet: Head(name=Heads.mithril_coronet.name, price=2850, min_int=3,
                                effect='+1d6 MDAM to to abilities that cause MDAM'),
}


class Necks(aenum.AutoNumberEnum):
    empty = ()
    mako_amulet = ()

necks = {
    Necks.empty: Neck(name=Necks.empty.name),
    Necks.mako_amulet: Neck(name=Necks.mako_amulet.name, price=100, mp=2)
}


class Chests(aenum.AutoNumberEnum):
    empty = ()
    spurclaw_scale = ()

chests = {
    Chests.empty: Chest(name=Chests.empty.name),
    Chests.spurclaw_scale: Chest(name=Chests.spurclaw_scale.name, price=50, hp=1)
}


class Shields(aenum.AutoNumberEnum):
    empty = ()
    bronze_buckler = ()

shields = {
    Shields.empty: Shield(name=Shields.empty.name),
    Shields.bronze_buckler: Shield(name=Shields.bronze_buckler.name, price=40, hp=1)
}


class Hands(aenum.AutoNumberEnum):
    empty = ()
    bronze_gauntlets = ()

hands = {
    Hands.empty: Hand(name=Hands.empty.name),
    Hands.bronze_gauntlets: Hand(
        name=Hands.bronze_gauntlets.name, price=50, pdef=1, is_two_handed=True)
}


class Feets(aenum.AutoNumberEnum):
    empty = ()
    nighthawke_boots = ()

feets = {
    Feets.empty: Feet(name=Feets.empty.name),
    Feets.nighthawke_boots: Feet(name=Feets.nighthawke_boots.name, price=100, ste=3)
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
        name=Weapons.bronze_shuriken.name, price=40, picture=WeaponPicture.grey_shuriken,
        style=Style.ranged, is_two_handed=True,
        min_range=1, max_range=6, shape=Shape.range_point,
        attacks=2, pac=0, pdam=DiceFormula.from_str('d4'), damage_type=DamageType.piercing,
        cran=0, cdam=2)
}


class Items(aenum.AutoNumberEnum):
    empty = ()
    disguise_kit = ()

items = {
    Items.empty: Item(name=Items.empty.name, effect=''),
    Items.disguise_kit: Item(name=Items.disguise_kit.name, price=5,
                             effect='Allows Disguise Self check')
}
