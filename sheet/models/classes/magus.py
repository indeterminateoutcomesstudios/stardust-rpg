from ..ability import Ability, AbilityPicture, DurationUnit, Time
from ..class_type import Class
from ..equipment import DamageType, Shape

# Tier 1.
fireball_1 = Ability(
    name='Fireball I', picture=AbilityPicture.fire,
    mp_cost=2, attacks=2, mdam='1d4',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.std_ab_a, max_range='6',
    shape=Shape.circle, target_area='1RAD',
)

fireball_2 = Ability(
    name='Fireball II', picture=AbilityPicture.fire,
    mp_cost=3, attacks=2, mdam='1d6+WIS',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.std_ab_a, max_range='8',
    shape=Shape.circle, target_area='1RAD',
    prerequisites=(fireball_1,)
)

fireball_3 = Ability(
    name='Fireball III', picture=AbilityPicture.fire,
    mp_cost=4, attacks=2, mdam='1d8+WIS',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.std_ab_a, max_range='10',
    shape=Shape.circle, target_area='1RAD',
    prerequisites=(fireball_2,)
)

lightning_shield_1 = Ability(
    name='Lightning Shield I', picture=AbilityPicture.shield_oath,
    mp_cost=2, attacks=1, mdam='1d4+WIS',
    damage_type=DamageType.lightning, targets_mdef=True, max_range='3',
    target_area='1 ally', duration='3', duration_unit=DurationUnit.rnd,
    effect='Electric force field damages enemies who successfully melee attack shielded target'
)

lightning_shield_2 = Ability(
    name='Lightning Shield II', picture=AbilityPicture.shield_oath,
    mp_cost=2, attacks=1, mdam='1d6+WIS',
    damage_type=DamageType.lightning, targets_mdef=True, max_range='5',
    target_area='1 ally', duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Electric force field damages enemies who successfully melee attack shielded target',
    prerequisites=(lightning_shield_1,)
)

lightning_shield_3 = Ability(
    name='Lightning Shield III', picture=AbilityPicture.shield_oath,
    mp_cost=3, attacks=1, mdam='1d8+WIS',
    damage_type=DamageType.lightning, targets_mdef=True, max_range='7',
    target_area='1 ally', duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Electric force field damages enemies who successfully melee or range attack shielded '
           'target',
    prerequisites=(lightning_shield_2,)
)

ice_wall_1 = Ability(
    name='Ice Wall I', picture=AbilityPicture.hyoton,
    mp_cost=2, max_range='8', target_area='7DIS long, 1DIS wide, 1DIS high line',
    duration='8', duration_unit=DurationUnit.rnd,
    effect='Creates a wall of ice.  Each section has 10HP',
)

ice_wall_2 = Ability(
    name='Ice Wall II', picture=AbilityPicture.hyoton,
    mp_cost=4, max_range='10', target_area='10DIS long, 1DIS wide, 1DIS high line',
    duration='8', duration_unit=DurationUnit.rnd,
    effect='Creates a wall of ice.  Each section has [[10+5*WIS]]HP',
    prerequisites=(ice_wall_1,)
)

ice_wall_3 = Ability(
    name='Ice Wall III', picture=AbilityPicture.hyoton,
    mp_cost=6, max_range='12', target_area='[[13+WIS]]DIS long, 1DIS wide, 1DIS high line',
    duration='8+WIS', duration_unit=DurationUnit.rnd,
    effect='Creates a wall of ice.  Each section has [[25+10*WIS]]HP',
    prerequisites=(ice_wall_2,)
)

ice_slick_1 = Ability(
    name='Ice Slick I', picture=AbilityPicture.blizzard,
    mp_cost=3, attacks=1, mdam='1d2',
    damage_type=DamageType.cold, targets_mdef=True, max_range='5',
    shape=Shape.circle, target_area='Up to 2RAD', duration='4', duration_unit=DurationUnit.rnd,
    effect='Creates a slippery patch of ice.  Enemies who fail MDEF are immobilized for 1RND'
)

ice_slick_2 = Ability(
    name='Ice Slick II', picture=AbilityPicture.blizzard,
    mp_cost=4, attacks=1, mdam='1d2',
    damage_type=DamageType.cold, targets_mdef=True, max_range='7',
    shape=Shape.circle, target_area='Up to 2RAD', duration='6', duration_unit=DurationUnit.rnd,
    effect='Creates a slippery patch of ice.  Enemies who fail MDEF are immobilized for 1RND',
    prerequisites=(ice_slick_1,)
)

ice_slick_3 = Ability(
    name='Ice Slick III', picture=AbilityPicture.blizzard,
    mp_cost=4, attacks=1, mdam='1d4',
    damage_type=DamageType.cold, targets_mdef=True, max_range='7',
    shape=Shape.circle, target_area='Up to [[2+WIS]]RAD',
    duration='6', duration_unit=DurationUnit.rnd,
    effect='Creates a slippery patch of ice.  Enemies who fail MDEF are immobilized for 1RND',
    prerequisites=(ice_slick_2,)
)

imbue_weapon_1 = Ability(
    name='Imbue Weapon I', picture=AbilityPicture.awareness,
    mp_cost=2, max_range='5', target_area='1 ally',
    duration='6', duration_unit=DurationUnit.rnd,
    effect='Imbues ally\'s weapon with ice.  Successful physical attacks apply -[[1+WIS]]SPEED. '
           'Can cast once per RND.'
)

imbue_weapon_2 = Ability(
    name='Imbue Weapon II', picture=AbilityPicture.awareness,
    mp_cost=3, max_range='5', target_area='1 ally',
    duration='6', duration_unit=DurationUnit.rnd,
    effect='Imbues ally\'s weapon with lightning. Successful or unsuccessful physical attacks '
           'apply [[1+WIS]]MDAM. Can cast once per RND.',
    prerequisites=(imbue_weapon_1,)
)

imbue_weapon_3 = Ability(
    name='Imbue Weapon III', picture=AbilityPicture.awareness,
    mp_cost=4, max_range='5', target_area='1 ally',
    duration='6', duration_unit=DurationUnit.rnd,
    effect='Imbues ally\'s weapon with fire.  Successful physical attacks burn [[1+WIS]]MDAM for '
           '3RND. Can cast once per RND.',
    prerequisites=(imbue_weapon_2,)
)

# Tier 2.
inferno_1 = Ability(
    name='Inferno I', picture=AbilityPicture.fire_2,
    mp_cost=6, attacks=1, mdam='3d6',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.std_ab_a,
    min_range='1', max_range='3', shape=Shape.cone, target_area='3DIS cone',
    prerequisites=(fireball_3, imbue_weapon_3)
)

inferno_2 = Ability(
    name='Inferno II', picture=AbilityPicture.fire_2,
    mp_cost=10, attacks=2, mdam='1d10+WIS',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.std_ab_a,
    min_range='1', max_range='3', shape=Shape.cone, target_area='3DIS cone',
    prerequisites=(inferno_1,)
)

inferno_3 = Ability(
    name='Inferno III', picture=AbilityPicture.fire_2,
    mp_cost=14, attacks=3, mdam='1d10+2*WIS',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.std_ab_a,
    min_range='1', max_range='3', shape=Shape.cone, target_area='3DIS cone',
    prerequisites=(inferno_2,)
)

sunray_1 = Ability(
    name='Sunray I', picture=AbilityPicture.flaming_arrow,
    mp_cost=3, attacks=1, mdam='1d8+WIS',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.std_ab_a,
    shape=Shape.halo, target_area='1RAD Halo',
    effect='Sunray shoots down onto caster and explodes outward knocking back creatures 2DIS. '
           'and immobilizes',
    prerequisites=(fireball_2, imbue_weapon_3)
)

sunray_2 = Ability(
    name='Sunray II', picture=AbilityPicture.flaming_arrow,
    mp_cost=5, attacks=1, mdam='1d8+2*WIS',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.std_ab_a,
    shape=Shape.halo, target_area='2RAD Halo',
    effect='Sunray shoots down onto caster and explodes outward knocking back creatures 2DIS and '
           'staggering',
    prerequisites=(sunray_1,)
)

sunray_3 = Ability(
    name='Sunray III', picture=AbilityPicture.flaming_arrow,
    mp_cost=8, attacks=1, mdam='2d8+2*WIS',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.std_ab_a,
    shape=Shape.halo, target_area='2RAD Halo',
    effect='Sunray shoots down onto caster and explodes outward knocking back creatures 2DIS and '
           'disabling',
    prerequisites=(sunray_2,)
)

lightning_strike_1 = Ability(
    name='Lightning Strike I', picture=AbilityPicture.thunder_2,
    mp_cost=6, attacks=1, mdam='1d12',
    damage_type=DamageType.lightning, targets_mdef=True, time=Time.std_ab_a,
    shape=Shape.multi_point, max_range='10', target_area='One creature per bolt',
    effect='2 lightning bolts strike enemies.  Maximum of 1 bolt per target.',
    prerequisites=(lightning_shield_3, ice_slick_2, imbue_weapon_2)
)

lightning_strike_2 = Ability(
    name='Lightning Strike II', picture=AbilityPicture.thunder_2,
    mp_cost=10, attacks=1, mdam='1d12+WIS',
    damage_type=DamageType.lightning, targets_mdef=True, time=Time.std_ab_a,
    shape=Shape.multi_point, max_range='12', target_area='One creature per bolt',
    effect='[[2+WIS]] lightning bolts strike enemies.  Maximum of 1 bolt per target.',
    prerequisites=(lightning_strike_1,)
)

lightning_strike_3 = Ability(
    name='Lightning Strike III', picture=AbilityPicture.thunder_2,
    mp_cost=14, attacks=1, mdam='1d12+2*WIS',
    damage_type=DamageType.lightning, targets_mdef=True, time=Time.std_ab_a,
    shape=Shape.multi_point, max_range='12', target_area='One creature per bolt',
    effect='[[3+WIS]] lightning bolts strike enemies.  Maximum of 1 bolt per target.',
    prerequisites=(lightning_strike_2,)
)

deep_freeze_1 = Ability(
    name='Deep Freeze I', picture=AbilityPicture.blizzard_2,
    mp_cost=2, attacks=1, mdam='1d10',
    damage_type=DamageType.cold, targets_mdef=True, time=Time.std_ab_a,
    shape=Shape.multi_point, max_range='5', target_area='One living creature',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Slows enemy -[[WIS]]SPEED',
    prerequisites=(ice_wall_2, ice_slick_3)
)

deep_freeze_2 = Ability(
    name='Deep Freeze II', picture=AbilityPicture.blizzard_2,
    mp_cost=6, attacks=1, mdam='1d12+WIS',
    damage_type=DamageType.cold, targets_mdef=True, time=Time.std_ab_a,
    shape=Shape.multi_point, max_range='5', target_area='One living creature',
    duration='5', duration_unit=DurationUnit.rnd,
    effect='Immobilizes for 1 RND and slows enemy -[[WIS]]SPEED for Duration',
    prerequisites=(deep_freeze_1,)
)

deep_freeze_3 = Ability(
    name='Deep Freeze III', picture=AbilityPicture.blizzard_2,
    mp_cost=10, attacks=1, mdam='1d12+2*WIS',
    damage_type=DamageType.cold, targets_mdef=True, time=Time.std_ab_a,
    shape=Shape.multi_point, max_range='7', target_area='One living creature',
    duration='5', duration_unit=DurationUnit.rnd,
    effect='Stuns for 1 RND and slows enemy -[[WIS]]SPEED for Duration',
    prerequisites=(deep_freeze_2,)
)

infuse_1 = Ability(
    name='Infuse I', picture=AbilityPicture.mana_wall,
    mp_cost=4, max_range='1', target_area='1 ally', time=Time.free_a,
    effect='Adds [[4+WIS]]MP to ally',
    prerequisites=(fireball_2, ice_wall_2, lightning_shield_2)
)

infuse_2 = Ability(
    name='Infuse II', picture=AbilityPicture.mana_wall,
    mp_cost=8, max_range='5', target_area='1 ally', time=Time.free_a,
    effect='Adds [[9+WIS]]MP to ally',
    prerequisites=(infuse_1,)
)

infuse_3 = Ability(
    name='Infuse III', picture=AbilityPicture.mana_wall,
    mp_cost=12, max_range='9', target_area='1 ally', time=Time.free_a,
    effect='Adds [[14+2*WIS]]MP to ally',
    prerequisites=(infuse_2,)
)

# Tier 3.
fire_storm_1 = Ability(
    name='Fire Storm I', picture=AbilityPicture.fire_3,
    mp_cost=10, attacks=1, mdam='4d8',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.full_a,
    max_range='9', shape=Shape.circle, target_area='4RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Fiery storm engulfs the area.  Must continue to cast for at least Duration.',
    prerequisites=(inferno_3, sunray_2, infuse_2)
)

fire_storm_2 = Ability(
    name='Fire Storm II', picture=AbilityPicture.fire_3,
    mp_cost=12, attacks=1, mdam='4d10+2*WIS',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.full_a,
    max_range='12', shape=Shape.circle, target_area='4RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Fiery storm engulfs the area.  Must continue to cast for at least Duration.',
    prerequisites=(fire_storm_1,)
)

fire_storm_3 = Ability(
    name='Fire Storm III', picture=AbilityPicture.fire_3,
    mp_cost=14, attacks=1, mdam='4d12+4*WIS',
    damage_type=DamageType.fire, targets_mdef=True, time=Time.full_a,
    max_range='12', shape=Shape.circle, target_area='[[4+WIS]]RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Fiery storm engulfs the area.  Must continue to cast for at least Duration.',
    prerequisites=(fire_storm_2,)
)

thunder_cloud_1 = Ability(
    name='Thunder Cloud I', picture=AbilityPicture.thunder_3,
    mp_cost=10, attacks=1, mdam='1d6+WIS',
    damage_type=DamageType.lightning, targets_mdef=True, time=Time.full_a,
    shape=Shape.circle, target_area='Allies and targets with 8RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Allies gain MDAM to successful and unsuccessful physical attacks, all allies gain '
           'Lightning Shield I.  Must continue cast for at least Duration.',
    prerequisites=(lightning_strike_3, sunray_2, infuse_2)
)

thunder_cloud_2 = Ability(
    name='Thunder Cloud II', picture=AbilityPicture.thunder_3,
    mp_cost=12, attacks=1, mdam='1d8+WIS',
    damage_type=DamageType.lightning, targets_mdef=True, time=Time.full_a,
    shape=Shape.circle, target_area='Allies and targets with [[8+WIS]]RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Allies gain MDAM to successful and unsuccessful physical attacks, all allies gain '
           'Lightning Shield II, 1 bolt of Lightning Strike per enemy in range. '
           'Must continue cast for at least Duration.',
    prerequisites=(thunder_cloud_1,)
)

thunder_cloud_3 = Ability(
    name='Thunder Cloud III', picture=AbilityPicture.thunder_3,
    mp_cost=14, attacks=1, mdam='2d8+WIS',
    damage_type=DamageType.lightning, targets_mdef=True, time=Time.full_a,
    shape=Shape.circle, target_area='Allies and targets with [[12+WIS]]RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Allies gain MDAM to successful and unsuccessful physical attacks, all allies gain '
           'Lightning Shield III, 1 bolt of Lightning Strike per enemy in range. '
           'Must continue to cast for at least Duration.',
    prerequisites=(thunder_cloud_2,)
)

ice_wind_1 = Ability(
    name='Ice Wind I', picture=AbilityPicture.blizzard_3,
    mp_cost=6, attacks=1, mdam='1d6+WIS',
    damage_type=DamageType.cold, targets_mdef=True, time=Time.full_a, max_range='4',
    shape=Shape.cone, target_area='4DIS cone',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Slows enemy -[[2+WIS]]SPEED, adds +[[WIS]]PRED to allies.  Must continue to cast '
           'for at least Duration.',
    prerequisites=(lightning_strike_2, deep_freeze_3, infuse_1)
)

ice_wind_2 = Ability(
    name='Ice Wind II', picture=AbilityPicture.blizzard_3,
    mp_cost=7, attacks=1, mdam='1d8+WIS',
    damage_type=DamageType.cold, targets_mdef=True, time=Time.full_a, max_range='6',
    shape=Shape.cone, target_area='6DIS cone',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Slows enemy -[[4+WIS]]SPEED, adds +[[WIS]]PRED to allies.  Must continue to cast '
           'for at least Duration.',
    prerequisites=(ice_wind_1,)
)

ice_wind_3 = Ability(
    name='Ice Wind III', picture=AbilityPicture.blizzard_3,
    mp_cost=8, attacks=1, mdam='1d12+2*WIS',
    damage_type=DamageType.cold, targets_mdef=True, time=Time.full_a, max_range='6',
    shape=Shape.cone, target_area='6DIS cone',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Slows enemy -[[4+WIS]]SPEED, adds +[[WIS]]PRED to allies.  Must continue to cast '
           'for at least Duration.',
    prerequisites=(ice_wind_1,)
)

arcane_master_1 = Ability(
    name='Arcane Master I', picture=AbilityPicture.divine_seal,
    mp_cost=0, target_area='Self',
    effect='[Passive] +3RND Duration on ice abilities',
    prerequisites=(inferno_3, lightning_shield_3, deep_freeze_3)
)

arcane_master_2 = Ability(
    name='Arcane Master II', picture=AbilityPicture.divine_seal,
    mp_cost=0, target_area='Self',
    effect='[Passive] +5Range on lightning abilities',
    prerequisites=(arcane_master_1,)
)

arcane_master_3 = Ability(
    name='Arcane Master III', picture=AbilityPicture.divine_seal,
    mp_cost=0, target_area='Self',
    effect='[Passive] +1DIS on fire abilities',
    prerequisites=(arcane_master_2,)
)

fury_1 = Ability(
    name='Fury I', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=6, target_area='Self', time=Time.free_a,
    duration='3', duration_unit=DurationUnit.rnd,
    effect='-[[WIS]]HP per RND on caster.  +1AbA per RND. Must cast for at least Duration.',
    prerequisites=(inferno_2, lightning_strike_2, infuse_3)
)

fury_2 = Ability(
    name='Fury II', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=10, target_area='Self', time=Time.free_a,
    duration='4', duration_unit=DurationUnit.rnd,
    effect='-[[WIS+1]]HP per RND on caster. +1AbA +1StdA per RND. +[[WIS]]RAD to abilities. '
           'Must cast for at least Duration.',
    prerequisites=(fury_1,)
)

fury_3 = Ability(
    name='Fury III', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=14, target_area='Self', time=Time.free_a,
    duration='4', duration_unit=DurationUnit.rnd,
    effect='-[[WIS+2]]HP per RND on caster. +2AbA +1StdA per RND. +[[WIS]]RAD to abilities. '
           '+[[WIS]]Range to abilities. Must cast for at least Duration.',
    prerequisites=(fury_2,)
)


class Magus(Class):
    def __init__(self) -> None:
        super().__init__(
            name=self.__class__.__name__, hd=6, md=6, sd=2, speed=3, pdef=4, mdef=1,
            pred=0, mred=1, reg=1.25, vis=2, pac=0.5, mac=1, ath=1, ste=2, fort=1, apt=4,
            per=4, spe=2, starting_ap=5, use_melee_light=True,
            use_magic_light=True, use_magic_medium=True, use_magic_heavy=True,
            use_light_armor=True,
            abilities=(fireball_1, fireball_2, fireball_3,
                       lightning_shield_1, lightning_shield_2, lightning_shield_3,
                       ice_wall_1, ice_wall_2, ice_wall_3,
                       ice_slick_1, ice_slick_2, ice_slick_3,
                       imbue_weapon_1, imbue_weapon_2, imbue_weapon_3,
                       inferno_1, inferno_2, inferno_3,
                       sunray_1, sunray_2, sunray_3,
                       lightning_strike_1, lightning_strike_2, lightning_strike_3,
                       deep_freeze_1, deep_freeze_2, deep_freeze_3,
                       infuse_1, infuse_2, infuse_3,
                       fire_storm_1, fire_storm_2, fire_storm_3,
                       thunder_cloud_1, thunder_cloud_2, thunder_cloud_3,
                       ice_wind_1, ice_wind_2, ice_wind_3,
                       arcane_master_1, arcane_master_2, arcane_master_3,
                       fury_1, fury_2, fury_3))
