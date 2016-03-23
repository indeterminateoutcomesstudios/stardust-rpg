#!/usr/bin/env python3


class Class:
    def __init__(self, name: str='', hd: int=0, md: int=0, sd: int=0, speed: int=0,
                 pdef: int=0, mdef: float=0.0, pred: float=0.0, mred: float=0.0,
                 reg: float=0.0, vis: int=0, pac: float=0.0, mac: float=0.0,
                 ath: int=0, ste: int=0, fort: int=0, apt: int=0, per: int=0, spe: int=0,
                 starting_abilities: int=0,
                 use_melee_light: bool=False, use_melee_medium: bool=False,
                 use_melee_heavy: bool=False, use_ranged_light: bool=False,
                 use_ranged_medium: bool=False, use_ranged_heavy: bool=False,
                 use_magic_light: bool=False, use_magic_medium: bool=False,
                 use_magic_heavy: bool=False, use_light_armor: bool=False,
                 use_medium_armor: bool=False, use_heavy_armor: bool=False):
        self.name = name
        self.hd = hd
        self.md = md
        self.sd = sd
        self.speed = speed
        self.pdef = pdef
        self.mdef = mdef
        self.pred = pred
        self.mred = mred
        self.reg = reg
        self.vis = vis
        self.pac = pac
        self.mac = mac
        self.ath = ath
        self.ste = ste
        self.fort = fort
        self.apt = apt
        self.per = per
        self.spe = spe
        self.starting_abilities = starting_abilities
        self.use_melee_light = use_melee_light
        self.use_melee_medium = use_melee_medium
        self.use_melee_heavy = use_melee_heavy
        self.use_ranged_light = use_ranged_light
        self.use_ranged_medium = use_ranged_medium
        self.use_ranged_heavy = use_ranged_heavy
        self.use_magic_light = use_magic_light
        self.use_magic_medium = use_magic_medium
        self.use_magic_heavy = use_magic_heavy
        self.use_light_armor = use_light_armor
        self.use_medium_armor = use_medium_armor
        self.use_heavy_armor = use_heavy_armor


class Character:
    atp_lvl_mod = 2
    ap_lvl_mod = 2
    hp_lvl_con_mod = 1.5
    mp_lvl_int_mod = 1
    sp_lvl_int_mod = 1
    pred_con_mod = 0.5
    mred_int_mod = 0.5
    starting_reg = 18
    speed_dex_mod = 0.5
    vis_con_mod = 0.5
    bpac_lvl_str_mod = 1
    bmac_lvl_cha_mod = 1

    def __init__(self, cls: Class=Class(), lvl: int=0,
                 stren: int=0, dex: int=0, con: int=0, intel: int=0, wis: int=0, cha: int=0,
                 starting_ap: int=0):
        self.cls = cls
        self.lvl = lvl
        self.str = stren
        self.dex = dex
        self.con = con
        self.int = intel
        self.wis = wis
        self.cha = cha
        self.starting_ap = starting_ap

    @property
    def max_atp(self) -> int:
        return self.lvl * self.atp_lvl_mod

    @property
    def ap(self) -> int:
        return self.starting_ap + (self.ap_lvl_mod * self.lvl) + self.wis + self.cha

    @property
    def hp(self) -> int:
        return round(self.lvl * self.hp_lvl_con_mod * self.con)

    @property
    def mp(self) -> int:
        return self.lvl * self.mp_lvl_int_mod * self.int

    @property
    def max_sp(self) -> int:
        return self.lvl * self.sp_lvl_int_mod * self.int

    @property
    def pdef(self) -> int:
        return self.cls.pdef + self.dex

    @property
    def mdef(self) -> int:
        return round(self.cls.mdef * self.lvl)

    @property
    def pred(self) -> int:
        return round(self.cls.pred + (self.pred_con_mod * self.con))

    @property
    def mred(self) -> int:
        return round(self.cls.mred + (self.mred_int_mod * self.int))

    @property
    def reg(self) -> int:
        return round(self.starting_reg - (self.cls.reg * self.lvl) - self.cha)

    @property
    def rd(self) -> str:
        if self.lvl <= 3:
            return 'd2'
        elif 4 <= self.lvl <= 6:
            return 'd4'
        elif 7 <= self.lvl <= 9:
            return 'd6'
        elif 10 <= self.lvl <= 12:
            return 'd8'
        elif 13 <= self.lvl <= 15:
            return 'd10'
        else:
            return 'd12'

    @property
    def speed(self) -> int:
        return round(self.cls.speed + (self.speed_dex_mod * self.dex))

    @property
    def vis(self) -> int:
        return round(self.cls.vis + (self.vis_con_mod * self.con))

    @property
    def bpac(self) -> int:
        return round(self.cls.pac + (self.bpac_lvl_str_mod * self.str))

    @property
    def bmac(self) -> int:
        return round(self.cls.mac + (self.bmac_lvl_cha_mod * self.cha))
