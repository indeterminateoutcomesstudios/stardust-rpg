#!/usr/bin/env python3

import enum
import itertools

_enum_value = itertools.count(1)


@enum.unique
class Slot(enum.Enum):
    item = next(_enum_value)
    utility = next(_enum_value)
    weapon = next(_enum_value)
    head = next(_enum_value)
    neck = next(_enum_value)
    chest = next(_enum_value)
    shield = next(_enum_value)
    hand = next(_enum_value)
    feet = next(_enum_value)

_enum_value = itertools.count(1)


@enum.unique
class Rarity(enum.Enum):
    common = next(_enum_value)
    rare = next(_enum_value)
    unique = next(_enum_value)
    set = next(_enum_value)

_enum_value = itertools.count(1)


@enum.unique
class Style(enum.Enum):
    melee = next(_enum_value)
    ranged = next(_enum_value)
    magic = next(_enum_value)

_enum_value = itertools.count(1)


@enum.unique
class Type(enum.Enum):
    light = next(_enum_value)
    medium = next(_enum_value)
    heavy = next(_enum_value)


class Equipment:
    def __init__(self, slot: Slot, name: str, rarity: Rarity, price: int, effect: str):
        self.slot = slot
        self.name = name
        self.rarity = rarity
        self.price = price
        self.effect = effect


class Wearable(Equipment):
    pass
