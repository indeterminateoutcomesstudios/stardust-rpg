from ..class_type import Class


class Magus(Class):
    def __init__(self):
        super().__init__(
            name=self.__class__.__name__, hd=6, md=6, sd=2, speed=3, pdef=4, mdef=1,
            pred=0, mred=1, reg=1.25, vis=2, pac=0.5, mac=1, ath=1, ste=2, fort=1, apt=4,
            per=4, spe=2, starting_ap=5, use_melee_light=True,
            use_magic_light=True, use_magic_medium=True, use_magic_heavy=True,
            use_light_armor=True,
            abilities=())
