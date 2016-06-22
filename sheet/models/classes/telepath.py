from ..class_type import Class


class Telepath(Class):
    def __init__(self) -> None:
        super().__init__(
            name=self.__class__.__name__, hd=8, md=6, sd=4, speed=5, pdef=4, mdef=1.25,
            pred=0, mred=1, reg=0.75, vis=3, pac=0.75, mac=1, ath=2, ste=4, fort=1, apt=1,
            per=4, spe=4, starting_ap=4, use_melee_light=True,
            use_ranged_light=True, use_ranged_medium=True, use_ranged_heavy=True,
            use_magic_light=True, use_magic_medium=True, use_magic_heavy=True,
            use_light_armor=True,
            abilities=())
