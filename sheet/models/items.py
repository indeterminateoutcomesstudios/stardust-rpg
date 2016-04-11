#!/usr/bin/env python3

"""Temporary module to store items until database solution is created."""

import autoenum
from frozendict import frozendict

from . import equipment


class Utilities(autoenum.AutoEnum):
    empty = ()

utilities = frozendict(
    {Utilities.empty: equipment.Wearable(slot=equipment.Slot.utility, name='Empty Utility')}
)


class Heads(autoenum.AutoEnum):
    empty = ()

heads = frozendict(
    {Heads.empty: equipment.Wearable(slot=equipment.Slot.head, name='Empty Head')}
)


class Necks(autoenum.AutoEnum):
    empty = ()

necks = frozendict(
    {Necks.empty: equipment.Wearable(slot=equipment.Slot.neck, name='Empty Neck')}
)


class Chests(autoenum.AutoEnum):
    empty = ()

chests = frozendict(
    {Chests.empty: equipment.Wearable(slot=equipment.Slot.chest, name='Empty Chest')}
)


class Shields(autoenum.AutoEnum):
    empty = ()

shields = frozendict(
    {Shields.empty: equipment.Wearable(slot=equipment.Slot.shield, name='Empty Shield')}
)


class Hands(autoenum.AutoEnum):
    empty = ()

hands = frozendict(
    {Hands.empty: equipment.Hand(name='Empty Hand')}
)


class Feets(autoenum.AutoEnum):
    empty = ()

feets = frozendict(
    {Feets.empty: equipment.Wearable(slot=equipment.Slot.feet, name='Empty Feet')}
)


class Weapons(autoenum.AutoEnum):
    empty = ()

weapons = frozendict(
    {Weapons.empty: equipment.Weapon(name='Empty Weapon')}
)
