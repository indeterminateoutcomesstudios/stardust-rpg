#!/usr/bin/env python3

import re
from typing import Tuple


class Dice:
    def __init__(self, sides: int, num_dice: int=1):
        self.sides = sides
        self.num_dice = num_dice

    @classmethod
    def from_str(cls, string: str) -> 'Dice':
        # Examples: d4 2d10 d20 10d20
        match = re.fullmatch(r'^(?P<num_dice>\d*)d(?P<sides>\d+)?', string)

        if match is not None:
            sides = int(match.group('sides'))
            num_dice = match.group('num_dice')
            if num_dice != '':
                return cls(sides=sides, num_dice=int(num_dice))
            else:
                return cls(sides=sides)

    def __str__(self) -> str:
        if self.num_dice > 1:
            num_dice_char = str(self.num_dice)
        else:
            num_dice_char = ''
        return '{}d{}'.format(num_dice_char, self.sides)


class DiceFormula:
    def __init__(self, dice_pool: Tuple[Dice, ...], modifier: int=0):
        self.dice_pool = dice_pool
        self.modifier = modifier

    def __str__(self) -> str:
        s = ''
        for dice in self.dice_pool:
            s += '{} + '.format(dice)

        if self.modifier > 0:
            s += str(self.modifier)
        else:
            s = s[:-len(' + ')]

        return s
