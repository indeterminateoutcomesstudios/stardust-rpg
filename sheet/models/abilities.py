#!/usr/bin/env python3


import aenum

from .classes import paladin


class Abilities(aenum.AutoNumberEnum):
    reflect_1 = ()
    reflect_2 = ()
    reflect_3 = ()
    telekinesis_1 = ()
    telekinesis_2 = ()
    telekinesis_3 = ()
    protect_1 = ()
    protect_2 = ()
    protect_3 = ()
    shell_1 = ()
    shell_2 = ()
    shell_3 = ()

abilities = {
    Abilities.reflect_1: paladin.reflect_1,
    Abilities.reflect_2: paladin.reflect_2,
    Abilities.reflect_3: paladin.reflect_3,
    Abilities.telekinesis_1: paladin.telekinesis_1,
    Abilities.telekinesis_2: paladin.telekinesis_2,
    Abilities.telekinesis_3: paladin.telekinesis_3,
    Abilities.protect_1: paladin.protect_1,
    Abilities.protect_2: paladin.protect_2,
    Abilities.protect_3: paladin.protect_3,
    Abilities.shell_1: paladin.shell_1,
    Abilities.shell_2: paladin.shell_2,
    Abilities.shell_3: paladin.shell_3,
}


inverse_abilities = {ability: enum for enum, ability in abilities.items()}
"""Maps abilities to their corresponding enums."""
