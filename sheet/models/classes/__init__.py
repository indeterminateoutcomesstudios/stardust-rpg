import aenum

from . import geomancer, magus, marksman, paladin, spectre, telepath, templar, valkyrie
from .. import class_type


class Classes(aenum.AutoNumberEnum):
    paladin = ()
    templar = ()
    magus = ()
    valkyrie = ()
    spectre = ()
    telepath = ()
    marksman = ()
    geomancer = ()


classes = {
    Classes.paladin: paladin.Paladin(),
    Classes.templar: templar.Templar(),
    Classes.magus: magus.Magus(),
    Classes.valkyrie: valkyrie.Valkyrie(),
    Classes.spectre: spectre.Spectre(),
    Classes.telepath: telepath.Telepath(),
    Classes.marksman: marksman.Marksman(),
    Classes.geomancer: geomancer.Geomancer(),
}


def get_class(name: str) -> class_type.Class:
    for cls in classes.values():
        if name == cls.name:
            return cls
    raise KeyError("Unable to find class '{}', invalid name.".format(name))
