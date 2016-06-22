import aenum

from . import geomancer, magus, marksman, paladin, spectre, telepath, templar, valkyrie


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
