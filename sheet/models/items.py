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
                            rarity=Rarity.set, effect='+2PDAM per ATTACK. Resist corruption 2RND'),
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
    spinal_support = ()
    crystal_amulet = ()
    starlet_necklace = ()
    heavy_quiver = ()
    equalizer = ()
    ammo_sash = ()
    foregrip = ()
    adamantine_amulet = ()
    range_finder = ()
    suppressor = ()
    duraform_pendant = ()
    lunavein_necklace = ()
    long_barrel = ()
    lunahollow_necklace = ()
    overcharge_amulet = ()
    emerald_amulet = ()
    mithril_riviere = ()
    lunaburn_amulet = ()
    sapphire_amulet = ()
    obsidian_necklace = ()
    augmenter = ()
    mithril_amulet = ()
    omni_amulet = ()

necks = {
    Necks.empty: Neck(name=Necks.empty.name),
    Necks.mako_amulet: Neck(name=Necks.mako_amulet.name, price=100, mp=2),
    Necks.spinal_support: Neck(name=Necks.spinal_support.name, price=200, min_wis=1,
                               equip_type=Type.medium, effect='-1 Min STR on chest'),
    Necks.crystal_amulet: Neck(name=Necks.crystal_amulet.name, price=350, min_wis=1, reg=2),
    Necks.starlet_necklace: Neck(name=Necks.starlet_necklace.name, price=350, min_wis=1,
                                 effect='When ability crits, it consumes no MP and grants +4MP'),
    Necks.heavy_quiver: Neck(name=Necks.heavy_quiver.name, price=400, min_wis=1,
                             effect='Allows use of heavy range weapons'),
    Necks.equalizer: Neck(name=Necks.equalizer.name, price=400, min_wis=1, reg=-18,
                          rarity=Rarity.rare, effect='RD is d1'),
    Necks.ammo_sash: Neck(name=Necks.ammo_sash.name, price=650, min_wis=2,
                          effect='+1ATTACK on Reaper, Marksman only'),
    Necks.foregrip: Neck(name=Necks.foregrip.name, price=675, min_wis=1, bpac=2,
                         effect='Can only be used on firearms. Marksman only.'),
    Necks.adamantine_amulet: Neck(name=Necks.adamantine_amulet.name, price=750, min_wis=2, ap=1),
    Necks.range_finder: Neck(name=Necks.range_finder.name, price=750, min_wis=2,
                             effect='+4Range on rifles, Marksman only'),
    Necks.suppressor: Neck(name=Necks.suppressor.name, price=850, min_wis=2,
                           effect='Muffles ignition of firearm, can only be heard within 3DIS, '
                                  'Marksman only'),
    Necks.duraform_pendant: Neck(name=Necks.duraform_pendant.name, price=950, min_wis=2,
                                 effect='+6REG is no movement taken that RND'),
    Necks.lunavein_necklace: Neck(name=Necks.lunavein_necklace.name, price=1250, min_wis=2,
                                  effect='On hit, ignore 2PDAM by consuming 2MP'),
    Necks.long_barrel: Neck(name=Necks.long_barrel.name, price=975, min_wis=2,
                            effect='+1Range on shotgun, Marksman only'),
    Necks.lunahollow_necklace: Neck(name=Necks.lunahollow_necklace.name, price=1250, min_wis=0,
                                    rarity=Rarity.rare,
                                    effect='Slots a ring and applies its effect to the slot,'
                                           'Min WIS = 2x Min CHA on ring'),
    Necks.overcharge_amulet: Neck(name=Necks.overcharge_amulet.name, price=1300, min_wis=2,
                                  rarity=Rarity.rare,
                                  effect='Cast ability at +1 Ability LVL for +50% MP cost'),
    Necks.emerald_amulet: Neck(name=Necks.emerald_amulet.name, price=1300, min_wis=2,
                               effect='On successful REG, recover HP instead of MP'),
    Necks.mithril_riviere: Neck(name=Necks.mithril_riviere.name, price=1450, min_wis=2,
                                effect='When casting an ability that misses, ignore MP cost and '
                                       'recover +2MP'),
    Necks.lunaburn_amulet: Neck(name=Necks.lunaburn_amulet.name, price=1700, min_wis=2, bmac=-4,
                                effect='Abilities always crit, 2x MP Cost on abilities'),
    Necks.sapphire_amulet: Neck(name=Necks.sapphire_amulet.name, price=1850, min_wis=2,
                                rarity=Rarity.rare,
                                effect='Use MRED instead of PRED to reduce physical attack '
                                       'damage'),
    Necks.obsidian_necklace: Neck(name=Necks.obsidian_necklace.name, price=1850, min_wis=2,
                                  rarity=Rarity.set, reg=-10, mred=3),
    Necks.augmenter: Neck(name=Necks.augmenter.name, price=3250, min_wis=3, rarity=Rarity.unique,
                          equip_type=Type.medium,
                          effect='On successful physical ATTACK, can spend 2MP to do 4MDAM'),
    Necks.mithril_amulet: Neck(name=Necks.mithril_amulet.name, price=10000, min_wis=4,
                               rarity=Rarity.rare, effect='-1 MP Cost to all abilities'),
    Necks.omni_amulet: Neck(name=Necks.omni_amulet.name, price=20000, min_wis=5,
                            rarity=Rarity.rare, effect='+1 Ability LVL to all abilities')
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
