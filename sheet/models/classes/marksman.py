from ..class_type import Class


class Marksman(Class):
    def __init__(self):
        super().__init__(
            name=self.__class__.__name__, hd=8, md=4, sd=4, speed=4, pdef=4, mdef=0.25,
            pred=0, mred=0, reg=1, vis=3, pac=1, mac=0.75, ath=4, ste=2, fort=1, apt=4,
            per=1, spe=2, starting_ap=4,
            use_ranged_light=True, use_ranged_medium=True, use_ranged_heavy=True,
            use_light_armor=True, use_medium_armor=True,
            abilities=())
