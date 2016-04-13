#!/usr/bin/env python3

import autoenum
from frozendict import frozendict
from typing import Dict  # noqa


class Classes(autoenum.AutoEnum):
    empty = ()


class Class:
    def __init__(self, name: str='Empty Class', hd: int=0, md: int=0, sd: int=0, speed: int=0,
                 pdef: int=0, mdef: float=0.0, pred: float=0.0, mred: float=0.0,
                 reg: float=0.0, vis: int=0, pac: float=0.0, mac: float=0.0,
                 ath: int=0, ste: int=0, fort: int=0, apt: int=0, per: int=0, spe: int=0,
                 starting_ap: int=0,
                 use_melee_light: bool=False, use_melee_medium: bool=False,
                 use_melee_heavy: bool=False, use_ranged_light: bool=False,
                 use_ranged_medium: bool=False, use_ranged_heavy: bool=False,
                 use_magic_light: bool=False, use_magic_medium: bool=False,
                 use_magic_heavy: bool=False, use_light_armor: bool=False,
                 use_medium_armor: bool=False, use_heavy_armor: bool=False):
        self.name = name
        self.hd = hd
        self.md = md
        self.sd = sd
        self.speed = speed
        self.pdef = pdef
        self.mdef = mdef
        self.pred = pred
        self.mred = mred
        self.reg = reg
        self.vis = vis
        self.pac = pac
        self.mac = mac
        self.ath = ath
        self.ste = ste
        self.fort = fort
        self.apt = apt
        self.per = per
        self.spe = spe
        self.starting_ap = starting_ap
        self.use_melee_light = use_melee_light
        self.use_melee_medium = use_melee_medium
        self.use_melee_heavy = use_melee_heavy
        self.use_ranged_light = use_ranged_light
        self.use_ranged_medium = use_ranged_medium
        self.use_ranged_heavy = use_ranged_heavy
        self.use_magic_light = use_magic_light
        self.use_magic_medium = use_magic_medium
        self.use_magic_heavy = use_magic_heavy
        self.use_light_armor = use_light_armor
        self.use_medium_armor = use_medium_armor
        self.use_heavy_armor = use_heavy_armor


class_map = frozendict(
    {Classes.empty: Class()}
)  # type: Dict[Classes, Class]

