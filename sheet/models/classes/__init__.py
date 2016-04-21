#!/usr/bin/env python3

import aenum

from .paladin import Paladin
from ..class_type import Class


class Classes(aenum.AutoNumberEnum):
    empty = ()
    paladin = ()

classes = {
    Classes.empty: Class(),
    Classes.paladin: Paladin(),
}
