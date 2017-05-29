from enum import auto, Enum

from .dice import DiceFormula
from .equipment import (Chest, DamageType, DamageTypeSet, Feet, Hand, Head, Item, Neck, Rarity,
                        Shape, Shield, Slot, Style, Type, Utility, VulnerabilitySet, Weapon,
                        WeaponPicture)


def get_item(slot: Slot, item_index: int) -> Item:
    if slot is Slot.item:
        item_dict = items
        item_enum = Items
    elif slot is Slot.utility:
        item_dict = utilities
        item_enum = Utilities
    elif slot is Slot.weapon:
        item_dict = weapons
        item_enum = Weapons
    elif slot is Slot.head:
        item_dict = heads
        item_enum = Heads
    elif slot is Slot.neck:
        item_dict = necks
        item_enum = Necks
    elif slot is Slot.chest:
        item_dict = chests
        item_enum = Chests
    elif slot is Slot.shield:
        item_dict = shields
        item_enum = Shields
    elif slot is Slot.hand:
        item_dict = hands
        item_enum = Hands
    elif slot is Slot.feet:
        item_dict = feets
        item_enum = Feets
    else:
        raise NotImplementedError(f'Unexpected slot: {slot}')

    return item_dict[item_enum(item_index)]


class Utilities(Enum):
    # TODO: Remove "empty" as there is no longer a Utility slot.
    empty = auto()
    candle = auto()
    rope_kit = auto()
    crowbar = auto()
    hammer = auto()
    pickaxe = auto()
    tinder_box = auto()
    fishing_net = auto()
    harp = auto()
    mandolin = auto()
    bugle = auto()
    snorkle = auto()
    torch = auto()
    medical_kit = auto()
    grappling_hook = auto()
    gliding_suit = auto()
    communication_orb = auto()
    repelling_gear = auto()
    bow_cable = auto()
    magnifying_glass = auto()
    binoculars = auto()
    lantern = auto()
    spider_gloves = auto()
    flare_gun = auto()
    grappling_gun = auto()
    detect_realm = auto()
    dwarven_crystal_lantern = auto()
    mirrored_lunacite_lantern = auto()


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
                                    rarity=Rarity.rare, effect='Allows gliding flight'),
    Utilities.communication_orb: Utility(name=Utilities.communication_orb.name, price=500,
                                         min_int=1, rarity=Rarity.rare,
                                         effect='Paried with another communication orb, allows '
                                                'communication at great distance'),
    Utilities.repelling_gear: Utility(name=Utilities.repelling_gear.name, price=500, min_int=1,
                                      effect='Allows repelling down a wall or cliff'),
    Utilities.bow_cable: Utility(name=Utilities.bow_cable.name, price=500, min_int=1,
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


class Heads(Enum):
    empty = auto()
    cursed_helm = auto()
    mako_hood = auto()
    adept_hood = auto()
    adamantine_circlet = auto()
    hero_mask = auto()
    mako_helm = auto()
    techno_eyepiece = auto()
    apprentice_helm = auto()
    lunafabric_hood = auto()
    telescoping_lenses = auto()
    volcanic_helm = auto()
    rusty_bucket = auto()
    circlet_of_healing = auto()
    circlet_of_power = auto()
    circlet_of_telepathy = auto()
    mako_guard = auto()
    mithril_earrings = auto()
    mithril_headband = auto()
    adamantine_helmet = auto()
    avenger_circlet = auto()
    sapphire_circlet = auto()
    obsidian_tiara = auto()
    lunatech_helm = auto()
    lunafiber_hood = auto()
    lunaburn_circlet = auto()
    mithril_tiara = auto()
    mithril_coronet = auto()


heads = {
    Heads.empty: Head(name=Heads.empty.name),
    Heads.cursed_helm: Head(name=Heads.cursed_helm.name, price=0, min_int=0, reg=2,
                            rarity=Rarity.set, effect='+2PDAM per ATTACK. Resist corruption 2RND'),
    Heads.mako_hood: Head(name=Heads.mako_hood.name, price=50, mp=2),
    Heads.adept_hood: Head(name=Heads.adept_hood.name, price=125, reg=1),
    Heads.adamantine_circlet: Head(name=Heads.adamantine_circlet.name, price=125, mdef=1),
    Heads.hero_mask: Head(name=Heads.hero_mask.name, price=350, min_int=1,
                          effect='+5STE when disguising, +5SPE with common'),
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


class Necks(Enum):
    empty = auto()
    mako_amulet = auto()
    spinal_support = auto()
    crystal_amulet = auto()
    starlet_necklace = auto()
    heavy_quiver = auto()
    equalizer = auto()
    ammo_sash = auto()
    foregrip = auto()
    adamantine_amulet = auto()
    range_finder = auto()
    suppressor = auto()
    duraform_pendant = auto()
    lunavein_necklace = auto()
    long_barrel = auto()
    lunahollow_necklace = auto()
    overcharge_amulet = auto()
    emerald_amulet = auto()
    mithril_riviere = auto()
    lunaburn_amulet = auto()
    sapphire_amulet = auto()
    obsidian_necklace = auto()
    augmenter = auto()
    mithril_amulet = auto()
    omni_amulet = auto()


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


class Chests(Enum):
    empty = auto()
    hopper_scale = auto()
    spurclaw_scale = auto()
    griffon_hide = auto()
    hardened_griffon_hide = auto()
    bulletsteel = auto()
    ursa_hide = auto()
    hardened_ursa_hide = auto()
    lunaweave_cloth = auto()
    fitted_lunaweave_cloth = auto()
    lunasteel_robe = auto()
    omni_robe = auto()

    bronze_chain = auto()
    hardened_bronze_chain = auto()
    iron_chain = auto()
    hardened_iron_chain = auto()
    steel_chain = auto()
    hardened_steel_chain = auto()
    lunaweave_chain = auto()
    hardened_lunaweave_chain = auto()
    lunasteel_chain = auto()
    hardened_lunasteel_chain = auto()
    omni_chain = auto()

    bronze_plate = auto()
    hardened_bronze_plate = auto()
    iron_plate = auto()
    hardened_iron_plate = auto()
    steel_plate = auto()
    hardened_steel_plate = auto()
    lunaweave_plate = auto()
    hardened_lunaweave_plate = auto()
    lunasteel_plate = auto()
    hardened_lunasteel_plate = auto()
    omni_plate = auto()

    cursed_plate = auto()
    coral_slate = auto()
    volcanic_slate = auto()
    lunatech_chest = auto()
    lunafiber_robe = auto()


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
                              rarity=Rarity.rare, pdef=1, pred=1, speed=-0.5),
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


class Shields(Enum):
    empty = auto()
    bronze_buckler = auto()
    iron_buckler = auto()
    plated_iron_buckler = auto()
    steel_buckler = auto()
    plated_steel_buckler = auto()
    arachnid_shield = auto()
    mithril_shield = auto()
    lunaweave_buckler = auto()
    plated_lunaweave_buckler = auto()
    lunasteel_buckler = auto()
    plated_lunasteel_buckler = auto()
    omni_buckler = auto()

    bronze_kite_shield = auto()
    plated_bronze_kite_shield = auto()
    bouncer = auto()
    iron_kite_shield = auto()
    plated_iron_kite_shield = auto()
    interlocking_kite_shield = auto()
    steel_kite_shield = auto()
    plated_steel_kite_shield = auto()
    spine_shield = auto()
    lunaweave_kite_shield = auto()
    plated_lunaweave_kite_shield = auto()
    lunasteel_kite_shield = auto()
    plated_lunasteel_kite_shield = auto()
    omni_kite_shield = auto()

    bronze_tower_shield = auto()
    plated_bronze_tower_shield = auto()
    double_handled_shield = auto()
    iron_tower_shield = auto()
    plated_iron_tower_shield = auto()
    extendable_brace_shield = auto()
    the_two_towers = auto()
    steel_tower_shield = auto()
    plated_steel_tower_shield = auto()
    adamantine_shield = auto()
    lunaweave_tower_shield = auto()
    plated_lunaweave_tower_shield = auto()
    lunasteel_tower_shield = auto()
    plated_lunasteel_tower_shield = auto()
    omni_tower_shield = auto()

    cursed_shield = auto()
    coral_shield = auto()
    volcanic_shield = auto()


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


class Hands(Enum):
    empty = auto()
    bronze_gauntlets = auto()
    adamantine_ring = auto()
    mako_ring = auto()
    lunaweave_ring = auto()
    locking_glove = auto()
    gill_ring = auto()
    fencing_glove = auto()
    emerald_ring = auto()
    fire_ring = auto()
    iron_gauntlets = auto()
    universal_donor = auto()
    ruby_ring = auto()
    feather_glove = auto()
    reinforced_bangle = auto()
    ring_of_regen = auto()
    stone_ring = auto()
    diamond_ring = auto()
    diamond_bangles = auto()
    colossus_armlet = auto()
    ring_of_communication = auto()
    shield_bearer = auto()
    stabilizer = auto()
    steel_gauntlets = auto()
    titan_joint = auto()
    dueling_glove = auto()
    slotted_gauntlet = auto()

    coral_gauntlets = auto()
    volcanic_gauntlets = auto()
    lunatech_gauntlets = auto()
    obsidian_gauntlets = auto()
    lunafiber_glove = auto()


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


class Feets(Enum):
    empty = auto()
    nighthawke_boots = auto()
    spiked_soles = auto()
    iron_brackets = auto()
    fencing_boots = auto()
    tender_soles = auto()
    fortified_greaves = auto()
    flippers = auto()
    claw_shoes = auto()
    reflex_soles = auto()
    juggernaut_greaves = auto()
    racers = auto()
    sprinting_shoes = auto()
    trailblazers = auto()
    dodgers = auto()
    inertial_helix = auto()
    three_heroes = auto()
    lunabeam_walkers = auto()
    ocean_striders = auto()
    cloud_walkers = auto()
    gyro_heels = auto()
    earth_clamps = auto()
    whirlwind_greaves = auto()
    rebound_greaves = auto()
    skywalker_boots = auto()
    wind_boots = auto()
    topaz_slippers = auto()
    wind_striders = auto()
    flashers = auto()
    ocean_born = auto()
    mithril_boots = auto()
    grooved_soles = auto()
    cursed_greaves = auto()
    coral_greaves = auto()
    volcanic_greaves = auto()
    lunatech_boots = auto()
    lunafiber_slippers = auto()


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
                                          'by hitting an enemy deals SPEED PDAM and knocks back '
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


class Weapons(Enum):
    empty = auto()
    fists = auto()

    bronze_wrist_blades = auto()
    iron_wrist_blades = auto()
    volcanic_wrist_blades = auto()
    reflex_claw = auto()
    steel_wrist_blades = auto()
    lunaweave_wrist_blades = auto()
    lunasteel_wrist_blades = auto()

    bronze_rapier = auto()
    iron_rapier = auto()
    steel_rapier = auto()
    cursed_rapier = auto()
    lunaweave_rapier = auto()
    lunasteel_rapier = auto()

    bronze_knuckle = auto()
    iron_knuckle = auto()
    steel_knuckle = auto()
    lunaweave_knuckle = auto()
    lunasteel_knuckle = auto()

    bronze_chain_whip = auto()
    iron_chain_whip = auto()
    steel_chain_whip = auto()
    lunaweave_chain_whip = auto()
    lunasteel_chain_whip = auto()

    bronze_claws = auto()
    iron_claws = auto()
    dragon_claws = auto()
    steel_claws = auto()
    lunaweave_claws = auto()
    lunasteel_claws = auto()

    bronze_longsword = auto()
    iron_longsword = auto()
    moonbeam = auto()
    steel_longsword = auto()
    lunaweave_longsword = auto()
    lunasteel_longsword = auto()

    bronze_broadsword = auto()
    iron_broadsword = auto()
    braveheart = auto()
    steel_broadsword = auto()
    lunaweave_broadsword = auto()
    lunasteel_broadsword = auto()

    bronze_double_bladed_spear = auto()
    iron_double_bladed_spear = auto()
    savior = auto()
    steel_double_bladed_spear = auto()
    lunaweave_double_bladed_spear = auto()
    lunasteel_double_bladed_spear = auto()

    bronze_lance = auto()
    iron_lance = auto()
    ashers_pride = auto()
    steel_lance = auto()
    lunaweave_lance = auto()
    lunasteel_lance = auto()

    bronze_hammer = auto()
    iron_hammer = auto()
    steel_hammer = auto()
    lunaweave_hammer = auto()
    lunasteel_hammer = auto()

    bronze_flail = auto()
    iron_flail = auto()
    steel_flail = auto()
    lunaweave_flail = auto()
    lunasteel_flail = auto()

    bronze_war_axe = auto()
    iron_war_axe = auto()
    harbinger = auto()
    steel_war_axe = auto()
    lunaweave_war_axe = auto()
    lunasteel_war_axe = auto()

    bronze_great_sword = auto()
    iron_great_sword = auto()
    vengeant = auto()
    leave_n_cleave = auto()
    steel_great_sword = auto()
    obsidian_blade = auto()
    lunaweave_great_sword = auto()
    lunasteel_great_sword = auto()

    bronze_shuriken = auto()
    iron_shuriken = auto()
    volcanic_shuriken = auto()
    nightwind = auto()
    steel_shuriken = auto()
    lunaweave_shuriken = auto()
    lunasteel_shuriken = auto()

    bronze_longbow = auto()
    iron_longbow = auto()
    volcanic_longbow = auto()
    steel_longbow = auto()
    lunaweave_longbow = auto()
    lunasteel_longbow = auto()

    bronze_ternate_crossbow = auto()
    iron_ternate_crossbow = auto()
    steel_ternate_crossbow = auto()
    lunaweave_ternate_crossbow = auto()
    lunasteel_ternate_crossbow = auto()

    bronze_compound_bow = auto()
    iron_compound_bow = auto()
    avenger = auto()
    steel_compound_bow = auto()
    lunaweave_compound_bow = auto()
    lunasteel_compound_bow = auto()

    bronze_wand = auto()
    iron_wand = auto()
    steel_wand = auto()
    pandoras_kiss = auto()
    lunaweave_wand = auto()
    lunasteel_wand = auto()

    bronze_staff = auto()
    iron_staff = auto()
    volcanic_staff = auto()
    thunder_staff = auto()
    coral_staff = auto()
    steel_staff = auto()
    lunaweave_staff = auto()
    lunasteel_staff = auto()

    pistol = auto()
    pistol_mark_2 = auto()
    pistol_mark_3 = auto()
    golden_gun = auto()
    lunaweave_pistol = auto()

    rifle = auto()
    rifle_mark_2 = auto()
    rifle_mark_2_scoped = auto()
    rifle_mark_3 = auto()
    rifle_mark_3_scoped = auto()
    lunaweave_rifle = auto()

    shotgun = auto()
    shotgun_mark_2 = auto()
    purifier = auto()
    shotgun_mark_3 = auto()
    lunaweave_shotgun = auto()


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
        cdam=6, effect='+1MP on hit, Passively grants wielder Lightning Shield II'),
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
    Weapons.golden_gun: Weapon(
        name=Weapons.golden_gun.name, price=1950, picture=WeaponPicture.orange_pistol,
        rarity=Rarity.unique, pac=-3,
        style=Style.ranged, min_dex=2, min_range=1, max_range=5, shape=Shape.range_point,
        attacks=1, pdam=DiceFormula.from_str('d100'), damage_type=DamageType.piercing,
        effect='Wielder spends FullA and 5MP to attack. Cooldown 5RND.'),
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
    Weapons.purifier: Weapon(
        name=Weapons.purifier.name, price=975, picture=WeaponPicture.white_shotgun,
        style=Style.ranged, equip_type=Type.medium, min_dex=1, rarity=Rarity.unique,
        min_range=1, max_range=3, shape=Shape.cone_3,
        attacks=1, pdam=DiceFormula.from_str('d10'), damage_type=DamageType.bludgeoning,
        cdam=10, effect='Blind'),
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


class Items(Enum):
    empty = auto()
    disguise_kit = auto()
    apprentice_disguise_kit = auto()
    master_disguise_kit = auto()
    lock_pick = auto()
    apprentice_lock_pick = auto()
    master_lock_pick = auto()
    bronze_manacles = auto()
    iron_manacles = auto()
    steel_manacles = auto()


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
