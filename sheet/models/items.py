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
    hopper_scale = ()
    spurclaw_scale = ()
    griffon_hide = ()
    hardened_griffon_hide = ()
    bulletsteel = ()
    ursa_hide = ()
    hardened_ursa_hide = ()
    lunaweave_cloth = ()
    fitted_lunaweave_cloth = ()
    lunasteel_robe = ()
    omni_robe = ()

    bronze_chain = ()
    hardened_bronze_chain = ()
    iron_chain = ()
    hardened_iron_chain = ()
    steel_chain = ()
    hardened_steel_chain = ()
    lunaweave_chain = ()
    hardened_lunaweave_chain = ()
    lunasteel_chain = ()
    hardened_lunasteel_chain = ()
    omni_chain = ()

    bronze_plate = ()
    hardened_bronze_plate = ()
    iron_plate = ()
    hardened_iron_plate = ()
    steel_plate = ()
    hardened_steel_plate = ()
    lunaweave_plate = ()
    hardened_lunaweave_plate = ()
    lunasteel_plate = ()
    hardened_lunasteel_plate = ()
    omni_plate = ()

    cursed_plate = ()
    coral_slate = ()
    volcanic_slate = ()
    lunatech_chest = ()
    lunafiber_robe = ()

chests = {
    # Light.
    Chests.empty: Chest(name=Chests.empty.name),
    Chests.hopper_scale: Chest(name=Chests.hopper_scale.name, price=35, min_str=1, pdef=1,
                               effect='+1PRED vs. Earth, +3ATH when swimming'),
    Chests.spurclaw_scale: Chest(name=Chests.spurclaw_scale.name, price=50, hp=1),
    Chests.griffon_hide: Chest(name=Chests.griffon_hide.name, price=200, min_str=1, pdef=1),
    Chests.hardened_griffon_hide: Chest(name=Chests.hardened_griffon_hide.name, price=200,
                                        min_str=1, hp=2),
    Chests.bulletsteel: Chest(name=Chests.bulletsteel.name, price=500, min_str=2,
                              rarity=Rarity.rare, pdef=1, pred=1, speed=-1),
    Chests.ursa_hide: Chest(name=Chests.ursa_hide.name, price=1000, min_str=2, pdef=2),
    Chests.hardened_ursa_hide: Chest(name=Chests.hardened_ursa_hide.name, price=1000, min_str=2,
                                     pdef=1, hp=2),
    Chests.lunaweave_cloth: Chest(name=Chests.lunaweave_cloth.name, price=3500, min_str=3, pdef=3,
                                  mdef=1),
    Chests.fitted_lunaweave_cloth: Chest(name=Chests.fitted_lunaweave_cloth.name, price=3500,
                                         min_str=3, pdef=2, speed=0.5, mdef=1),
    Chests.lunasteel_robe: Chest(name=Chests.lunasteel_robe.name, price=10000, min_str=4, pdef=4,
                                 speed=1, mdef=2),
    Chests.omni_robe: Chest(name=Chests.omni_robe.name, price=30000, min_str=5, rarity=Rarity.rare,
                            pdef=5, speed=1, stren=1, dex=1, con=1, intel=1, wis=1, cha=1),

    # Medium.
    Chests.bronze_chain: Chest(name=Chests.bronze_chain.name, price=60, equip_type=Type.medium,
                               pdef=1),
    Chests.hardened_bronze_chain: Chest(name=Chests.hardened_bronze_chain.name, price=60,
                                        equip_type=Type.medium, hp=2),
    Chests.iron_chain: Chest(name=Chests.iron_chain.name, price=250, equip_type=Type.medium,
                             min_str=1, pdef=2, hp=1),
    Chests.hardened_iron_chain: Chest(name=Chests.hardened_iron_chain.name, price=250,
                                      equip_type=Type.medium, min_str=1, pdef=1, hp=2),
    Chests.steel_chain: Chest(name=Chests.steel_chain.name, price=1250, equip_type=Type.medium,
                              min_str=2, pdef=3, hp=2),
    Chests.hardened_steel_chain: Chest(name=Chests.hardened_steel_chain.name, price=1250,
                                       equip_type=Type.medium, min_str=2, pdef=2, hp=4),
    Chests.lunaweave_chain: Chest(name=Chests.lunaweave_chain.name, price=4000,
                                  equip_type=Type.medium, min_str=3, pdef=4, pred=0.5, hp=3,
                                  speed=3),
    Chests.hardened_lunaweave_chain: Chest(name=Chests.hardened_lunaweave_chain.name, price=4000,
                                           equip_type=Type.medium, min_str=3, pdef=3, pred=0.5,
                                           hp=6, speed=0.5),
    Chests.lunasteel_chain: Chest(name=Chests.lunasteel_chain.name, price=4000,
                                  equip_type=Type.medium, min_str=4, pdef=5, pred=0.5, hp=4,
                                  speed=0.5, mred=0.5),
    Chests.hardened_lunasteel_chain: Chest(name=Chests.hardened_lunasteel_chain.name, price=12500,
                                           equip_type=Type.medium, min_str=4, pdef=4, pred=0.5,
                                           hp=8, speed=0.5, mred=0.5),
    Chests.omni_chain: Chest(name=Chests.omni_chain.name, price=40000, equip_type=Type.medium,
                             min_str=5, pdef=6, pred=0.5, hp=5, effect='+1 All ability modifiers'),

    # Heavy.
    Chests.bronze_plate: Chest(name=Chests.bronze_plate.name, price=75, equip_type=Type.heavy,
                               pdef=2, hp=1, speed=-0.5),
    Chests.hardened_bronze_plate: Chest(name=Chests.hardened_bronze_plate.name, price=75,
                                        equip_type=Type.heavy, pdef=1, hp=2, speed=-0.5),
    Chests.iron_plate: Chest(name=Chests.iron_plate.name, price=300, equip_type=Type.heavy,
                             min_str=1, pdef=3, pred=0.5, hp=3, speed=-0.5),
    Chests.hardened_iron_plate: Chest(name=Chests.hardened_iron_plate.name, price=300,
                                      equip_type=Type.heavy, min_str=1, pdef=2, pred=0.5, hp=6,
                                      speed=-0.5),
    Chests.steel_plate: Chest(name=Chests.steel_plate.name, price=1500, equip_type=Type.heavy,
                              min_str=2, pdef=3, pred=1, hp=12, speed=-0.5),
    Chests.lunaweave_plate: Chest(name=Chests.lunaweave_plate.name, price=4750,
                                  equip_type=Type.heavy, min_str=3, pdef=5, pred=1, hp=9,
                                  speed=-0.5),
    Chests.hardened_lunaweave_plate: Chest(name=Chests.hardened_lunaweave_plate.name, price=4750,
                                           equip_type=Type.heavy, min_str=3, pdef=4, pred=1,
                                           hp=18, speed=-0.5),
    Chests.lunasteel_plate: Chest(name=Chests.lunasteel_plate.name, price=15000,
                                  equip_type=Type.heavy, min_str=4, pdef=6, pred=1.5, hp=12),
    Chests.hardened_lunasteel_plate: Chest(name=Chests.hardened_lunasteel_plate.name, price=15000,
                                           min_str=4, pdef=5, pred=1.5, hp=24),
    Chests.omni_plate: Chest(name=Chests.omni_plate.name, price=50000, equip_type=Type.heavy,
                             min_str=5, pdef=7, pred=1.5, hp=15, stren=1, dex=1, con=1, intel=1,
                             wis=1, cha=1),

    # Set.
    Chests.cursed_plate: Chest(name=Chests.cursed_plate.name, price=0, min_str=0,
                               rarity=Rarity.set, pdef=-2, bpac=5,
                               effect='Resist corruption 2RND'),
    Chests.coral_slate: Chest(name=Chests.coral_slate.name, price=250, min_str=0,
                              rarity=Rarity.set, pdef=2, hp=1, effect='+1PRED vs. Sanctum'),
    Chests.volcanic_slate: Chest(name=Chests.volcanic_slate.name, price=950, min_str=2,
                                 rarity=Rarity.set, pdef=3, hp=1,
                                 effect='[Counter] Enemies who successfully melee attack take '
                                        '1d4 Fire MDAM'),
    Chests.lunatech_chest: Chest(name=Chests.lunatech_chest.name, price=2750, min_str=4,
                                 rarity=Rarity.set, equip_type=Type.medium, pdef=3, speed=-1,
                                 effect='Amethyste: Take 2StdA per RND.'),
    Chests.lunafiber_robe: Chest(name=Chests.lunafiber_robe.name, price=3850, min_str=3,
                                 rarity=Rarity.set, pdef=1,
                                 effect='-1MP Cost on abilities, +1MP on REG')
}


class Shields(aenum.AutoNumberEnum):
    empty = ()
    bronze_buckler = ()
    iron_buckler = ()
    plated_iron_buckler = ()
    steel_buckler = ()
    plated_steel_buckler = ()
    arachnid_shield = ()
    mithril_shield = ()
    lunaweave_buckler = ()
    plated_lunaweave_buckler = ()
    lunasteel_buckler = ()
    plated_lunasteel_buckler = ()
    omni_buckler = ()

    bronze_kite_shield = ()
    plated_bronze_kite_shield = ()
    bouncer = ()
    iron_kite_shield = ()
    plated_iron_kite_shield = ()
    interlocking_kite_shield = ()
    steel_kite_shield = ()
    plated_steel_kite_shield = ()
    spine_shield = ()
    lunaweave_kite_shield = ()
    plated_lunaweave_kite_shield = ()
    lunasteel_kite_shield = ()
    plated_lunasteel_kite_shield = ()
    omni_kite_shield = ()

    bronze_tower_shield = ()
    plated_bronze_tower_shield = ()
    double_handled_shield = ()
    iron_tower_shield = ()
    plated_iron_tower_shield = ()
    extendable_brace_shield = ()
    the_two_towers = ()
    steel_tower_shield = ()
    plated_steel_tower_shield = ()
    adamantine_shield = ()
    lunaweave_tower_shield = ()
    plated_lunaweave_tower_shield = ()
    lunasteel_tower_shield = ()
    plated_lunasteel_tower_shield = ()
    omni_tower_shield = ()

    cursed_shield = ()
    coral_shield = ()
    volcanic_shield = ()


shields = {
    # Light.
    Shields.empty: Shield(name=Shields.empty.name),
    Shields.bronze_buckler: Shield(name=Shields.bronze_buckler.name, price=40, hp=1),
    Shields.iron_buckler: Shield(name=Shields.iron_buckler.name, price=175, min_str=1, pdef=1,
                                 hp=2),
    Shields.plated_iron_buckler: Shield(name=Shields.plated_iron_buckler.name, price=175,
                                        min_str=1, hp=4),
    Shields.steel_buckler: Shield(name=Shields.steel_buckler.name, price=875, min_str=2, pdef=2,
                                  hp=3),
    Shields.plated_steel_buckler: Shield(name=Shields.plated_steel_buckler.name, price=875,
                                         min_str=2, pdef=1, hp=6),
    Shields.arachnid_shield: Shield(name=Shields.arachnid_shield.name, price=1250, min_str=2,
                                    rarity=Rarity.unique, pdef=2,
                                    effect='After hit with melee attack, attacker is immobilized'),
    Shields.mithril_shield: Shield(name=Shields.mithril_shield.name, price=2650, min_str=3,
                                   rarity=Rarity.rare, hp=1, mdef=3),
    Shields.lunaweave_buckler: Shield(name=Shields.lunaweave_buckler.name, price=3250, min_str=3,
                                      pdef=3, hp=4, effect='Reflect 1PDAM per ATTACK'),
    Shields.plated_lunaweave_buckler: Shield(name=Shields.plated_lunaweave_buckler.name,
                                             price=3250, min_str=3, pdef=2, hp=8,
                                             effect='Reflect 1PDAM per ATTACK'),
    Shields.lunasteel_buckler: Shield(name=Shields.lunasteel_buckler.name, price=8750, min_str=4,
                                      pdef=4, hp=5, effect='Reflect 1 melee ATTACK per RND'),
    Shields.plated_lunasteel_buckler: Shield(name=Shields.plated_lunasteel_buckler.name,
                                             price=8750, min_str=4, pdef=3, hp=10,
                                             effect='Reflect 1 melee ATTACK per RND'),
    Shields.omni_buckler: Shield(name=Shields.omni_buckler.name, price=12500, min_str=5,
                                 rarity=Rarity.rare, pdef=5, hp=6),

    # Medium.
    Shields.bronze_kite_shield: Shield(name=Shields.bronze_kite_shield.name, price=50, min_str=0,
                                       equip_type=Type.medium, pdef=1, hp=1),
    Shields.plated_bronze_kite_shield: Shield(name=Shields.plated_bronze_kite_shield.name,
                                              price=50, min_str=0, equip_type=Type.medium, hp=2),
    Shields.bouncer: Shield(name=Shields.bouncer.name, price=85, min_str=0,
                            equip_type=Type.medium, rarity=Rarity.rare, hp=2,
                            effect='When enemy fumbles a physical attack against you, damage is '
                                   'applied to enemy'),
    Shields.iron_kite_shield: Shield(name=Shields.iron_kite_shield.name, price=200, min_str=1,
                                     equip_type=Type.medium, pdef=2, hp=2),
    Shields.plated_iron_kite_shield: Shield(name=Shields.plated_iron_kite_shield.name, price=200,
                                            equip_type=Type.medium, pdef=1, hp=4),
    Shields.interlocking_kite_shield: Shield(name=Shields.interlocking_kite_shield.name,
                                             price=450, min_str=1, equip_type=Type.medium,
                                             rarity=Rarity.rare, pdef=2, hp=2,
                                             effect='If adjacent ally is equipping Interlocking '
                                                    'Kite Shield, +1PRED'),
    Shields.steel_kite_shield: Shield(name=Shields.steel_kite_shield.name, price=1000, min_str=2,
                                      pdef=3, hp=3),
    Shields.plated_steel_kite_shield: Shield(name=Shields.plated_steel_kite_shield.name,
                                             price=1000, min_str=2, pdef=2, hp=6),
    Shields.spine_shield: Shield(name=Shields.spine_shield.name, price=1250, min_str=2, pdef=2,
                                 effect='[Counter] After enemy hits melee attack, enemy takes 1d4 '
                                        'PDAM'),
    Shields.lunaweave_kite_shield: Shield(name=Shields.lunaweave_kite_shield.name, price=3500,
                                          min_str=3, equip_type=Type.medium, rarity=Rarity.rare,
                                          pdef=4, hp=4, effect='Reflect 1PDAM per attack'),
    Shields.plated_lunaweave_kite_shield: Shield(name=Shields.plated_lunaweave_kite_shield.name,
                                                 price=3500, min_str=3, pdef=3, hp=8,
                                                 effect='Reflect 1PDAM per attack'),
    Shields.lunasteel_kite_shield: Shield(name=Shields.lunasteel_kite_shield.name, price=10000,
                                          min_str=4, equip_type=Type.medium, pdef=5, hp=5,
                                          effect='Reflect 1 melee attack per RND'),
    Shields.plated_lunasteel_kite_shield: Shield(name=Shields.plated_lunasteel_kite_shield.name,
                                                 price=10000, min_str=4, equip_type=Type.medium,
                                                 pdef=4, hp=10,
                                                 effect='Reflect 1 melee attack per RND'),
    Shields.omni_kite_shield: Shield(name=Shields.omni_kite_shield.name, price=18000, min_str=5,
                                     equip_type=Type.medium, pdef=6, hp=6),

    # Heavy.
    Shields.bronze_tower_shield: Shield(name=Shields.bronze_tower_shield.name, price=75,
                                        equip_type=Type.heavy, pdef=1, hp=3),
    Shields.plated_bronze_tower_shield: Shield(name=Shields.plated_bronze_tower_shield.name,
                                               price=100, equip_type=Type.heavy, hp=6),
    Shields.double_handled_shield: Shield(name=Shields.plated_bronze_tower_shield.name, price=150,
                                          equip_type=Type.heavy, rarity=Rarity.rare, hp=6,
                                          effect='Can spend StdA to grant +1PRED for 1RND'),
    Shields.iron_tower_shield: Shield(name=Shields.iron_tower_shield.name, price=250, min_str=1,
                                      equip_type=Type.heavy, pdef=2, hp=6),
    Shields.plated_iron_tower_shield: Shield(name=Shields.plated_iron_tower_shield.name, price=300,
                                             min_str=1, equip_type=Type.heavy, pdef=1, hp=12),
    Shields.extendable_brace_shield: Shield(name=Shields.extendable_brace_shield.name, price=500,
                                            min_str=1, equip_type=Type.heavy, rarity=Rarity.rare,
                                            pdef=2, hp=6,
                                            effect='Shield can extend 1DIS to left and right, '
                                                   'making it impassable to enemies'),
    Shields.the_two_towers: Shield(name=Shields.the_two_towers.name, price=850, min_str=1,
                                   equip_type=Type.heavy, rarity=Rarity.rare, pdef=1, hp=12,
                                   mdef=2),
    Shields.steel_tower_shield: Shield(name=Shields.steel_tower_shield.name, price=1250,
                                       min_str=2, equip_type=Type.heavy, pdef=3, hp=9),
    Shields.plated_steel_tower_shield: Shield(name=Shields.plated_steel_tower_shield.name,
                                              price=1500, min_str=2, equip_type=Type.heavy,
                                              pdef=2, hp=18),
    Shields.adamantine_shield: Shield(name=Shields.adamantine_shield.name, price=1350,
                                      min_str=2, equip_type=Type.heavy, rarity=Rarity.rare,
                                      pdef=2, hp=6,
                                      effect='Absorb 1MDAM into MP per magic attack'),
    Shields.lunaweave_tower_shield: Shield(name=Shields.lunaweave_tower_shield.name, price=4000,
                                           min_str=3, equip_type=Type.heavy, pdef=4, hp=12,
                                           effect='Reflect 1PDAM per attack'),
    Shields.plated_lunaweave_tower_shield: Shield(name=Shields.plated_lunaweave_tower_shield.name,
                                                  price=4750, min_str=3, equip_type=Type.heavy,
                                                  pdef=3, hp=24,
                                                  effect='Reflect 1PDAM per attack'),
    Shields.lunasteel_tower_shield: Shield(name=Shields.lunasteel_tower_shield.name, price=12500,
                                           min_str=4, pdef=5, hp=15,
                                           effect='Reflect 1 ATTACK per RND'),
    Shields.plated_lunasteel_tower_shield: Shield(name=Shields.plated_lunasteel_tower_shield.name,
                                                  price=12500, min_str=4, equip_type=Type.heavy,
                                                  pdef=4, hp=28,
                                                  effect='Reflect 1 ATTACK per RND'),
    Shields.omni_tower_shield: Shield(name=Shields.omni_tower_shield.name, price=30000, min_str=5,
                                      equip_type=Type.heavy, rarity=Rarity.rare, pdef=6, hp=18),

    # Set.
    Shields.cursed_shield: Shield(name=Shields.cursed_shield.name, price=0, min_str=0,
                                  rarity=Rarity.set,
                                  effect='[Counter] 2MDAM to attacker on hit, Resist corruption '
                                         '2RND'),
    Shields.coral_shield: Shield(name=Shields.coral_shield.name, price=225, min_str=1, hp=2,
                                 rarity=Rarity.set, effect='Reflect 1PDAM vs. Water'),
    Shields.volcanic_shield: Shield(name=Shields.volcanic_shield.name, price=1375, min_str=2,
                                    rarity=Rarity.set, pdef=1, hp=3, mdef=2,
                                    effect='Absorb 2MDAM as MP when hit with Fire Magic attack'),
}


class Hands(aenum.AutoNumberEnum):
    empty = ()
    bronze_gauntlets = ()
    adamantine_ring = ()
    mako_ring = ()
    lunaweave_ring = ()
    locking_glove = ()
    gill_ring = ()
    fencing_glove = ()
    emerald_ring = ()
    fire_ring = ()
    iron_gauntlets = ()
    universal_donor = ()
    ruby_ring = ()
    feather_glove = ()
    reinforced_bangle = ()
    ring_of_regen = ()
    stone_ring = ()
    diamond_ring = ()
    diamond_bangles = ()
    colossus_armlet = ()
    ring_of_communication = ()
    shield_bearer = ()
    stabilizer = ()
    steel_gauntlets = ()
    titan_joint = ()
    dueling_glove = ()
    slotted_gauntlet = ()

    coral_gauntlets = ()
    volcanic_gauntlets = ()
    lunatech_gauntlets = ()
    obsidian_gauntlets = ()
    lunafiber_glove = ()


hands = {
    Hands.empty: Hand(name=Hands.empty.name),
    Hands.bronze_gauntlets: Hand(name=Hands.bronze_gauntlets.name, price=50, pdef=1,
                                 is_two_handed=True, equip_type=Type.medium),
    Hands.adamantine_ring: Hand(name=Hands.adamantine_ring.name, price=60, mdef=1),
    Hands.mako_ring: Hand(name=Hands.mako_ring.name, price=60, mp=2),
    Hands.lunaweave_ring: Hand(name=Hands.lunaweave_ring.name, price=75, bmac=1),
    Hands.locking_glove: Hand(name=Hands.locking_glove.name, price=200, min_cha=1,
                              effect='+3ATH when grappling'),
    Hands.gill_ring: Hand(name=Hands.gill_ring.name, price=250, min_cha=1, rarity=Rarity.rare,
                          effect='Water breathing'),
    Hands.fencing_glove: Hand(name=Hands.fencing_glove.name, price=250, min_cha=1, bpac=1),
    Hands.emerald_ring: Hand(name=Hands.emerald_ring.name, price=350, min_cha=1, hp=5),
    Hands.fire_ring: Hand(name=Hands.fire_ring.name, price=375, min_cha=1, effect='FireRES'),
    Hands.iron_gauntlets: Hand(name=Hands.iron_gauntlets.name, price=450, min_cha=2,
                               equip_type=Type.medium, is_two_handed=True, pdef=2),
    Hands.universal_donor: Hand(name=Hands.universal_donor.name, price=750, min_cha=2,
                                rarity=Rarity.unique, rd=1, mp=2),
    Hands.ruby_ring: Hand(name=Hands.ruby_ring.name, price=1000, min_cha=2, pdef=-1,
                          effect='+1PDAM on melee weapon in hand'),
    Hands.feather_glove: Hand(name=Hands.feather_glove.name, price=1100, min_cha=2,
                              effect='+3Range on Ranged Weapons'),
    Hands.reinforced_bangle: Hand(name=Hands.reinforced_bangle.name, price=1150, min_cha=2,
                                  equip_type=Type.medium, effect='-1 Min DEX on hand'),
    Hands.ring_of_regen: Hand(name=Hands.ring_of_regen.name, price=1200, min_cha=2,
                              effect='+1HP per 2RND in combat'),
    Hands.stone_ring: Hand(name=Hands.stone_ring.name, price=1200, min_cha=2, pred=1, speed=-0.5),
    Hands.diamond_ring: Hand(name=Hands.diamond_ring.name, price=1200, min_cha=2, bpac=6,
                             effect='-2PDAM'),
    Hands.diamond_bangles: Hand(name=Hands.diamond_bangles.name, price=1350, min_cha=2,
                                equip_type=Type.heavy, is_two_handed=True,
                                effect='Reflect 1PDAM when hit with melee'),
    Hands.colossus_armlet: Hand(name=Hands.colossus_armlet.name, price=1400, min_cha=2,
                                equip_type=Type.heavy, rarity=Rarity.rare, is_two_handed=True,
                                bpac=2,
                                effect='Can equip one handed melee weapon as if 2-handed for '
                                       '+1d4 PDAM'),
    Hands.ring_of_communication: Hand(name=Hands.ring_of_communication.name, price=1450,
                                      min_cha=2, rarity=Rarity.rare,
                                      effect='Ring allow wearers of a pair to communicate at a '
                                             'distance'),
    Hands.shield_bearer: Hand(name=Hands.shield_bearer.name, price=1500, equip_type=Type.medium,
                              is_two_handed=True, effect='Allows use of heavy shields'),
    Hands.stabilizer: Hand(name=Hands.stabilizer.name, price=1500, min_cha=2,
                           equip_type=Type.medium, effect='+1CRAN on firearm in hand'),
    Hands.steel_gauntlets: Hand(name=Hands.steel_gauntlets.name, price=1500, min_cha=2,
                                equip_type=Type.heavy, is_two_handed=True, pdef=3),
    Hands.titan_joint: Hand(name=Hands.titan_joint.name, price=1650, min_cha=2,
                            equip_type=Type.heavy, rarity=Rarity.rare, is_two_handed=True,
                            effect='Can equip 2-handed weapon and a shield'),
    Hands.dueling_glove: Hand(name=Hands.dueling_glove.name, price=200, min_cha=1, reg=1,
                              effect='Marksman only'),
    Hands.slotted_gauntlet: Hand(name=Hands.slotted_gauntlet.name, price=650, min_cha=2,
                                 effect='Marksman only, +1ATTACK on one handed firearm'),

    # Set.
    Hands.coral_gauntlets: Hand(name=Hands.coral_gauntlets.name, price=400, min_cha=1,
                                rarity=Rarity.set, is_two_handed=True, effect='+1MRED vs. Water'),
    Hands.volcanic_gauntlets: Hand(name=Hands.volcanic_gauntlets.name, price=725, min_cha=1,
                                   rarity=Rarity.set, is_two_handed=True,
                                   effect='Add 1d4 Fire MDAM to melee and ranged attacks'),
    Hands.lunatech_gauntlets: Hand(name=Hands.lunatech_gauntlets.name, price=1850, min_cha=2,
                                   equip_type=Type.medium, rarity=Rarity.set, is_two_handed=True,
                                   mdef=4,
                                   effect='Sapphire: successful MDEF reflects magic attack'),
    Hands.obsidian_gauntlets: Hand(name=Hands.obsidian_gauntlets.name, price=1850, min_cha=2,
                                   rarity=Rarity.set, is_two_handed=True, mdef=5, bmac=-8),
    Hands.lunafiber_glove: Hand(name=Hands.lunafiber_glove.name, price=2500, min_cha=2,
                                rarity=Rarity.set, reg=5, mp=10, ap=1),
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
