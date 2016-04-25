#!/usr/bin/env python3

from ..ability import Ability, DurationUnit, Time
from ..class_type import Class
from ..equipment import DamageType, Shape

reflect_1 = Ability(
    name='Reflect [Counter] I', mp_cost=2, target_area='Self', time=Time.free_a,
    effect='If hit with melee attack, can reflect 1PDAM'
)

reflect_2 = Ability(
    name='Reflect [Counter] II', mp_cost=3, target_area='Self', time=Time.free_a,
    effect='If hit with melee attack, can reflect [[1+WIS]]PDAM',
    prerequisites=(reflect_1,),
)

reflect_3 = Ability(
    name='Reflect [Counter] III', mp_cost=3, target_area='Self', time=Time.free_a,
    effect='If hit with magic attack, can reflect [[1+WIS]]MDAM',
    prerequisites=(reflect_2,),
)

telekinesis_1 = Ability(
    name='Telekinesis I', mp_cost=1, attacks=1, mdam='1d6',
    damage_type=DamageType.force, targets_mdef=True, max_range=8,
    target_area='Object < 20lb (Small)',
    effect='Can telekinetically interact/(move 4DIS) object (or self) doing MDAM if thrown '
           'against a surface'
)

telekinesis_2 = Ability(
    name='Telekinesis II', mp_cost=2, attacks=1, mdam='1d8 + WIS',
    damage_type=DamageType.force, targets_mdef=True, max_range=8,
    target_area='Object < 200lb (Medium)',
    effect='Can telekinetically interact/(move 6DIS) object (or self) doing MDAM if thrown '
           'against a surface',
    prerequisites=(telekinesis_1,),
)

telekinesis_3 = Ability(
    name='Telekinesis III', mp_cost=4, attacks=1, mdam='1d12 + 2*WIS',
    damage_type=DamageType.force, targets_mdef=True, max_range=8,
    target_area='Object < 800lb (Large)',
    effect='Can telekinetically interact/(move 8DIS) object (or self) doing MDAM if thrown '
           'against a surface',
    prerequisites=(telekinesis_2,),
)

protect_1 = Ability(
    name='Protect I', mp_cost=2, max_range=1, target_area='One ally',
    duration='1+WIS', duration_unit=DurationUnit.rnd,
    effect='+1PDEF Caster. Target gets caster PDEF. +1PRED. Take ½ DAM for protected target. '
           '-2SPEED.  Can end early.'
)

protect_2 = Ability(
    name='Protect II', mp_cost=3, max_range=1, target_area='One ally',
    duration='1+WIS', duration_unit=DurationUnit.rnd,
    effect='+2PDEF, Take 3/4 DAM for protected target. Can stop at any time.  Can end early.',
    prerequisites=(protect_1,),
)

protect_3 = Ability(
    name='Protect III', mp_cost=4, max_range=1, target_area='One ally',
    duration='1+WIS', duration_unit=DurationUnit.rnd,
    effect='+[[3+WIS]]PDEF, Take All DAM for protected target.  Can end early.',
    prerequisites=(protect_2,),
)

shell_1 = Ability(
    name='Shell I', mp_cost=5, time=Time.full_a, shape=Shape.circle,
    target_area='Up to [[4+WIS]]RAD',
    duration='1+WIS', duration_unit=DurationUnit.rnd,
    effect='Protective spherical shield blocks abilities/projectiles/objects. '
           '+1 MRED to magic attacks that passes through. '
           '25% chance inanimate projectiles to reflect off. Enemies cannot pass through',
    prerequisites=(reflect_2,),
)

shell_2 = Ability(
    name='Shell II', mp_cost=7, time=Time.full_a, shape=Shape.circle,
    target_area='Up to [[4+(2*WIS)]]RAD',
    duration='2+WIS', duration_unit=DurationUnit.rnd,
    effect='Protective spherical shield blocks abilities/projectiles/objects. '
           '+[[2+WIS]] MRED to magic attacks that passes through. '
           '50% chance inanimate projectiles to reflect off. Enemies cannot pass through',
    prerequisites=(shell_1,),
)

shell_3 = Ability(
    name='Shell III', mp_cost=9, time=Time.full_a, shape=Shape.circle,
    target_area='Up to [[4+(2*WIS)]]RAD',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Protective spherical shield blocks abilities/projectiles/objects. '
           '+[[3+2*WIS]] MRED to magic attacks that passes through. '
           '75% chance inanimate projectiles to reflect off. Enemies cannot pass through',
    prerequisites=(shell_2,),
)


class Paladin(Class):
    def __init__(self):
        super().__init__(
            name=self.__class__.__name__, hd=12, md=4, sd=2, speed=4, pdef=6, mdef=0.75,
            pred=1, mred=0, reg=0.75, vis=2, pac=1, mac=0.5, ath=4, ste=1, fort=4, apt=1,
            per=2, spe=2, starting_ap=4, use_melee_light=True, use_melee_medium=True,
            use_melee_heavy=True, use_light_armor=True, use_medium_armor=True,
            use_heavy_armor=True,
            abilities=(reflect_1, reflect_2, reflect_3, telekinesis_1, telekinesis_2,
                       telekinesis_3, protect_1, protect_2, protect_3, shell_1, shell_2,
                       shell_3))
