from ..class_type import Class


class Spectre(Class):
    def __init__(self) -> None:
        super().__init__(
            name=self.__class__.__name__, hd=8, md=6, sd=4, speed=5, pdef=6, mdef=0.5,
            pred=0, mred=0, reg=0.5, vis=3, pac=0.75, mac=0.5, ath=4, ste=4, fort=1, apt=2,
            per=2, spe=1, starting_ap=5, use_melee_light=True, use_melee_medium=True,
            use_ranged_light=True, use_ranged_medium=True,
            use_light_armor=True, use_medium_armor=True,
            abilities=())
