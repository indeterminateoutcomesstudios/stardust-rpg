#!/usr/bin/env python3

"""Temporary module to store items until database solution is created."""

import aenum
from frozendict import frozendict

from . import equipment


class Utilities(aenum.AutoNumberEnum):
    empty = ()

utilities = frozendict(
    {Utilities.empty: equipment.Wearable(slot=equipment.Slot.utility, name='Empty Utility')}
)


class Heads(aenum.AutoNumberEnum):
    empty = ()

heads = frozendict(
    {Heads.empty: equipment.Wearable(slot=equipment.Slot.head, name='Empty Head')}
)


class Necks(aenum.AutoNumberEnum):
    empty = ()

necks = frozendict(
    {Necks.empty: equipment.Wearable(slot=equipment.Slot.neck, name='Empty Neck')}
)


class Chests(aenum.AutoNumberEnum):
    empty = ()

chests = frozendict(
    {Chests.empty: equipment.Wearable(slot=equipment.Slot.chest, name='Empty Chest')}
)


class Shields(aenum.AutoNumberEnum):
    empty = ()

shields = frozendict(
    {Shields.empty: equipment.Wearable(slot=equipment.Slot.shield, name='Empty Shield')}
)


class Hands(aenum.AutoNumberEnum):
    empty = ()

hands = frozendict(
    {Hands.empty: equipment.Hand(name='Empty Hand')}
)


class Feets(aenum.AutoNumberEnum):
    empty = ()

feets = frozendict(
    {Feets.empty: equipment.Wearable(slot=equipment.Slot.feet, name='Empty Feet')}
)


class Weapons(aenum.AutoNumberEnum):
    empty = ()

weapons = frozendict(
    {Weapons.empty: equipment.Weapon(name='Empty Weapon')}
)
