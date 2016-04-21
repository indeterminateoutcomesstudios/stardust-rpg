#!/usr/bin/env python3

from ..ability import Ability, Time
from ..class_type import Class

reflect_1 = Ability(
    name='Reflect [Counter] I', mp_cost=2, target_area='Self', time=Time.free_a,
    effect='If hit with melee attack, can reflect 1PDAM')

reflect_2 = Ability(
    name='Reflect [Counter] II', mp_cost=3, target_area='Self', time=Time.free_a,
    effect='If hit with melee attack, can reflect [[1+WIS]]PDAM')

reflect_3 = Ability(
    name='Reflect [Counter] III', mp_cost=3, target_area='Self', time=Time.free_a,
    effect='If hit with magic attack, can reflect [[1+WIS]]MDAM')


class Paladin(Class):
    def __init__(self):
        super().__init__(
            name=self.__class__.__name__, hd=12, md=4, sd=2, speed=4, pdef=6, mdef=0.75,
            pred=1, mred=0, reg=0.75, vis=2, pac=1, mac=0.5, ath=4, ste=1, fort=4, apt=1,
            per=2, spe=2, starting_ap=4, use_melee_light=True, use_melee_medium=True,
            use_melee_heavy=True, use_light_armor=True, use_medium_armor=True,
            use_heavy_armor=True,
            abilities=(reflect_1, reflect_2, reflect_3))
