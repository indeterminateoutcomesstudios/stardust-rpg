#!/usr/bin/env python3

import aenum


from . import paladin
from .. import class_type


class Classes(aenum.AutoNumberEnum):
    empty = ()
    paladin = ()

classes = {
    Classes.empty: class_type.Class(),
    Classes.paladin: paladin.Paladin(),
}
