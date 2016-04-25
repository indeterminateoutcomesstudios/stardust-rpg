#!/usr/bin/env python3

import enum

import aenum
from typing import Tuple

from .equipment import DamageType, Shape


@enum.unique
class AbilityPictures(enum.Enum):
    # TODO: Enumerate
    pass


class DurationUnit(aenum.AutoNumberEnum):
    instant = ()
    rnd = ()
    min = ()
    hour = ()
    day = ()
    forever = ()


class Time(aenum.AutoNumberEnum):
    free_a = ()
    ab_a = ()
    std_a = ()
    full_a = ()
    std_ab_a = ()


class Ability:
    def __init__(self, name: str, mp_cost: int, target_area: str, duration: str=None,
                 duration_unit: DurationUnit=DurationUnit.instant,
                 prerequisites: Tuple['Ability', ...]=(), damage_type: DamageType=None, effect='',
                 attacks: int=0, pdam: str=None, mdam: str=None,
                 targets_mdef: bool=False, time: Time=Time.ab_a, min_range: int=0,
                 max_range: int=0, shape: Shape=Shape.point):
        self.name = name
        self.damage_type = damage_type
        self.mp_cost = mp_cost
        self.prerequisites = prerequisites
        self.target_area = target_area
        self.duration = duration
        self.duration_unit = duration_unit
        self.effect = effect
        self.attacks = attacks
        # TODO: Validate pdam/mdam formulas?
        self.pdam = pdam
        self.mdam = mdam
        self.targets_mdef = targets_mdef
        self.time = time
        self.min_range = min_range
        self.max_range = max_range
        self.shape = shape
