from ..class_type import Class


class Templar(Class):
    def __init__(self):
        super().__init__(
            name=self.__class__.__name__, hd=10, md=6, sd=4, speed=5, pdef=5, mdef=1,
            pred=0, mred=0, reg=1, vis=2, pac=0.5, mac=0.75, ath=2, ste=4, fort=2, apt=2,
            per=1, spe=4, starting_ap=4, use_melee_light=True, use_melee_medium=True,
            use_ranged_light=True, use_magic_light=True, use_magic_medium=True,
            use_light_armor=True, use_medium_armor=True,
            abilities=())
