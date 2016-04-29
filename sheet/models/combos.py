#!/usr/bin/env python3

from typing import Tuple


from .ability import Ability, AbilityPicture, DurationUnit, Time
from .class_type import Class
from .classes.paladin import Paladin
from .equipment import DamageType, Shape


class Combo(Ability):
    def __init__(self, classes: Tuple[Class, Class], prerequisite_lvl: int,
                 name: str, picture: AbilityPicture, mp_cost: int, target_area: str,
                 duration: str = None, duration_unit: DurationUnit = DurationUnit.instant,
                 damage_type: DamageType = None,
                 effect='',
                 attacks: int = 0, pdam: str = None, mdam: str = None,
                 targets_mdef: bool = False, time: Time = Time.ab_a, min_range: int = 0,
                 max_range: int = 0, shape: Shape = Shape.point):
        self.classes = classes
        self.prerequisite_lvl = prerequisite_lvl
        super().__init__(name=name, picture=picture, mp_cost=mp_cost, target_area=target_area,
                         duration=duration, duration_unit=duration_unit, prerequisites=(),
                         damage_type=damage_type, effect=effect, attacks=attacks, pdam=pdam,
                         mdam=mdam, targets_mdef=targets_mdef, time=time, min_range=min_range,
                         max_range=max_range, shape=shape)


combos = (
    Combo(
        classes=(Paladin, Paladin), prerequisite_lvl=2,
        name='Temporal Shock Wave I', picture=AbilityPicture.benediction,
        mp_cost=4, attacks=1, mdam='d10 + WIS',
        damage_type=DamageType.force, targets_mdef=True, time=Time.full_a, min_range=1,
        max_range=1, shape=Shape.circle, target_area='[[1+WIS]]RAD',
        duration_unit=DurationUnit.instant,
        effect='Removes status effects from allies and heals [[d4+WIS]]HP. '
               'Knockback enemies [[WIS]]DIS.'
    ),
    Combo(
        classes=(Paladin, Paladin), prerequisite_lvl=5,
        name='Temporal Shock Wave II', picture=AbilityPicture.benediction,
        mp_cost=7, attacks=1, mdam='2d12 + WIS',
        damage_type=DamageType.force, targets_mdef=True, time=Time.full_a, min_range=1,
        max_range=1, shape=Shape.circle, target_area='[[2+WIS]]RAD',
        duration_unit=DurationUnit.instant,
        effect='Removes status effects from allies and heals [[2d10+WIS]]HP. '
               'Knockback enemies [[1+WIS]]DIS.'
    ),
    Combo(
        classes=(Paladin, Paladin), prerequisite_lvl=8,
        name='Temporal Shock Wave III', picture=AbilityPicture.benediction,
        mp_cost=12, attacks=1, mdam='4d12 + 2*WIS',
        damage_type=DamageType.force, targets_mdef=True, time=Time.full_a, min_range=1,
        max_range=1, shape=Shape.circle, target_area='[[4+WIS]]RAD',
        duration_unit=DurationUnit.instant,
        effect='Removes status effects from allies and heals [[3d10+2*WIS]]HP. '
               'Knockback enemies  [[3+WIS]]DIS.'
    ),
)
