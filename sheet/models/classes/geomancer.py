from ..class_type import Class


class Geomancer(Class):
    def __init__(self):
        super().__init__(
            name=self.__class__.__name__, hd=20, md=4, sd=2, speed=3, pdef=3, mdef=0.5,
            pred=0.5, mred=0.5, reg=0.75, vis=4, pac=1, mac=0.5, ath=4, ste=1, fort=5, apt=1,
            per=2, spe=2, starting_ap=4,
            use_melee_heavy=True,
            use_light_armor=True, use_medium_armor=True, use_heavy_armor=True,
            abilities=())
