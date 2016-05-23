from ..class_type import Class


class Valkyrie(Class):
    def __init__(self):
        super().__init__(
            name=self.__class__.__name__, hd=10, md=6, sd=2, speed=5, pdef=6, mdef=1,
            pred=0, mred=0, reg=1, vis=3, pac=0.5, mac=0.75, ath=2, ste=2, fort=1, apt=1,
            per=4, spe=4, starting_ap=4, use_melee_light=True, use_melee_medium=True,
            use_ranged_light=True, use_ranged_medium=True, use_ranged_heavy=True,
            use_light_armor=True,
            abilities=())
