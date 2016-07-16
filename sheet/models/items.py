import aenum

from .dice import DiceFormula
from .equipment import (Chest, DamageType, DamageTypeSet, Feet, Hand, Head, Item, Neck, Rarity,
                        Shape, Shield, Style, Type, Utility, VulnerabilitySet, Weapon,
                        WeaponPicture)


class Utilities(aenum.AutoNumberEnum):
    empty = ()
    candle = ()
    rope_kit = ()
    crowbar = ()
    hammer = ()
    pickaxe = ()
    tinder_box = ()
    fishing_net = ()
    harp = ()
    mandolin = ()
    bugle = ()
    snorkle = ()
    torch = ()
    medical_kit = ()
    grappling_hook = ()
    gliding_suit = ()
    communication_orb = ()
    repelling_gear = ()
    bow_cable = ()
    magnifying_glass = ()
    binoculars = ()
    lantern = ()
    spider_gloves = ()
    flare_gun = ()
    grappling_gun = ()
    detect_realm = ()
    dwarven_crystal_lantern = ()
    mirrored_lunacite_lantern = ()


utilities = {
    Utilities.empty: Utility(name=Utilities.empty.name),
    Utilities.candle: Utility(name=Utilities.candle.name, price=15,
                              effect='8APT to light, lights 1VIS for 5RND when dropped'),
    Utilities.rope_kit: Utility(name=Utilities.rope_kit.name, price=25,
                                effect='Kit of various size/length rope'),
    Utilities.crowbar: Utility(name=Utilities.crowbar.name, price=50,
                               effect='Used to wedge open tight corners'),
    Utilities.hammer: Utility(name=Utilities.hammer.name, price=50,
                              effect='Can drive in small objects'),
    Utilities.pickaxe: Utility(name=Utilities.pickaxe.name, price=50,
                               effect='Can dig into the ground for ore or other objects'),
    Utilities.tinder_box: Utility(name=Utilities.tinder_box.name, price=55,
                                  effect='Starts a fire'),
    Utilities.fishing_net: Utility(name=Utilities.fishing_net.name, price=65,
                                   effect='Catches medium fish'),
    Utilities.harp: Utility(name=Utilities.harp.name, price=150,
                            effect='A soothing musical instrument'),
    Utilities.mandolin: Utility(name=Utilities.mandolin.name, price=150,
                                effect='A cheerful musical instrument'),
    Utilities.bugle: Utility(name=Utilities.bugle.name, price=150,
                             effect='A rousing musical instrument'),
    Utilities.snorkle: Utility(name=Utilities.snorkle.name, price=160,
                               effect='Allows breathing while face is submerged'),
    Utilities.torch: Utility(name=Utilities.torch.name, price=200, min_int=1,
                             effect='10APT to light, lights 2VIS for 10RND when dropped'),
    Utilities.medical_kit: Utility(name=Utilities.medical_kit.name, price=250, min_int=1,
                                   effect="13APT revives adjacent KO'd ally to 1HP"),
    Utilities.grappling_hook: Utility(name=Utilities.grappling_hook.name, price=350, min_int=1,
                                      effect='Iron grapple attached to 8DIS of rope.  Can be '
                                             'thrown to attach to fixtures'),
    Utilities.gliding_suit: Utility(name=Utilities.gliding_suit.name, price=450, min_int=1,
                                    equip_type=Type.medium, rarity=Rarity.rare,
                                    effect='Allows gliding flight'),
    Utilities.communication_orb: Utility(name=Utilities.communication_orb.name, price=500,
                                         min_int=1, rarity=Rarity.rare,
                                         effect='Paried with another communication orb, allows '
                                                'communication at great distance'),
    Utilities.repelling_gear: Utility(name=Utilities.repelling_gear.name, price=500, min_int=1,
                                      effect='Allows repelling down a wall or cliff'),
    Utilities.bow_cable: Utility(name=Utilities.bow_cable.name, price=500, min_int=1,
                                 equip_type=Type.medium,
                                 effect='Crossbow fires a cable up to 12DIS which attaches to '
                                        'surface.  Cable can be ziplined on.'),
    Utilities.magnifying_glass: Utility(name=Utilities.magnifying_glass.name, price=600, min_int=1,
                                        effect='Magnifies vision of small objects'),
    Utilities.binoculars: Utility(name=Utilities.binoculars.name, price=650, min_int=1,
                                  effect='Allows PER at long distances'),
    Utilities.lantern: Utility(name=Utilities.lantern.name, price=1000, min_int=2,
                               effect='12APT to light, lights 3VIS for 20RND when dropped'),
    Utilities.spider_gloves: Utility(name=Utilities.spider_gloves.name, price=1000, min_int=2,
                                     rarity=Rarity.rare,
                                     effect='Wall Climbing, -4SPEED while wall climbing'),
    Utilities.flare_gun: Utility(name=Utilities.flare_gun.name, price=1250, min_int=2,
                                 rarity=Rarity.rare,
                                 effect='Fires a bright red flare, +3VIS on target at 10 Range '
                                        'for 2RND'),
    Utilities.grappling_gun: Utility(name=Utilities.grappling_gun.name, price=2250, min_int=3,
                                     effect='Attaches to surface at range 12DIS and pulls Med '
                                            'creature to it'),
    Utilities.detect_realm: Utility(name=Utilities.detect_realm.name, price=2250, min_int=3,
                                    rarity=Rarity.rare,
                                    effect='Configured to detect creatures of a certain realm '
                                           'within 12DIS'),
    Utilities.dwarven_crystal_lantern: Utility(name=Utilities.dwarven_crystal_lantern.name,
                                               price=2250, min_int=3, rarity=Rarity.rare,
                                               effect='14APT to light, lights 4VIS 50RND when '
                                                      'dropped'),
    Utilities.mirrored_lunacite_lantern: Utility(name=Utilities.mirrored_lunacite_lantern.name,
                                                 price=8500, min_int=4, rarity=Rarity.rare,
                                                 effect='16APT to light, lights tVIS forever when '
                                                        'dropped')
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
    Necks.equalizer: Neck(name=Necks.equalizer.name, price=400, min_wis=1, reg=18,
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
    Hands.fire_ring: Hand(name=Hands.fire_ring.name, price=375, min_cha=1,
                          vul_set=VulnerabilitySet(res=DamageTypeSet(fire=True))),
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
    spiked_soles = ()
    iron_brackets = ()
    fencing_boots = ()
    tender_soles = ()
    fortified_greaves = ()
    flippers = ()
    claw_shoes = ()
    reflex_soles = ()
    juggernaut_greaves = ()
    racers = ()
    sprinting_shoes = ()
    trailblazers = ()
    dodgers = ()
    inertial_helix = ()
    three_heroes = ()
    lunabeam_walkers = ()
    ocean_striders = ()
    cloud_walkers = ()
    gyro_heels = ()
    earth_clamps = ()
    whirlwind_greaves = ()
    rebound_greaves = ()
    skywalker_boots = ()
    wind_boots = ()
    topaz_slippers = ()
    wind_striders = ()
    flashers = ()
    ocean_born = ()
    mithril_boots = ()
    grooved_soles = ()
    cursed_greaves = ()
    coral_greaves = ()
    volcanic_greaves = ()
    lunatech_boots = ()
    lunafiber_slippers = ()


feets = {
    Feets.empty: Feet(name=Feets.empty.name),
    Feets.nighthawke_boots: Feet(name=Feets.nighthawke_boots.name, price=100, ste=3),
    Feets.spiked_soles: Feet(name=Feets.spiked_soles.name, price=100, ath=3),
    Feets.iron_brackets: Feet(name=Feets.iron_brackets.name, price=125,
                              effect='Immune to knockback'),
    Feets.fencing_boots: Feet(name=Feets.fencing_boots.name, price=200,
                              effect='Enemies diagonally adjacent can be targetted as if they '
                                     'were 1DIS away'),
    Feets.tender_soles: Feet(name=Feets.tender_soles.name, price=200, min_str=1,
                             effect='+6STE vs. Detect Trap'),
    Feets.fortified_greaves: Feet(name=Feets.fortified_greaves.name, price=250, min_str=1,
                                  equip_type=Type.heavy, effect='Ignore SPEED penalty on Chest '
                                                                'armor'),
    Feets.flippers: Feet(name=Feets.flippers.name, price=350, min_str=1,
                         effect='+5ATH while swimming'),
    Feets.claw_shoes: Feet(name=Feets.claw_shoes.name, price=350, min_str=1,
                           effect='+5ATH while climbing'),
    Feets.reflex_soles: Feet(name=Feets.reflex_soles.name, price=350, min_str=1,
                             effect='Can spend 3SPEED to jump 3DIS'),
    Feets.juggernaut_greaves: Feet(name=Feets.juggernaut_greaves.name, price=350, min_str=1,
                                   equip_type=Type.heavy, rarity=Rarity.rare,
                                   effect='Spending all SPEED moving in a straight line ending '
                                          'by hitting an enemy deals 1*SPEED PDAM and knocks back '
                                          '1DIS'),
    Feets.racers: Feet(name=Feets.racers.name, price=375, min_str=1,
                       effect='Spend StdA and AbA to move at +3SPEED for 1RND'),
    Feets.sprinting_shoes: Feet(name=Feets.sprinting_shoes.name, price=400, min_str=1, speed=0.5),
    Feets.trailblazers: Feet(name=Feets.trailblazers.name, price=450, min_str=1,
                             rarity=Rarity.unique,
                             effect='Activating leaves a trail of fire dealing 3MDAM to creatures '
                                    'moving across the path for 1RND'),
    Feets.dodgers: Feet(name=Feets.dodgers.name, price=450, min_str=1,
                        effect='When hit with an area of effect attack, can move up to 2DIS to '
                               'avoid the area.  If avoided, immune to effect.'),
    Feets.inertial_helix: Feet(name=Feets.inertial_helix.name, price=450, min_str=1,
                               effect='+3SPEED for 1RND if moving in a straight line'),
    Feets.three_heroes: Feet(name=Feets.three_heroes.name, price=500, min_str=1,
                             rarity=Rarity.unique,
                             effect='+1SPEED per adjecent ally wearing Three Heroes'),
    Feets.lunabeam_walkers: Feet(name=Feets.lunabeam_walkers.name, price=950, min_str=2,
                                 equip_type=Type.medium, effect='Add Chest HP Bonus also to MP'),
    Feets.ocean_striders: Feet(name=Feets.ocean_striders.name, price=1000, min_str=2,
                               rarity=Rarity.rare, effect='Water walk at ½ SPEED'),
    Feets.cloud_walkers: Feet(name=Feets.cloud_walkers.name, price=1000, min_str=2,
                              rarity=Rarity.unique,
                              effect='Feather fall: fall at a maximum SPEED of 4DIS per RND'),
    Feets.gyro_heels: Feet(name=Feets.gyro_heels.name, price=1200, min_str=2, rarity=Rarity.unique,
                           effect='Save up to ½ maximum SPEED from a RND to use on the next RND'),
    Feets.earth_clamps: Feet(name=Feets.earth_clamps.name, price=1250, min_str=2,
                             equip_type=Type.medium, rarity=Rarity.rare,
                             effect='Not moving for during a RND grants +1PRED for 1RND'),
    Feets.whirlwind_greaves: Feet(name=Feets.whirlwind_greaves.name, price=1250, min_str=2,
                                  rarity=Rarity.rare,
                                  effect='Moving 180 degrees around an enemy before ATTACKing '
                                         'grants +2PAC on next ATTACK'),
    Feets.rebound_greaves: Feet(name=Feets.rebound_greaves.name, price=1250, min_str=2,
                                effect='On critical hit, +8HP and +4SPEED for 1RND'),
    Feets.skywalker_boots: Feet(name=Feets.skywalker_boots.name, price=1300, min_str=2,
                                effect='Walk over gaps at -2SPEED for 1RND'),
    Feets.wind_boots: Feet(name=Feets.wind_boots.name, price=1450, min_str=2, speed=1),
    Feets.topaz_slippers: Feet(name=Feets.topaz_slippers.name, price=1450, min_str=2,
                               effect='+2SPEED for 1RND after consuming 2MP'),
    Feets.wind_striders: Feet(name=Feets.wind_striders.name, price=1650, min_str=2,
                              effect='Can spend 2MP to ignore immobilization'),
    Feets.flashers: Feet(name=Feets.flashers.name, price=1700, min_str=2, rarity=Rarity.rare,
                         effect='If no StdA taken, +3SPEED for 1RND'),
    Feets.ocean_born: Feet(name=Feets.ocean_born.name, price=1850, min_str=3, rarity=Rarity.unique,
                           equip_type=Type.medium, effect='+3HP per RND while in water'),
    Feets.mithril_boots: Feet(name=Feets.mithril_boots.name, price=3150, min_str=3,
                              equip_type=Type.medium, rarity=Rarity.rare,
                              effect='After being hit by magical attack, can ignore 4 MDAM by '
                                     'consuming 2MP'),
    Feets.grooved_soles: Feet(name=Feets.grooved_soles.name, price=300, min_str=1,
                              effect='Marksman only, +2SPEED while Reaper is drawn'),
    Feets.cursed_greaves: Feet(name=Feets.cursed_greaves.name, mdef=-2, bmac=5, speed=1,
                               rarity=Rarity.set, effect='Resist corruption 2RND'),
    Feets.coral_greaves: Feet(name=Feets.coral_greaves.name, price=350, rarity=Rarity.set,
                              effect='+1PDEF +2SPEED in water'),
    Feets.volcanic_greaves: Feet(name=Feets.volcanic_greaves.name, price=650, min_str=1,
                                 rarity=Rarity.set, hp=5, effect='Allows lava walking'),
    Feets.lunatech_boots: Feet(name=Feets.lunatech_boots.name, price=2000, min_str=3,
                               equip_type=Type.medium, rarity=Rarity.set, speed=2,
                               effect='Topaz: FreeA take jump of 8DIS vertical, 5DIS horizontal'),
    Feets.lunafiber_slippers: Feet(name=Feets.lunafiber_slippers.name, price=2250, min_str=2,
                                   mdef=4, bmac=5),
}


class Weapons(aenum.AutoNumberEnum):
    empty = ()
    fists = ()

    bronze_wrist_blades = ()
    iron_wrist_blades = ()
    volcanic_wrist_blades = ()
    reflex_claw = ()
    steel_wrist_blades = ()
    lunaweave_wrist_blades = ()
    lunasteel_wrist_blades = ()

    bronze_rapier = ()
    iron_rapier = ()
    steel_rapier = ()
    cursed_rapier = ()
    lunaweave_rapier = ()
    lunasteel_rapier = ()

    bronze_knuckle = ()
    iron_knuckle = ()
    steel_knuckle = ()
    lunaweave_knuckle = ()
    lunasteel_knuckle = ()

    bronze_chain_whip = ()
    iron_chain_whip = ()
    steel_chain_whip = ()
    lunaweave_chain_whip = ()
    lunasteel_chain_whip = ()

    bronze_claws = ()
    iron_claws = ()
    dragon_claws = ()
    steel_claws = ()
    lunaweave_claws = ()
    lunasteel_claws = ()

    bronze_longsword = ()
    iron_longsword = ()
    moonbeam = ()
    steel_longsword = ()
    lunaweave_longsword = ()
    lunasteel_longsword = ()

    bronze_broadsword = ()
    iron_broadsword = ()
    braveheart = ()
    steel_broadsword = ()
    lunaweave_broadsword = ()
    lunasteel_broadsword = ()

    bronze_double_bladed_spear = ()
    iron_double_bladed_spear = ()
    savior = ()
    steel_double_bladed_spear = ()
    lunaweave_double_bladed_spear = ()
    lunasteel_double_bladed_spear = ()

    bronze_lance = ()
    iron_lance = ()
    ashers_pride = ()
    steel_lance = ()
    lunaweave_lance = ()
    lunasteel_lance = ()

    bronze_hammer = ()
    iron_hammer = ()
    steel_hammer = ()
    lunaweave_hammer = ()
    lunasteel_hammer = ()

    bronze_flail = ()
    iron_flail = ()
    steel_flail = ()
    lunaweave_flail = ()
    lunasteel_flail = ()

    bronze_war_axe = ()
    iron_war_axe = ()
    harbinger = ()
    steel_war_axe = ()
    lunaweave_war_axe = ()
    lunasteel_war_axe = ()

    bronze_great_sword = ()
    iron_great_sword = ()
    vengeant = ()
    leave_n_cleave = ()
    steel_great_sword = ()
    obsidian_blade = ()
    lunaweave_great_sword = ()
    lunasteel_great_sword = ()

    bronze_shuriken = ()
    iron_shuriken = ()
    volcanic_shuriken = ()
    nightwind = ()
    steel_shuriken = ()
    lunaweave_shuriken = ()
    lunasteel_shuriken = ()

    bronze_longbow = ()
    iron_longbow = ()
    volcanic_longbow = ()
    steel_longbow = ()
    lunaweave_longbow = ()
    lunasteel_longbow = ()

    bronze_ternate_crossbow = ()
    iron_ternate_crossbow = ()
    steel_ternate_crossbow = ()
    lunaweave_ternate_crossbow = ()
    lunasteel_ternate_crossbow = ()

    bronze_compound_bow = ()
    iron_compound_bow = ()
    avenger = ()
    steel_compound_bow = ()
    lunaweave_compound_bow = ()
    lunasteel_compound_bow = ()

    bronze_wand = ()
    iron_wand = ()
    steel_wand = ()
    pandoras_kiss = ()
    lunaweave_wand = ()
    lunasteel_wand = ()

    bronze_staff = ()
    iron_staff = ()
    volcanic_staff = ()
    thunder_staff = ()
    coral_staff = ()
    steel_staff = ()
    lunaweave_staff = ()
    lunasteel_staff = ()

    pistol = ()
    pistol_mark_2 = ()
    pistol_mark_3 = ()
    lunaweave_pistol = ()

    rifle = ()
    rifle_mark_2 = ()
    rifle_mark_2_scoped = ()
    rifle_mark_3 = ()
    rifle_mark_3_scoped = ()
    lunaweave_rifle = ()

    shotgun = ()
    shotgun_mark_2 = ()
    shotgun_mark_3 = ()
    lunaweave_shotgun = ()


weapons = {
    Weapons.empty: Weapon(name=Weapons.empty.name, picture=WeaponPicture.hands, style=Style.melee),
    Weapons.fists: Weapon(
        name=Weapons.fists.name, picture=WeaponPicture.hands,
        style=Style.melee, is_two_handed=True,
        pdam=DiceFormula.from_str('d4'), damage_type=DamageType.bludgeoning),

    Weapons.bronze_wrist_blades: Weapon(
        name=Weapons.bronze_wrist_blades.name, price=40, picture=WeaponPicture.pink_wristblades,
        style=Style.melee, is_two_handed=True,
        attacks=2, pdam=DiceFormula.from_str('1d6'), damage_type=DamageType.slashing,
        cdam=3),
    Weapons.iron_wrist_blades: Weapon(
        name=Weapons.iron_wrist_blades.name, price=175, picture=WeaponPicture.pink_wristblades,
        style=Style.melee, is_two_handed=True, min_dex=1,
        attacks=2, pdam=DiceFormula.from_str('1d8'), damage_type=DamageType.slashing,
        cdam=4),
    Weapons.volcanic_wrist_blades: Weapon(
        name=Weapons.volcanic_wrist_blades.name, price=450, picture=WeaponPicture.grey_wristblades,
        style=Style.melee, is_two_handed=True, min_dex=1, rarity=Rarity.set,
        attacks=2, pdam=DiceFormula.from_str('1d8'), mdam=DiceFormula.from_str('1d2'),
        damage_type=DamageType.slashing, cdam=4,
        effect='1 Fire MDAM per RND for 4RND'),
    Weapons.reflex_claw: Weapon(
        name=Weapons.reflex_claw.name, price=550, picture=WeaponPicture.grey_wristblades,
        style=Style.melee, is_two_handed=True, min_dex=2, rarity=Rarity.unique,
        attacks=1, pdam=DiceFormula.from_str('1d6'), damage_type=DamageType.slashing,
        cdam=3,
        effect='Take 1 attack on each enemy in range during MovA. On hit, +1SPEED for current '
               'RND'),
    Weapons.steel_wrist_blades: Weapon(
        name=Weapons.steel_wrist_blades.name, price=875, picture=WeaponPicture.grey_wristblades,
        style=Style.melee, is_two_handed=True, min_dex=2,
        attacks=3, pdam=DiceFormula.from_str('1d6'), damage_type=DamageType.slashing,
        cdam=3),
    Weapons.lunaweave_wrist_blades: Weapon(
        name=Weapons.lunaweave_wrist_blades.name, price=3250,
        picture=WeaponPicture.grey_wristblades,
        style=Style.melee, is_two_handed=True, min_dex=3,
        attacks=3, pdam=DiceFormula.from_str('1d8'), damage_type=DamageType.slashing,
        cdam=4),
    Weapons.lunasteel_wrist_blades: Weapon(
        name=Weapons.lunasteel_wrist_blades.name, price=8750,
        picture=WeaponPicture.grey_wristblades,
        style=Style.melee, is_two_handed=True, min_dex=3,
        attacks=3, pdam=DiceFormula.from_str('1d10'), damage_type=DamageType.slashing,
        cdam=5),

    Weapons.bronze_rapier: Weapon(
        name=Weapons.bronze_rapier.name, price=40, picture=WeaponPicture.gold_rapier,
        style=Style.melee, shape=Shape.line_2, max_range=2,
        attacks=2, pdam=DiceFormula.from_str('1d6'), damage_type=DamageType.piercing,
        cdam=3),
    Weapons.iron_rapier: Weapon(
        name=Weapons.iron_rapier.name, price=175, picture=WeaponPicture.grey_rapier,
        style=Style.melee, shape=Shape.line_2, min_dex=1, max_range=2,
        attacks=2, pdam=DiceFormula.from_str('1d8'), damage_type=DamageType.piercing,
        cdam=4),
    Weapons.steel_rapier: Weapon(
        name=Weapons.steel_rapier.name, price=875, picture=WeaponPicture.grey_rapier,
        style=Style.melee, shape=Shape.line_2, min_dex=2, max_range=2,
        attacks=2, pdam=DiceFormula.from_str('1d12'), damage_type=DamageType.piercing,
        cdam=6),
    Weapons.cursed_rapier: Weapon(
        name=Weapons.cursed_rapier.name, price=0, picture=WeaponPicture.black_sword,
        style=Style.melee, shape=Shape.line_2, min_dex=0, max_range=2, rarity=Rarity.unique,
        attacks=2, pdam=DiceFormula.from_str('1d12 + 1d4'), damage_type=DamageType.piercing,
        cdam=8, effect='+1MP on hit, -1HP per hit, 20FOR to unequip'),
    Weapons.lunaweave_rapier: Weapon(
        name=Weapons.lunaweave_rapier.name, price=3250, picture=WeaponPicture.dark_blue_sword,
        style=Style.melee, shape=Shape.line_2, min_dex=3, max_range=2,
        attacks=2, pdam=DiceFormula.from_str('1d12 + 1d4'), damage_type=DamageType.piercing,
        cdam=8),
    Weapons.lunasteel_rapier: Weapon(
        name=Weapons.lunasteel_rapier.name, price=8750, picture=WeaponPicture.crystal_sword,
        style=Style.melee, shape=Shape.line_2, min_dex=4, max_range=2,
        attacks=2, pdam=DiceFormula.from_str('2d10'), damage_type=DamageType.piercing,
        cdam=10),

    Weapons.bronze_knuckle: Weapon(
        name=Weapons.bronze_knuckle.name, price=40, picture=WeaponPicture.orange_gauntlets,
        style=Style.melee,
        pdam=DiceFormula.from_str('1d12'), damage_type=DamageType.bludgeoning,
        pac=2, pdef=1, effect='On crit: Stun 1RND'),
    Weapons.iron_knuckle: Weapon(
        name=Weapons.iron_knuckle.name, price=175, picture=WeaponPicture.grey_gauntlets,
        style=Style.melee, min_dex=1,
        pdam=DiceFormula.from_str('1d12'), damage_type=DamageType.bludgeoning,
        pac=2, pdef=1, effect='On crit: Stun 1RND'),
    Weapons.steel_knuckle: Weapon(
        name=Weapons.steel_knuckle.name, price=875, picture=WeaponPicture.blue_gauntlets,
        style=Style.melee, min_dex=2,
        pdam=DiceFormula.from_str('2d12'), damage_type=DamageType.bludgeoning,
        pac=2, pdef=2, effect='On crit: Stun 1RND'),
    Weapons.lunaweave_knuckle: Weapon(
        name=Weapons.lunaweave_knuckle.name, price=3250, picture=WeaponPicture.yellow_gauntlets,
        style=Style.melee, min_dex=3,
        pdam=DiceFormula.from_str('2d12 + 1d6'), damage_type=DamageType.bludgeoning,
        pac=2, bmac=2, pdef=2, effect='On crit: Stun 2RND'),
    Weapons.lunasteel_knuckle: Weapon(
        name=Weapons.lunasteel_knuckle.name, price=8750, picture=WeaponPicture.green_gauntlets,
        style=Style.melee, min_dex=4,
        pdam=DiceFormula.from_str('3d12'), damage_type=DamageType.bludgeoning,
        pac=2, bmac=2, pdef=3, mdef=2, effect='On crit: Stun 2RND'),

    Weapons.bronze_chain_whip: Weapon(
        name=Weapons.bronze_chain_whip.name, price=50, picture=WeaponPicture.brown_whip,
        style=Style.melee, equip_type=Type.medium, shape=Shape.halo,
        pdam=DiceFormula.from_str('1d10'), damage_type=DamageType.slashing, cdam=10),
    Weapons.iron_chain_whip: Weapon(
        name=Weapons.iron_chain_whip.name, price=200, picture=WeaponPicture.grey_whip,
        style=Style.melee, equip_type=Type.medium, shape=Shape.halo, min_dex=1,
        attacks=2, pdam=DiceFormula.from_str('1d8'), damage_type=DamageType.slashing, cdam=8),
    Weapons.steel_chain_whip: Weapon(
        name=Weapons.steel_chain_whip.name, price=1000, picture=WeaponPicture.grey_whip,
        style=Style.melee, equip_type=Type.medium, shape=Shape.halo, min_dex=2,
        attacks=3, pdam=DiceFormula.from_str('1d8'), damage_type=DamageType.slashing, cdam=8),
    Weapons.lunaweave_chain_whip: Weapon(
        name=Weapons.lunaweave_chain_whip.name, price=3500, picture=WeaponPicture.yellow_whip,
        style=Style.melee, equip_type=Type.medium, shape=Shape.halo, min_dex=3,
        attacks=3, pdam=DiceFormula.from_str('1d10'), damage_type=DamageType.slashing, cdam=10),
    Weapons.lunasteel_chain_whip: Weapon(
        name=Weapons.lunasteel_chain_whip.name, price=10000, picture=WeaponPicture.green_whip,
        style=Style.melee, equip_type=Type.medium, shape=Shape.halo, min_dex=4,
        attacks=3, pdam=DiceFormula.from_str('1d12'), damage_type=DamageType.slashing, cdam=10),

    Weapons.bronze_claws: Weapon(
        name=Weapons.bronze_claws.name, price=50, picture=WeaponPicture.brown_claws,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_multi_point,
        is_two_handed=True, attacks=2, pdef=1,
        pdam=DiceFormula.from_str('1d6'), damage_type=DamageType.slashing, cdam=6),
    Weapons.iron_claws: Weapon(
        name=Weapons.iron_claws.name, price=200, picture=WeaponPicture.grey_claws,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_multi_point, min_dex=1,
        is_two_handed=True, attacks=2, pdef=1,
        pdam=DiceFormula.from_str('1d8'), damage_type=DamageType.slashing, cdam=8),
    Weapons.dragon_claws: Weapon(
        name=Weapons.dragon_claws.name, price=650, picture=WeaponPicture.red_claws,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_multi_point, min_dex=1,
        rarity=Rarity.unique,
        is_two_handed=True, attacks=2, pdef=1,
        pdam=DiceFormula.from_str('1d8'), damage_type=DamageType.slashing, cdam=8,
        effect='+1HP per hit'),
    Weapons.steel_claws: Weapon(
        name=Weapons.steel_claws.name, price=1000, picture=WeaponPicture.blue_claws,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_multi_point, min_dex=2,
        is_two_handed=True, attacks=2, pdef=2,
        pdam=DiceFormula.from_str('1d12'), damage_type=DamageType.slashing, cdam=12),
    Weapons.lunaweave_claws: Weapon(
        name=Weapons.lunaweave_claws.name, price=3500, picture=WeaponPicture.silver_claws,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_multi_point, min_dex=3,
        is_two_handed=True, attacks=2, pdef=2,
        pdam=DiceFormula.from_str('1d12 + 1d4'), damage_type=DamageType.slashing, cdam=16),
    Weapons.lunasteel_claws: Weapon(
        name=Weapons.lunasteel_claws.name, price=10000, picture=WeaponPicture.silver_claws_3,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_multi_point, min_dex=4,
        is_two_handed=True, attacks=2, pdef=3,
        pdam=DiceFormula.from_str('2d10'), damage_type=DamageType.slashing, cdam=20),

    Weapons.bronze_longsword: Weapon(
        name=Weapons.bronze_longsword.name, price=50, picture=WeaponPicture.gold_longsword,
        style=Style.melee, equip_type=Type.medium, pac=2,
        pdam=DiceFormula.from_str('1d12'), damage_type=DamageType.slashing, cdam=12),
    Weapons.iron_longsword: Weapon(
        name=Weapons.iron_longsword.name, price=200, picture=WeaponPicture.grey_longsword,
        style=Style.melee, equip_type=Type.medium, min_dex=1, pac=2,
        pdam=DiceFormula.from_str('1d12 + 1d6'), damage_type=DamageType.slashing, cdam=18),
    Weapons.moonbeam: Weapon(
        name=Weapons.moonbeam.name, price=550, picture=WeaponPicture.glow_sword,
        style=Style.melee, equip_type=Type.medium, min_dex=1, pac=2,
        rarity=Rarity.unique,
        pdam=DiceFormula.from_str('1d12 + 1d6'), damage_type=DamageType.slashing, cdam=18,
        effect='On kill, +4MP'),
    Weapons.steel_longsword: Weapon(
        name=Weapons.steel_longsword.name, price=1000, picture=WeaponPicture.grey_longsword,
        style=Style.melee, equip_type=Type.medium, min_dex=2, pac=2,
        pdam=DiceFormula.from_str('2d12'), damage_type=DamageType.slashing, cdam=24),
    Weapons.lunaweave_longsword: Weapon(
        name=Weapons.lunaweave_longsword.name, price=3500, picture=WeaponPicture.blue_longsword,
        style=Style.melee, equip_type=Type.medium, min_dex=2, pac=2,
        pdam=DiceFormula.from_str('3d12'), damage_type=DamageType.slashing, cdam=36),
    Weapons.lunasteel_longsword: Weapon(
        name=Weapons.lunasteel_longsword.name, price=10000,
        picture=WeaponPicture.crystal_longsword,
        style=Style.melee, equip_type=Type.medium, min_dex=2, pac=2,
        pdam=DiceFormula.from_str('4d12'), damage_type=DamageType.slashing, cdam=48),

    Weapons.bronze_broadsword: Weapon(
        name=Weapons.bronze_broadsword.name, price=50, picture=WeaponPicture.orange_broadsword,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_line_2,
        pdam=DiceFormula.from_str('1d10'), damage_type=DamageType.slashing, cdam=10),
    Weapons.iron_broadsword: Weapon(
        name=Weapons.iron_broadsword.name, price=200, picture=WeaponPicture.grey_broadsword,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_line_2, min_dex=1,
        pdam=DiceFormula.from_str('1d10 + 1d4'), damage_type=DamageType.slashing, cdam=14),
    Weapons.braveheart: Weapon(
        name=Weapons.braveheart.name, price=450, picture=WeaponPicture.pink_broadsword,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_line_2, min_dex=1,
        rarity=Rarity.unique,
        pdam=DiceFormula.from_str('1d10 + 1d4'), damage_type=DamageType.slashing, cdam=14,
        effect='If wielder below 50% maximum HP, +3PDAM'),
    Weapons.steel_broadsword: Weapon(
        name=Weapons.steel_broadsword.name, price=1000, picture=WeaponPicture.black_broadsword,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_line_2, min_dex=2,
        pdam=DiceFormula.from_str('2d10'), damage_type=DamageType.slashing, cdam=20),
    Weapons.lunaweave_broadsword: Weapon(
        name=Weapons.lunaweave_broadsword.name, price=2500,
        picture=WeaponPicture.yellow_broadsword,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_line_2, min_dex=3,
        pdam=DiceFormula.from_str('3d10'), damage_type=DamageType.slashing, cdam=30),
    Weapons.lunasteel_broadsword: Weapon(
        name=Weapons.lunasteel_broadsword.name, price=10000,
        picture=WeaponPicture.green_broadsword, is_two_handed=True,
        style=Style.melee, equip_type=Type.medium, shape=Shape.side_line_2, min_dex=4,
        pdam=DiceFormula.from_str('4d10'), damage_type=DamageType.slashing, cdam=40),

    Weapons.bronze_double_bladed_spear: Weapon(
        name=Weapons.bronze_double_bladed_spear.name, price=50,
        picture=WeaponPicture.white_two_handed_spear,
        style=Style.melee, equip_type=Type.medium, shape=Shape.melee_x,
        min_range=0, max_range=0, is_two_handed=True,
        pdam=DiceFormula.from_str('1d10'), damage_type=DamageType.slashing, cdam=10,
        effect='[Counter] If adjecent ally is hit by melee attack, can take 1ATTACK'),
    Weapons.iron_double_bladed_spear: Weapon(
        name=Weapons.iron_double_bladed_spear.name, price=200,
        picture=WeaponPicture.white_two_handed_spear, min_dex=1,
        style=Style.melee, equip_type=Type.medium, shape=Shape.melee_x,
        min_range=0, max_range=0, is_two_handed=True,
        pdam=DiceFormula.from_str('1d10 + 1d4'), damage_type=DamageType.slashing, cdam=14,
        effect='[Counter] If adjecent ally is hit by melee attack, can take 1ATTACK'),
    Weapons.savior: Weapon(
        name=Weapons.savior.name, price=450,
        picture=WeaponPicture.white_two_handed_spear, min_dex=1,
        style=Style.melee, equip_type=Type.medium, shape=Shape.melee_x,
        min_range=0, max_range=0, is_two_handed=True, rarity=Rarity.unique,
        pdam=DiceFormula.from_str('1d10 + 1d4'), damage_type=DamageType.slashing, cdam=14,
        effect='[Counter] If adjecent ally is hit by melee attack, can take 1ATTACK, '
               'Adjecent allies gains +1PRED'),
    Weapons.steel_double_bladed_spear: Weapon(
        name=Weapons.steel_double_bladed_spear.name, price=1000,
        picture=WeaponPicture.white_two_handed_spear, min_dex=2,
        style=Style.melee, equip_type=Type.medium, shape=Shape.melee_x,
        min_range=0, max_range=0, is_two_handed=True,
        pdam=DiceFormula.from_str('2d10'), damage_type=DamageType.slashing, cdam=20,
        effect='[Counter] If adjecent ally is hit by melee attack, can take 1ATTACK'),
    Weapons.lunaweave_double_bladed_spear: Weapon(
        name=Weapons.lunaweave_double_bladed_spear.name, price=3500,
        picture=WeaponPicture.white_two_handed_spear, min_dex=3,
        style=Style.melee, equip_type=Type.medium, shape=Shape.melee_x,
        min_range=0, max_range=0, is_two_handed=True,
        pdam=DiceFormula.from_str('3d10'), damage_type=DamageType.slashing, cdam=30,
        effect='[Counter] If adjecent ally is hit by melee attack, can take 1ATTACK'),
    Weapons.lunasteel_double_bladed_spear: Weapon(
        name=Weapons.lunasteel_double_bladed_spear.name, price=10000,
        picture=WeaponPicture.white_two_handed_spear, min_dex=4,
        style=Style.melee, equip_type=Type.medium, shape=Shape.melee_x,
        min_range=0, max_range=0, is_two_handed=True,
        pdam=DiceFormula.from_str('4d10'), damage_type=DamageType.slashing, cdam=40,
        effect='[Counter] If adjecent ally is hit by melee attack, can take 1ATTACK'),

    Weapons.bronze_lance: Weapon(
        name=Weapons.bronze_lance.name, price=50, picture=WeaponPicture.gold_spear,
        style=Style.melee, equip_type=Type.medium, shape=Shape.line_3,
        min_range=1, max_range=3, is_two_handed=True,
        pdam=DiceFormula.from_str('1d10'), damage_type=DamageType.piercing, cdam=10),
    Weapons.iron_lance: Weapon(
        name=Weapons.iron_lance.name, price=200, picture=WeaponPicture.grey_spear,
        style=Style.melee, equip_type=Type.medium, shape=Shape.line_3,
        min_range=1, max_range=3, is_two_handed=True, min_dex=1,
        pdam=DiceFormula.from_str('1d10 + 1d4'), damage_type=DamageType.piercing, cdam=14),
    Weapons.ashers_pride: Weapon(
        name=Weapons.ashers_pride.name, price=200, picture=WeaponPicture.dark_purple_spear,
        style=Style.melee, equip_type=Type.medium, shape=Shape.line_3, rarity=Rarity.unique,
        min_range=1, max_range=6, is_two_handed=True, min_dex=1,
        pdam=DiceFormula.from_str('1d10 + 1d4'), damage_type=DamageType.piercing, cdam=14,
        effect='Extended max range.'),
    Weapons.steel_lance: Weapon(
        name=Weapons.iron_lance.name, price=1000, picture=WeaponPicture.grey_spear,
        style=Style.melee, equip_type=Type.medium, shape=Shape.line_3,
        min_range=1, max_range=3, is_two_handed=True, min_dex=2,
        pdam=DiceFormula.from_str('2d10'), damage_type=DamageType.piercing, cdam=20),
    Weapons.lunaweave_lance: Weapon(
        name=Weapons.lunaweave_lance.name, price=3500, picture=WeaponPicture.blue_spear,
        style=Style.melee, equip_type=Type.medium, shape=Shape.line_3,
        min_range=1, max_range=3, is_two_handed=True, min_dex=3,
        pdam=DiceFormula.from_str('3d10'), damage_type=DamageType.piercing, cdam=30),
    Weapons.lunasteel_lance: Weapon(
        name=Weapons.lunasteel_lance.name, price=10000, picture=WeaponPicture.rainbow_spear,
        style=Style.melee, equip_type=Type.medium, shape=Shape.line_3,
        min_range=1, max_range=3, is_two_handed=True, min_dex=4,
        pdam=DiceFormula.from_str('4d10'), damage_type=DamageType.piercing, cdam=40),

    Weapons.bronze_hammer: Weapon(
        name=Weapons.bronze_hammer.name, price=75, picture=WeaponPicture.orange_hammer,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.t,
        min_range=1, max_range=2, is_two_handed=True,
        pdam=DiceFormula.from_str('1d10 + 1d4'), damage_type=DamageType.bludgeoning, cdam=14),
    Weapons.iron_hammer: Weapon(
        name=Weapons.iron_hammer.name, price=250, picture=WeaponPicture.red_hammer,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.t,
        min_range=1, max_range=2, is_two_handed=True, min_dex=1,
        pdam=DiceFormula.from_str('2d10'), damage_type=DamageType.bludgeoning, cdam=20),
    Weapons.steel_hammer: Weapon(
        name=Weapons.steel_hammer.name, price=1250, picture=WeaponPicture.black_war_hammer,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.t,
        min_range=1, max_range=2, is_two_handed=True, min_dex=2,
        pdam=DiceFormula.from_str('2d10 + 2d4'), damage_type=DamageType.bludgeoning, cdam=28),
    Weapons.lunaweave_hammer: Weapon(
        name=Weapons.lunaweave_hammer.name, price=4000, picture=WeaponPicture.blue_hammer,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.t,
        min_range=1, max_range=2, is_two_handed=True, min_dex=3,
        pdam=DiceFormula.from_str('4d10'), damage_type=DamageType.bludgeoning, cdam=40),
    Weapons.lunasteel_hammer: Weapon(
        name=Weapons.lunasteel_hammer.name, price=12500, picture=WeaponPicture.dark_blue_hammer,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.t,
        min_range=1, max_range=2, is_two_handed=True, min_dex=4,
        pdam=DiceFormula.from_str('3d20'), damage_type=DamageType.bludgeoning, cdam=60),

    Weapons.bronze_flail: Weapon(
        name=Weapons.bronze_flail.name, price=75, picture=WeaponPicture.red_flail,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.y,
        min_range=1, max_range=2, is_two_handed=True,
        pdam=DiceFormula.from_str('1d10 + 1d4'), damage_type=DamageType.bludgeoning, cdam=14),
    Weapons.iron_flail: Weapon(
        name=Weapons.iron_flail.name, price=250, picture=WeaponPicture.brown_flail,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.y,
        min_range=1, max_range=2, is_two_handed=True, min_dex=1,
        pdam=DiceFormula.from_str('2d10'), damage_type=DamageType.bludgeoning, cdam=20),
    Weapons.steel_flail: Weapon(
        name=Weapons.steel_flail.name, price=1250, picture=WeaponPicture.grey_flail,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.y,
        min_range=1, max_range=2, is_two_handed=True, min_dex=2,
        pdam=DiceFormula.from_str('2d10 + 2d4'), damage_type=DamageType.bludgeoning, cdam=28),
    Weapons.lunaweave_flail: Weapon(
        name=Weapons.lunaweave_flail.name, price=4000, picture=WeaponPicture.blue_flail,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.y,
        min_range=1, max_range=2, is_two_handed=True, min_dex=3,
        pdam=DiceFormula.from_str('4d10'), damage_type=DamageType.bludgeoning, cdam=40),
    Weapons.lunasteel_flail: Weapon(
        name=Weapons.lunasteel_flail.name, price=12500, picture=WeaponPicture.yellow_flail,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.y,
        min_range=1, max_range=2, is_two_handed=True, min_dex=4,
        pdam=DiceFormula.from_str('3d20'), damage_type=DamageType.bludgeoning, cdam=60),

    Weapons.bronze_war_axe: Weapon(
        name=Weapons.bronze_war_axe.name, price=75, picture=WeaponPicture.orange_great_axe,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.side_line_3,
        min_range=1, max_range=2, is_two_handed=True,
        pdam=DiceFormula.from_str('1d10 + 1d4'), damage_type=DamageType.bludgeoning, cdam=14),
    Weapons.iron_war_axe: Weapon(
        name=Weapons.iron_war_axe.name, price=250, picture=WeaponPicture.black_great_axe,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.side_line_3,
        min_range=1, max_range=2, is_two_handed=True, min_dex=1,
        pdam=DiceFormula.from_str('2d10'), damage_type=DamageType.bludgeoning, cdam=20),
    Weapons.harbinger: Weapon(
        name=Weapons.harbinger.name, price=1250, picture=WeaponPicture.purple_great_axe,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.side_line_3,
        min_range=1, max_range=2, is_two_handed=True, min_dex=1, rarity=Rarity.unique,
        pdam=DiceFormula.from_str('2d10'), damage_type=DamageType.bludgeoning, cdam=20,
        effect='If attack KOs enemy, may perform another physical attack'),
    Weapons.steel_war_axe: Weapon(
        name=Weapons.steel_war_axe.name, price=1250, picture=WeaponPicture.dark_purple_great_axe,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.side_line_3,
        min_range=1, max_range=2, is_two_handed=True, min_dex=2,
        pdam=DiceFormula.from_str('2d10 + 2d4'), damage_type=DamageType.bludgeoning, cdam=28),
    Weapons.lunaweave_war_axe: Weapon(
        name=Weapons.lunaweave_war_axe.name, price=4000, picture=WeaponPicture.dark_blue_great_axe,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.side_line_3,
        min_range=1, max_range=2, is_two_handed=True, min_dex=3,
        pdam=DiceFormula.from_str('4d10'), damage_type=DamageType.bludgeoning, cdam=40),
    Weapons.lunasteel_war_axe: Weapon(
        name=Weapons.lunasteel_war_axe.name, price=12500, picture=WeaponPicture.blue_great_axe,
        style=Style.melee, equip_type=Type.heavy, shape=Shape.side_line_3,
        min_range=1, max_range=2, is_two_handed=True, min_dex=4,
        pdam=DiceFormula.from_str('3d20'), damage_type=DamageType.bludgeoning, cdam=60),

    Weapons.bronze_great_sword: Weapon(
        name=Weapons.bronze_great_sword.name, price=75, picture=WeaponPicture.orange_royal_sword,
        style=Style.melee, equip_type=Type.heavy, pac=2,
        pdam=DiceFormula.from_str('1d12 + 1d8'), damage_type=DamageType.slashing, cdam=20),
    Weapons.iron_great_sword: Weapon(
        name=Weapons.iron_great_sword.name, price=250, picture=WeaponPicture.grey_royal_sword,
        style=Style.melee, equip_type=Type.heavy, min_dex=1, pac=2,
        pdam=DiceFormula.from_str('2d12 + 1d4'), damage_type=DamageType.bludgeoning, cdam=28),
    Weapons.vengeant: Weapon(
        name=Weapons.vengeant.name, price=1000, picture=WeaponPicture.flame_royal_sword,
        style=Style.melee, equip_type=Type.heavy, min_dex=1, pac=3, rarity=Rarity.unique,
        pdam=DiceFormula.from_str('2d12 + 1d4'), damage_type=DamageType.slashing, cdam=28,
        effect='Add ½ PDAM taken during the previous RND to weapon ATTACK'),
    Weapons.leave_n_cleave: Weapon(
        name=Weapons.leave_n_cleave.name, price=1000, picture=WeaponPicture.red_tooth_royal_sword,
        style=Style.melee, equip_type=Type.heavy, min_dex=1, pac=3, rarity=Rarity.unique,
        shape=Shape.side_line_2,
        pdam=DiceFormula.from_str('2d12 + 1d4'), damage_type=DamageType.slashing, cdam=28,
        effect='Extended AOE'),
    Weapons.steel_great_sword: Weapon(
        name=Weapons.steel_great_sword.name, price=1250, picture=WeaponPicture.black_royal_sword,
        style=Style.melee, equip_type=Type.heavy, min_dex=2, pac=2,
        pdam=DiceFormula.from_str('2d20'), damage_type=DamageType.slashing, cdam=40),
    Weapons.obsidian_blade: Weapon(
        name=Weapons.obsidian_blade.name, price=1550, picture=WeaponPicture.dark_tooth_royal_sword,
        style=Style.melee, equip_type=Type.heavy, min_dex=2, pac=2, mp=-10,
        pdam=DiceFormula.from_str('2d20'), damage_type=DamageType.slashing, cdam=40,
        effect='On hit enemy is silenced'),
    Weapons.lunaweave_great_sword: Weapon(
        name=Weapons.lunaweave_great_sword.name, price=4000,
        picture=WeaponPicture.blue_royal_sword,
        style=Style.melee, equip_type=Type.heavy, min_dex=3, pac=2,
        pdam=DiceFormula.from_str('2d20 + 1d12'), damage_type=DamageType.slashing, cdam=52),
    Weapons.lunasteel_great_sword: Weapon(
        name=Weapons.lunasteel_great_sword.name, price=12500,
        picture=WeaponPicture.rainbow_royal_sword,
        style=Style.melee, equip_type=Type.heavy, min_dex=4, pac=2,
        pdam=DiceFormula.from_str('3d20 + 1d8'), damage_type=DamageType.slashing, cdam=68),

    Weapons.bronze_shuriken: Weapon(
        name=Weapons.bronze_shuriken.name, price=40, picture=WeaponPicture.grey_shuriken,
        style=Style.ranged, is_two_handed=True,
        min_range=1, max_range=6, shape=Shape.range_point,
        attacks=2, pdam=DiceFormula.from_str('d4'), damage_type=DamageType.piercing,
        cdam=2),
    Weapons.iron_shuriken: Weapon(
        name=Weapons.iron_shuriken.name, price=175, picture=WeaponPicture.grey_shuriken,
        style=Style.ranged, is_two_handed=True, min_dex=1,
        min_range=1, max_range=7, shape=Shape.range_point,
        attacks=3, pdam=DiceFormula.from_str('d4'), damage_type=DamageType.piercing,
        cdam=2),
    Weapons.volcanic_shuriken: Weapon(
        name=Weapons.volcanic_shuriken.name, price=450, picture=WeaponPicture.red_shuriken,
        style=Style.ranged, is_two_handed=True, min_dex=2, rarity=Rarity.set,
        min_range=1, max_range=7, shape=Shape.range_point,
        attacks=3, pdam=DiceFormula.from_str('d4'), damage_type=DamageType.fire,
        cdam=2, effect='1 Fire MDAM per RND for 4RND'),
    Weapons.nightwind: Weapon(
        name=Weapons.nightwind.name, price=650, picture=WeaponPicture.orange_boomerang,
        style=Style.ranged, is_two_handed=True, min_dex=2, rarity=Rarity.unique,
        min_range=1, max_range=7, shape=Shape.range_point,
        attacks=3, pdam=DiceFormula.from_str('1'), damage_type=DamageType.piercing,
        cdam=0, effect='Causes sleep for 1RND'),
    Weapons.steel_shuriken: Weapon(
        name=Weapons.steel_shuriken.name, price=875, picture=WeaponPicture.grey_shuriken,
        style=Style.ranged, is_two_handed=True, min_dex=2,
        min_range=1, max_range=8, shape=Shape.range_point,
        attacks=3, pdam=DiceFormula.from_str('d6'), damage_type=DamageType.piercing,
        cdam=3),
    Weapons.lunaweave_shuriken: Weapon(
        name=Weapons.lunaweave_shuriken.name, price=3250, picture=WeaponPicture.grey_shuriken,
        style=Style.ranged, is_two_handed=True, min_dex=3,
        min_range=1, max_range=9, shape=Shape.range_point,
        attacks=3, pdam=DiceFormula.from_str('d8'), damage_type=DamageType.piercing,
        cdam=4),
    Weapons.lunasteel_shuriken: Weapon(
        name=Weapons.lunasteel_shuriken.name, price=10000, picture=WeaponPicture.grey_shuriken,
        style=Style.ranged, is_two_handed=True, min_dex=4,
        min_range=1, max_range=10, shape=Shape.range_point,
        attacks=3, pdam=DiceFormula.from_str('d12'), damage_type=DamageType.piercing,
        cdam=6),

    Weapons.bronze_longbow: Weapon(
        name=Weapons.bronze_longbow.name, price=50, picture=WeaponPicture.brown_bow,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True,
        min_range=2, max_range=12, shape=Shape.range_point,
        attacks=1, pdam=DiceFormula.from_str('1d8'), damage_type=DamageType.piercing,
        cdam=8),
    Weapons.iron_longbow: Weapon(
        name=Weapons.iron_longbow.name, price=200, picture=WeaponPicture.white_bow,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True,
        min_range=2, max_range=13, shape=Shape.range_point, min_dex=1,
        attacks=1, pdam=DiceFormula.from_str('1d12'), damage_type=DamageType.piercing,
        cdam=12),
    Weapons.volcanic_longbow: Weapon(
        name=Weapons.volcanic_longbow.name, price=850, picture=WeaponPicture.red_feather_bow,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True,
        min_range=2, max_range=13, shape=Shape.range_point, min_dex=2, rarity=Rarity.unique,
        attacks=2, pdam=DiceFormula.from_str('1d12'), damage_type=DamageType.fire,
        cdam=12, effect='[[1d4]] Fire MDAM on 1RAD'),
    Weapons.steel_longbow: Weapon(
        name=Weapons.steel_longbow.name, price=1000, picture=WeaponPicture.white_bow,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True,
        min_range=2, max_range=14, shape=Shape.range_point, min_dex=2,
        attacks=2, pdam=DiceFormula.from_str('1d12'), damage_type=DamageType.piercing,
        cdam=12),
    Weapons.lunaweave_longbow: Weapon(
        name=Weapons.lunaweave_longbow.name, price=3500, picture=WeaponPicture.blue_bow,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True,
        min_range=2, max_range=15, shape=Shape.range_point, min_dex=3,
        attacks=2, pdam=DiceFormula.from_str('1d12 + 1d4'), damage_type=DamageType.piercing,
        cdam=16),
    Weapons.lunasteel_longbow: Weapon(
        name=Weapons.lunasteel_longbow.name, price=10000, picture=WeaponPicture.orange_bow,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True,
        min_range=2, max_range=16, shape=Shape.range_point, min_dex=4,
        attacks=3, pdam=DiceFormula.from_str('1d10 + 1d4'), damage_type=DamageType.piercing,
        cdam=14),

    Weapons.bronze_ternate_crossbow: Weapon(
        name=Weapons.bronze_ternate_crossbow.name, price=75, picture=WeaponPicture.brown_crossbow,
        style=Style.ranged, equip_type=Type.heavy, is_two_handed=True,
        min_range=3, max_range=10, shape=Shape.range_multi_point, pac=1,
        attacks=1, pdam=DiceFormula.from_str('1d8'), damage_type=DamageType.piercing,
        cdam=8),
    Weapons.iron_ternate_crossbow: Weapon(
        name=Weapons.iron_ternate_crossbow.name, price=250, picture=WeaponPicture.grey_crossbow,
        style=Style.ranged, equip_type=Type.heavy, is_two_handed=True, min_dex=1,
        min_range=3, max_range=11, shape=Shape.range_multi_point, pac=1,
        attacks=1, pdam=DiceFormula.from_str('1d12'), damage_type=DamageType.piercing,
        cdam=12),
    Weapons.steel_ternate_crossbow: Weapon(
        name=Weapons.steel_ternate_crossbow.name, price=1250, picture=WeaponPicture.grey_crossbow,
        style=Style.ranged, equip_type=Type.heavy, is_two_handed=True, min_dex=2,
        min_range=3, max_range=12, shape=Shape.range_multi_point, pac=1,
        attacks=2, pdam=DiceFormula.from_str('1d12'), damage_type=DamageType.piercing,
        cdam=12),
    Weapons.lunaweave_ternate_crossbow: Weapon(
        name=Weapons.lunaweave_ternate_crossbow.name, price=4000,
        picture=WeaponPicture.diamond_crossbow,
        style=Style.ranged, equip_type=Type.heavy, is_two_handed=True, min_dex=3,
        min_range=3, max_range=13, shape=Shape.range_multi_point, pac=1,
        attacks=2, pdam=DiceFormula.from_str('1d12 + 1d4'), damage_type=DamageType.piercing,
        cdam=16),
    Weapons.lunasteel_ternate_crossbow: Weapon(
        name=Weapons.lunasteel_ternate_crossbow.name, price=12500,
        picture=WeaponPicture.gem_crossbow,
        style=Style.ranged, equip_type=Type.heavy, is_two_handed=True, min_dex=4,
        min_range=3, max_range=14, shape=Shape.range_multi_point, pac=1,
        attacks=3, pdam=DiceFormula.from_str('1d10 + 1d4'), damage_type=DamageType.piercing,
        cdam=14),

    Weapons.bronze_compound_bow: Weapon(
        name=Weapons.bronze_compound_bow.name, price=75, picture=WeaponPicture.brown_bow,
        style=Style.ranged, equip_type=Type.heavy, is_two_handed=True,
        min_range=3, max_range=13, shape=Shape.range_point, pac=1,
        attacks=1, pdam=DiceFormula.from_str('1d10'), damage_type=DamageType.piercing,
        cdam=10),
    Weapons.iron_compound_bow: Weapon(
        name=Weapons.iron_compound_bow.name, price=250, picture=WeaponPicture.white_bow,
        style=Style.ranged, equip_type=Type.heavy, is_two_handed=True,
        min_range=3, max_range=14, shape=Shape.range_point, pac=1, min_dex=1,
        attacks=1, pdam=DiceFormula.from_str('1d12 + 1d4'), damage_type=DamageType.piercing,
        cdam=10),
    Weapons.avenger: Weapon(
        name=Weapons.avenger.name, price=550, picture=WeaponPicture.pink_bow,
        style=Style.ranged, equip_type=Type.heavy, is_two_handed=True, rarity=Rarity.unique,
        min_range=3, max_range=14, shape=Shape.range_point, pac=2, min_dex=1,
        attacks=1, pdam=DiceFormula.from_str('1d12 + 1d4'), damage_type=DamageType.piercing,
        cdam=10, effect='+3PDAM against enemies who physically or magically hit ally last RND'),
    Weapons.steel_compound_bow: Weapon(
        name=Weapons.steel_compound_bow.name, price=1250, picture=WeaponPicture.white_bow,
        style=Style.ranged, equip_type=Type.heavy, is_two_handed=True,
        min_range=3, max_range=15, shape=Shape.range_point, pac=1, min_dex=2,
        attacks=2, pdam=DiceFormula.from_str('1d12 + 1d4'), damage_type=DamageType.piercing,
        cdam=14),
    Weapons.lunaweave_compound_bow: Weapon(
        name=Weapons.lunaweave_compound_bow.name, price=4000, picture=WeaponPicture.blue_bow,
        style=Style.ranged, equip_type=Type.heavy, is_two_handed=True,
        min_range=3, max_range=16, shape=Shape.range_point, pac=1, min_dex=3,
        attacks=2, pdam=DiceFormula.from_str('1d12 + 1d10'), damage_type=DamageType.piercing,
        cdam=20),
    Weapons.lunasteel_compound_bow: Weapon(
        name=Weapons.lunasteel_compound_bow.name, price=12500, picture=WeaponPicture.orange_bow,
        style=Style.ranged, equip_type=Type.heavy, is_two_handed=True,
        min_range=3, max_range=17, shape=Shape.range_point, pac=1, min_dex=4,
        attacks=3, pdam=DiceFormula.from_str('1d20'), damage_type=DamageType.piercing,
        cdam=20),

    Weapons.bronze_wand: Weapon(
        name=Weapons.bronze_wand.name, price=40, picture=WeaponPicture.orange_rod,
        style=Style.magic, min_range=1, max_range=6, shape=Shape.range_point, mdef=1, vis=1,
        attacks=2, mdam=DiceFormula.from_str('1d4'), damage_type=DamageType.force,
        cdam=2),
    Weapons.iron_wand: Weapon(
        name=Weapons.iron_wand.name, price=175, picture=WeaponPicture.red_rod, min_dex=1,
        style=Style.magic, min_range=1, max_range=6, shape=Shape.range_point, mdef=1, bmac=1,
        vis=1,
        attacks=2, mdam=DiceFormula.from_str('1d6'), damage_type=DamageType.force,
        cdam=3),
    Weapons.steel_wand: Weapon(
        name=Weapons.steel_wand.name, price=875, picture=WeaponPicture.blue_rod, min_dex=2,
        style=Style.magic, min_range=1, max_range=7, shape=Shape.range_point, mdef=2, bmac=2,
        vis=1,
        attacks=2, mdam=DiceFormula.from_str('1d8'), damage_type=DamageType.force,
        cdam=4),
    # Pandoras Kiss.
    Weapons.lunaweave_wand: Weapon(
        name=Weapons.lunaweave_wand.name, price=3250, picture=WeaponPicture.purple_rod, min_dex=3,
        style=Style.magic, min_range=1, max_range=7, shape=Shape.range_point, mdef=2, bmac=2,
        reg=2, vis=1,
        attacks=2, mdam=DiceFormula.from_str('1d10'), damage_type=DamageType.force,
        cdam=5),
    Weapons.lunasteel_wand: Weapon(
        name=Weapons.lunasteel_wand.name, price=8750, picture=WeaponPicture.teal_rod, min_dex=4,
        style=Style.magic, min_range=1, max_range=8, shape=Shape.range_point, mdef=3, bmac=3,
        reg=3, vis=1,
        attacks=2, mdam=DiceFormula.from_str('1d12'), damage_type=DamageType.force,
        cdam=5),

    Weapons.bronze_staff: Weapon(
        name=Weapons.bronze_staff.name, price=50, picture=WeaponPicture.wooden_staff,
        style=Style.magic, equip_type=Type.medium, is_two_handed=True,
        min_range=2, max_range=9, shape=Shape.range_circle, vis=1,
        mdam=DiceFormula.from_str('1d4'), damage_type=DamageType.force,
        cdam=4, effect='+1MP on hit'),
    Weapons.iron_staff: Weapon(
        name=Weapons.iron_staff.name, price=200, picture=WeaponPicture.grey_staff,
        style=Style.magic, equip_type=Type.medium, is_two_handed=True, min_dex=1,
        min_range=2, max_range=9, shape=Shape.range_circle, bmac=1, vis=1,
        mdam=DiceFormula.from_str('1d6'), damage_type=DamageType.force,
        cdam=6, effect='+1MP on hit'),
    Weapons.volcanic_staff: Weapon(
        name=Weapons.volcanic_staff.name, price=450, picture=WeaponPicture.flame_staff,
        style=Style.magic, equip_type=Type.medium, is_two_handed=True, min_dex=2,
        rarity=Rarity.set,
        min_range=2, max_range=10, shape=Shape.range_circle, bmac=1, vis=1,
        mdam=DiceFormula.from_str('1d6'), damage_type=DamageType.fire,
        cdam=6, effect='+1MP on hit, +2 MDAM on Fire abilities'),
    Weapons.thunder_staff: Weapon(
        name=Weapons.thunder_staff.name, price=450, picture=WeaponPicture.yellow_blue_staff,
        style=Style.magic, equip_type=Type.medium, is_two_handed=True, min_dex=2,
        rarity=Rarity.rare,
        min_range=2, max_range=10, shape=Shape.range_circle, bmac=1, vis=1,
        mdam=DiceFormula.from_str('1d6'), damage_type=DamageType.lightning,
        cdam=6, effect='+1MP on hit, Lightning abilities Stun 1RND'),
    Weapons.coral_staff: Weapon(
        name=Weapons.coral_staff.name, price=450, picture=WeaponPicture.teal_staff,
        style=Style.magic, equip_type=Type.medium, is_two_handed=True, min_dex=2,
        rarity=Rarity.set,
        min_range=2, max_range=10, shape=Shape.range_circle, bmac=1, vis=1,
        mdam=DiceFormula.from_str('1d6'), damage_type=DamageType.cold,
        cdam=6, effect='+1MP on hit, Ice abilities cost -1MP'),
    Weapons.steel_staff: Weapon(
        name=Weapons.steel_staff.name, price=1000, picture=WeaponPicture.purple_cross_staff,
        style=Style.magic, equip_type=Type.medium, is_two_handed=True, min_dex=2,
        min_range=2, max_range=10, shape=Shape.range_circle, bmac=2, vis=1,
        mdam=DiceFormula.from_str('1d8'), damage_type=DamageType.force,
        cdam=8, effect='+1MP on hit'),
    Weapons.lunaweave_staff: Weapon(
        name=Weapons.lunaweave_staff.name, price=3500, picture=WeaponPicture.purple_staff,
        style=Style.magic, equip_type=Type.medium, is_two_handed=True, min_dex=3,
        min_range=2, max_range=11, shape=Shape.range_circle, bmac=2, reg=2, vis=1,
        mdam=DiceFormula.from_str('1d12'), damage_type=DamageType.force,
        cdam=12, effect='+2MP on hit'),
    Weapons.lunasteel_staff: Weapon(
        name=Weapons.lunasteel_staff.name, price=10000, picture=WeaponPicture.yellow_red_staff,
        style=Style.magic, equip_type=Type.medium, is_two_handed=True, min_dex=4,
        min_range=2, max_range=12, shape=Shape.range_circle, bmac=3, reg=3, vis=1,
        mdam=DiceFormula.from_str('1d20'), damage_type=DamageType.force,
        cdam=20, effect='+3MP on hit'),

    Weapons.pistol: Weapon(
        name=Weapons.pistol.name, price=40, picture=WeaponPicture.normal_pistol,
        style=Style.ranged,
        min_range=1, max_range=6, shape=Shape.range_point,
        attacks=1, pdam=DiceFormula.from_str('d4'), damage_type=DamageType.piercing),
    Weapons.pistol_mark_2: Weapon(
        name=Weapons.pistol_mark_2.name, price=175, picture=WeaponPicture.brown_pistol,
        style=Style.ranged, min_dex=1, min_range=1, max_range=7, shape=Shape.range_point,
        attacks=2, pdam=DiceFormula.from_str('d4'), damage_type=DamageType.piercing),
    Weapons.pistol_mark_3: Weapon(
        name=Weapons.pistol_mark_3.name, price=850, picture=WeaponPicture.white_pistol,
        style=Style.ranged, min_dex=2, min_range=1, max_range=8, shape=Shape.range_point,
        attacks=2, pdam=DiceFormula.from_str('d6'), damage_type=DamageType.piercing),
    Weapons.lunaweave_pistol: Weapon(
        name=Weapons.lunaweave_pistol.name, price=2800, picture=WeaponPicture.blue_pistol,
        style=Style.ranged, min_dex=3, min_range=1, max_range=9, shape=Shape.range_point,
        attacks=3, pdam=DiceFormula.from_str('d6'), damage_type=DamageType.piercing,
        effect='On crit, +1MP'),

    Weapons.rifle: Weapon(
        name=Weapons.rifle.name, price=50, picture=WeaponPicture.normal_rifle,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True,
        min_range=2, max_range=15, shape=Shape.range_point, pac=1,
        attacks=1, pdam=DiceFormula.from_str('d12'), damage_type=DamageType.piercing,
        cdam=12),
    Weapons.rifle_mark_2: Weapon(
        name=Weapons.rifle_mark_2.name, price=250, picture=WeaponPicture.orange_rifle,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True, min_dex=1,
        min_range=2, max_range=16, shape=Shape.range_point, pac=1,
        attacks=1, pdam=DiceFormula.from_str('d20'), damage_type=DamageType.piercing,
        cdam=20),
    Weapons.rifle_mark_2_scoped: Weapon(
        name=Weapons.rifle_mark_2_scoped.name, price=550, picture=WeaponPicture.orange_rifle,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True, min_dex=1,
        min_range=2, max_range=17, shape=Shape.range_point, pac=3,
        attacks=1, pdam=DiceFormula.from_str('d20'), damage_type=DamageType.piercing,
        cdam=20),
    Weapons.rifle_mark_3: Weapon(
        name=Weapons.rifle_mark_3.name, price=1100, picture=WeaponPicture.purple_rifle,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True, min_dex=2,
        min_range=2, max_range=17, shape=Shape.range_point, pac=1,
        attacks=1, pdam=DiceFormula.from_str('d20 + d6'), damage_type=DamageType.piercing,
        cdam=26),
    Weapons.rifle_mark_3_scoped: Weapon(
        name=Weapons.rifle_mark_3_scoped.name, price=1550, picture=WeaponPicture.purple_rifle,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True, min_dex=2,
        min_range=2, max_range=18, shape=Shape.range_point, pac=3,
        attacks=1, pdam=DiceFormula.from_str('d20 + d6'), damage_type=DamageType.piercing,
        cdam=26),
    Weapons.lunaweave_rifle: Weapon(
        name=Weapons.lunaweave_rifle.name, price=3500, picture=WeaponPicture.flame_rifle,
        style=Style.ranged, equip_type=Type.medium, is_two_handed=True, min_dex=2,
        min_range=2, max_range=18, shape=Shape.range_point, pac=1,
        attacks=1, pdam=DiceFormula.from_str('2d20'), damage_type=DamageType.piercing,
        mdam=DiceFormula.from_str('1d10'),
        cdam=40),

    Weapons.shotgun: Weapon(
        name=Weapons.shotgun.name, price=75, picture=WeaponPicture.normal_shotgun,
        style=Style.ranged, equip_type=Type.medium,
        min_range=1, max_range=3, shape=Shape.cone_3,
        attacks=1, pdam=DiceFormula.from_str('d6'), damage_type=DamageType.bludgeoning,
        cdam=6),
    Weapons.shotgun_mark_2: Weapon(
        name=Weapons.shotgun_mark_2.name, price=450, picture=WeaponPicture.brown_shotgun,
        style=Style.ranged, equip_type=Type.medium, min_dex=1,
        min_range=1, max_range=3, shape=Shape.cone_3,
        attacks=1, pdam=DiceFormula.from_str('d10'), damage_type=DamageType.bludgeoning,
        cdam=10),
    Weapons.shotgun_mark_3: Weapon(
        name=Weapons.shotgun_mark_3.name, price=1200, picture=WeaponPicture.white_shotgun,
        style=Style.ranged, equip_type=Type.medium, min_dex=2,
        min_range=1, max_range=3, shape=Shape.cone_3,
        attacks=2, pdam=DiceFormula.from_str('d8'), damage_type=DamageType.bludgeoning,
        cdam=8, effect='If attack KOs enemy, may perform another physical ATTACK'),
    Weapons.lunaweave_shotgun: Weapon(
        name=Weapons.lunaweave_shotgun.name, price=3600, picture=WeaponPicture.blue_shotgun,
        style=Style.ranged, equip_type=Type.medium, min_dex=3,
        min_range=1, max_range=3, shape=Shape.cone_3,
        attacks=2, pdam=DiceFormula.from_str('1d12 + 1d4'), damage_type=DamageType.bludgeoning,
        cdam=12, effect='On Crit, Stun 1RND'),
}


class Items(aenum.AutoNumberEnum):
    empty = ()
    disguise_kit = ()
    apprentice_disguise_kit = ()
    master_disguise_kit = ()
    lock_pick = ()
    apprentice_lock_pick = ()
    master_lock_pick = ()
    bronze_manacles = ()
    iron_manacles = ()
    steel_manacles = ()


items = {
    Items.empty: Item(name=Items.empty.name, effect=''),
    Items.disguise_kit: Item(name=Items.disguise_kit.name, price=5,
                             effect='Allows Disguise Self check'),
    Items.apprentice_disguise_kit: Item(
        name=Items.apprentice_disguise_kit.name, price=50,
        effect='Allows Disguise Self check, +3STE, Magically alters sound of voice (15STE), Can '
               'disguise gender (18STE)'),
    Items.master_disguise_kit: Item(
        name=Items.master_disguise_kit.name, price=500, rarity=Rarity.rare,
        effect='Allows Disguise Self check, +5STE, Magically alters sound of voice (15STE), Can '
               'change race (18STE), Appear exactly like a target individual (20STE)'),
    Items.lock_pick: Item(name=Items.lock_pick.name, price=5, effect='Allows Open Lock'),
    Items.apprentice_lock_pick: Item(name=Items.apprentice_lock_pick.name, price=50,
                                     effect='Allows Open Lock, +3STE'),
    Items.master_lock_pick: Item(name=Items.master_lock_pick.name, price=500, rarity=Rarity.rare,
                                 effect='Allows Open Lock, Automatic success'),
    Items.bronze_manacles: Item(name=Items.bronze_manacles.name, price=50,
                                effect='15STE to escape, 1 attempt per hr'),
    Items.iron_manacles: Item(name=Items.iron_manacles.name, price=500,
                              effect='20STE & 20APT to escape, 1 attempt per hr'),
    Items.steel_manacles: Item(name=Items.steel_manacles.name, price=2000, rarity=Rarity.rare,
                               effect='20STE, 20APT & 20ATH to escape, 1 attempt per hr'),
}
