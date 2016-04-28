#!/usr/bin/env python3

import enum

import aenum
from typing import Tuple

from .equipment import DamageType, Shape
from . import macro


@enum.unique
class AbilityPictures(enum.Enum):
    # TODO: Enumerate
    pass

# TODO: Shape pictures.


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
    mp_mac_modifier = 0.25

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

    def mac(self) -> int:
        return round(self.mp_cost * self.mp_mac_modifier)

    @property
    def macro(self) -> str:
        common_template = ('{template_tag}'
                           '{color}'
                           '{{{{title=**{ability_name}**}}}}'
                           '{{{{subheader= Ability}}}}'
                           '{{{{subheaderright={time}}}}}'
                           '{{{{subheader2={mp_cost}MP}}}}'
                           '{{{{emote=@{{Name}} casts at @{{target|Name}}}}}}'
                           '{{{{Range=[[{min_range}]]-[[{max_range}]]}}}}'
                           '{{{{Shape=[p]({shape_picture}) ({shape})}}}}'
                           '{{{{Area={area}}}}}'
                           '{{{{Duration={duration}}}}}'
                           '{{{{Effect=*{effect}*}}}}'
                           '{template_terminator}')

        if (self.duration_unit is DurationUnit.instant or
           self.duration_unit is DurationUnit.forever):
            duration_str = self.duration_unit.name
        else:
            duration_str = '[[{duration_value}]]{duration_unit}'.format(
                duration_value=self.duration, duration_unit=self.duration_unit.name.upper())

            if self.duration_unit is DurationUnit.rnd:
                duration_str += '(ends [[{duration_rnd}+@{{tracker|RND}}]])'.format(
                    duration_rnd=self.duration)

        macro_str = common_template.format(template_tag=macro.template_tag,
                                           color=macro.MacroColorTag.purple.value,
                                           ability_name=self.name,
                                           time=self.time.name,
                                           mp_cost=self.mp_cost,
                                           min_range=self.min_range,
                                           max_range=self.max_range,
                                           template_terminator=macro.template_terminator,
                                           shape_picture=self.shape.value,
                                           shape=self.shape.name,
                                           area=self.target_area,
                                           duration=duration_str,
                                           effect=self.effect)
        for i in range(self.attacks):
            attack_template = ('{template_tag}'
                               '{{{{title=Attack}}}}'
                               '{color}'
                               '{hit}'
                               '{pdam}'
                               '{mdam}'
                               '{template_terminator}')

            hit = ''
            if self.targets_mdef:
                hit = ('{{{{Hit=[[{{d20+@{{BMAC}}+{mp_mac_modifier}*{mp_cost}}}>'
                       '@{{target|MDEF}}]] vs MDEF}}}}'.format(
                            mp_mac_modifier=self.mp_mac_modifier,
                            mp_cost=self.mp_cost))

            damage_template = ('{{{{{damage_category}='
                               '[[round({dam}-@{{target|{reduction_type}}})'
                               '*(1+@{{target|{damage_type}VUL}})'
                               '/(1+@{{target|{damage_type}RES}})'
                               '*(1-@{{target|{damage_type}IMU}})'
                               ']]{damage_category} [{damage_type}]}}}}'
                               '{{{{{damage_type}='
                               'VUL:@{{target|{damage_type}VUL}} '
                               'RES:@{{target|{damage_type}RES}} '
                               'IMU:@{{target|{damage_type}IMU}}'
                               '}}}}')

            pdam = ''
            if self.pdam is not None:
                pdam = damage_template.format(damage_category='PDAM',
                                              dam=self.pdam,
                                              reduction_type='PRED',
                                              damage_type=self.damage_type.cap_name)

            mdam = ''
            if self.mdam is not None:
                mdam = damage_template.format(damage_category='MDAM',
                                              dam=self.mdam,
                                              reduction_type='MRED',
                                              damage_type=self.damage_type.cap_name)

            macro_str += '\n' + attack_template.format(
                template_tag=macro.template_tag,
                color=macro.MacroColorTag.purple.value,
                template_terminator=macro.template_terminator,
                hit=hit,
                pdam=pdam,
                mdam=mdam)

        return macro.escape_attributes(macro_str)
