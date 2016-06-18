import enum
from typing import Any

import aenum

from . import dice
from . import macro


def for_django_template(cls: Any) -> Any:
    """See http://stackoverflow.com/a/35953630/1398841."""
    cls.do_not_call_in_templates = True
    return cls


@enum.unique
class Attribute(enum.Enum):
    stren = 1
    dex = 2
    con = 3
    intel = 4
    wis = 5
    cha = 6


class Slot(aenum.AutoNumberEnum):
    item = ()
    utility = ()
    weapon = ()
    head = ()
    neck = ()
    chest = ()
    shield = ()
    hand = ()
    feet = ()


@for_django_template
class Rarity(aenum.AutoNumberEnum):
    common = ()
    rare = ()
    unique = ()
    set = ()


class Style(aenum.AutoNumberEnum):
    melee = ()
    ranged = ()
    magic = ()


class Type(aenum.AutoNumberEnum):
    light = ()
    medium = ()
    heavy = ()


@enum.unique
class Shape(enum.Enum):
    point = 'http://i.imgur.com/Snx8fr2.png'
    multi_point = 'http://i.imgur.com/IB4CXeb.png'
    line = 'http://i.imgur.com/CbqMJ3N.png'
    double_line = 'https://i.imgur.com/roFRLYp.png'
    dual_line = 'http://i.imgur.com/FEjIzJH.png'
    volatile_line = 'http://i.imgur.com/45eHyTK.png'
    overloaded_line = 'http://i.imgur.com/4H9ZLTK.png'
    circle = 'http://i.imgur.com/OgukZ2z.png'
    cluster = 'http://i.imgur.com/2oCm5ny.png'
    square = 'http://i.imgur.com/HFNR3fs.png'
    cone = 'http://i.imgur.com/Ievab1N.png'
    wave = 'http://i.imgur.com/CejaQ8C.png'
    x = 'http://i.imgur.com/anYlNRb.png'
    melee_point = 'http://i.imgur.com/oLGyQrf.png'
    line_2 = 'http://i.imgur.com/8m66T5y.png'
    line_3 = 'http://i.imgur.com/j9RpR23.png'
    side_line_2 = 'http://i.imgur.com/lxlckBh.png'
    side_line_3 = 'http://i.imgur.com/W7jZB1R.png'
    halo = 'http://i.imgur.com/vp8K3ou.png'
    side_multi_point = 'http://i.imgur.com/4n7lbv1.png'
    melee_x = 'http://i.imgur.com/6jpEhfb.png'
    t = 'http://i.imgur.com/P4kpZox.png'
    y = 'http://i.imgur.com/vmb2P3N.png'
    range_point = 'http://i.imgur.com/CsJDRVa.png'
    range_multi_point = 'http://i.imgur.com/ldZwwVO.png'
    range_circle = 'http://i.imgur.com/bTYrZBc.png'
    cone_3 = 'http://i.imgur.com/5qYh6je.png'


class DamageType(aenum.AutoNumberEnum):
    slashing = ()
    piercing = ()
    bludgeoning = ()
    fire = ()
    cold = ()
    lightning = ()
    acid = ()
    poison = ()
    force = ()
    psychic = ()

    @property
    def cap_name(self) -> str:
        return self.name.title()


class Item:
    def __init__(self, name: str, slot: Slot=Slot.item,
                 rarity: Rarity=Rarity.common, price: int=0, effect: str=''):
        self.slot = slot
        self.name = name
        self.rarity = rarity
        self.price = price
        self.effect = effect


class Wearable(Item):
    def __init__(self, slot: Slot, name: str, min_attribute: Attribute, min_attribute_value: int=0,
                 rarity: Rarity=Rarity.common, price: int=0,
                 effect: str='', equip_type: Type=Type.light,
                 stren: int = 0, dex: int = 0, con: int = 0, intel: int = 0, wis: int = 0,
                 cha: int = 0,
                 ath: int = 0, ste: int = 0, fort: int = 0, apt: int = 0, per: int = 0,
                 spe: int = 0,
                 ap: int = 0, hp: int = 0, mp: int = 0, sp: int = 0, pdef: int = 0, mdef: int = 0,
                 pred: float = 0.0, mred: float = 0.0, reg: int = 0, rd: int = 0, speed: float = 0,
                 vis: int = 0, bpac: int = 0, bmac: int = 0, cran: int = 0):
        self.min_attribute = min_attribute
        self.min_attribute_value = min_attribute_value
        self.type = equip_type
        self.str = stren
        self.dex = dex
        self.con = con
        self.int = intel
        self.wis = wis
        self.cha = cha
        self.ath = ath
        self.ste = ste
        self.fort = fort
        self.apt = apt
        self.per = per
        self.spe = spe
        self.ap = ap
        self.hp = hp
        self.mp = mp
        self.sp = sp
        self.pdef = pdef
        self.mdef = mdef
        self.pred = pred
        self.mred = mred
        self.reg = reg
        self.rd = rd
        self.speed = speed
        self.vis = vis
        self.bpac = bpac
        self.bmac = bmac
        self.cran = cran
        super().__init__(slot=slot, name=name, rarity=rarity, price=price, effect=effect)


class Utility(Wearable):
    def __init__(self, name: str, min_int: int=0, rarity: Rarity=Rarity.common,
                 price: int = 0, effect: str = '', equip_type: Type=Type.light,
                 stren: int = 0, dex: int = 0, con: int = 0, intel: int = 0, wis: int = 0,
                 cha: int = 0,
                 ath: int = 0, ste: int = 0, fort: int = 0, apt: int = 0, per: int = 0,
                 spe: int = 0,
                 ap: int = 0, hp: int = 0, mp: int = 0, sp: int = 0, pdef: int = 0, mdef: int = 0,
                 pred: float = 0.0, mred: float = 0.0, reg: int = 0, rd: int = 0, speed: float = 0,
                 vis: int = 0, bpac: int = 0, bmac: int = 0,
                 is_two_handed: bool=False):
        self.is_two_handed = is_two_handed
        super().__init__(slot=Slot.utility, name=name, min_attribute=Attribute.intel,
                         min_attribute_value=min_int, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Head(Wearable):
    def __init__(self, name: str, min_int: int=0, rarity: Rarity=Rarity.common,
                 price: int=0, effect: str='', equip_type: Type=Type.light,
                 stren: int = 0, dex: int = 0, con: int = 0, intel: int = 0, wis: int = 0,
                 cha: int = 0,
                 ath: int = 0, ste: int = 0, fort: int = 0, apt: int = 0, per: int = 0,
                 spe: int = 0,
                 ap: int = 0, hp: int = 0, mp: int = 0, sp: int = 0, pdef: int = 0, mdef: int = 0,
                 pred: float = 0.0, mred: float = 0.0, reg: int = 0, rd: int = 0, speed: float = 0,
                 vis: int = 0, bpac: int = 0, bmac: int = 0,
                 is_two_handed: bool=False):
        self.is_two_handed = is_two_handed
        super().__init__(slot=Slot.head, name=name, min_attribute=Attribute.intel,
                         min_attribute_value=min_int, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Neck(Wearable):
    def __init__(self, name: str, min_wis: int=0, rarity: Rarity=Rarity.common,
                 price: int=0, effect: str='', equip_type: Type=Type.light,
                 stren: int = 0, dex: int = 0, con: int = 0, intel: int = 0, wis: int = 0,
                 cha: int = 0,
                 ath: int = 0, ste: int = 0, fort: int = 0, apt: int = 0, per: int = 0,
                 spe: int = 0,
                 ap: int = 0, hp: int = 0, mp: int = 0, sp: int = 0, pdef: int = 0, mdef: int = 0,
                 pred: float = 0.0, mred: float = 0.0, reg: int = 0, rd: int = 0, speed: float = 0,
                 vis: int = 0, bpac: int = 0, bmac: int = 0,
                 is_two_handed: bool=False):
        self.is_two_handed = is_two_handed
        super().__init__(slot=Slot.neck, name=name, min_attribute=Attribute.wis,
                         min_attribute_value=min_wis, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Chest(Wearable):
    def __init__(self, name: str, min_str: int=0, rarity: Rarity=Rarity.common,
                 price: int=0, effect: str='', equip_type: Type=Type.light,
                 stren: int = 0, dex: int = 0, con: int = 0, intel: int = 0, wis: int = 0,
                 cha: int = 0,
                 ath: int = 0, ste: int = 0, fort: int = 0, apt: int = 0, per: int = 0,
                 spe: int = 0,
                 ap: int = 0, hp: int = 0, mp: int = 0, sp: int = 0, pdef: int = 0, mdef: int = 0,
                 pred: float = 0.0, mred: float = 0.0, reg: int = 0, rd: int = 0, speed: float = 0,
                 vis: int = 0, bpac: int = 0, bmac: int = 0,
                 is_two_handed: bool=False):
        self.is_two_handed = is_two_handed
        super().__init__(slot=Slot.chest, name=name, min_attribute=Attribute.stren,
                         min_attribute_value=min_str, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Shield(Wearable):
    def __init__(self, name: str, min_str: int=0, rarity: Rarity=Rarity.common,
                 price: int=0, effect: str='', equip_type: Type=Type.light,
                 stren: int = 0, dex: int = 0, con: int = 0, intel: int = 0, wis: int = 0,
                 cha: int = 0,
                 ath: int = 0, ste: int = 0, fort: int = 0, apt: int = 0, per: int = 0,
                 spe: int = 0,
                 ap: int = 0, hp: int = 0, mp: int = 0, sp: int = 0, pdef: int = 0, mdef: int = 0,
                 pred: float = 0.0, mred: float = 0.0, reg: int = 0, rd: int = 0, speed: float = 0,
                 vis: int = 0, bpac: int = 0, bmac: int = 0,
                 is_two_handed: bool=False):
        self.is_two_handed = is_two_handed
        super().__init__(slot=Slot.shield, name=name, min_attribute=Attribute.stren,
                         min_attribute_value=min_str, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Feet(Wearable):
    def __init__(self, name: str, min_str: int=0, rarity: Rarity=Rarity.common,
                 price: int=0, effect: str='', equip_type: Type=Type.light,
                 stren: int = 0, dex: int = 0, con: int = 0, intel: int = 0, wis: int = 0,
                 cha: int = 0,
                 ath: int = 0, ste: int = 0, fort: int = 0, apt: int = 0, per: int = 0,
                 spe: int = 0,
                 ap: int = 0, hp: int = 0, mp: int = 0, sp: int = 0, pdef: int = 0, mdef: int = 0,
                 pred: float = 0.0, mred: float = 0.0, reg: int = 0, rd: int = 0, speed: float = 0,
                 vis: int = 0, bpac: int = 0, bmac: int = 0,
                 is_two_handed: bool=False):
        self.is_two_handed = is_two_handed
        super().__init__(slot=Slot.feet, name=name, min_attribute=Attribute.stren,
                         min_attribute_value=min_str, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Hand(Wearable):
    def __init__(self, name: str, min_cha: int=0, rarity: Rarity=Rarity.common,
                 price: int=0, effect: str='', equip_type: Type=Type.light,
                 stren: int = 0, dex: int = 0, con: int = 0, intel: int = 0, wis: int = 0,
                 cha: int = 0,
                 ath: int = 0, ste: int = 0, fort: int = 0, apt: int = 0, per: int = 0,
                 spe: int = 0,
                 ap: int = 0, hp: int = 0, mp: int = 0, sp: int = 0, pdef: int = 0, mdef: int = 0,
                 pred: float = 0.0, mred: float = 0.0, reg: int = 0, rd: int = 0, speed: float = 0,
                 vis: int = 0, bpac: int = 0, bmac: int = 0,
                 is_two_handed: bool=False):
        self.is_two_handed = is_two_handed
        super().__init__(slot=Slot.hand, name=name, min_attribute=Attribute.cha,
                         min_attribute_value=min_cha, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


@enum.unique
class WeaponPicture(enum.Enum):
    hands = ('http://img1.wikia.nocookie.net/__cb20140420170312/finalfantasy/images/2/24/'
             'Unarmed.png')
    grey_knife = ('http://img4.wikia.nocookie.net/__cb20140415211502/finalfantasy/images/5/58/'
                  'Knife.png')
    blue_knife = ('http://img2.wikia.nocookie.net/__cb20140420224051/finalfantasy/images/7/7e/'
                  'Mythril_Knife.png')
    green_knife = ('http://img1.wikia.nocookie.net/__cb20140420224358/finalfantasy/images/e/e7/'
                   'Mage_Masher.png')
    yellow_knife = ('http://img2.wikia.nocookie.net/__cb20140420224118/finalfantasy/images/9/90/'
                    'Orichalum.png')
    red_knife = ('http://img1.wikia.nocookie.net/__cb20140420224139/finalfantasy/images/4/45/'
                 'Assassin_Dagger.png')
    orange_knife = ('http://img3.wikia.nocookie.net/__cb20111222092919/finalfantasy/images/c/c6/'
                    'FF4PSP_Weapon_Dancing_Dagger.png')
    dark_knife = ('http://img3.wikia.nocookie.net/__cb20130121182239/finalfantasy/images/8/89/'
                  'Valiant_Knife_ATB.png')
    black_knife = ('http://img4.wikia.nocookie.net/__cb20130121182327/finalfantasy/images/d/d4/'
                   'Zwill_Crossblade_ATB.png')
    purple_knife = ('http://img3.wikia.nocookie.net/__cb20130123233601/finalfantasy/images/c/c3/'
                    'Mythril_Knife_ATB.png')
    tooth_knife = ('http://img4.wikia.nocookie.net/__cb20130123233542/finalfantasy/images/4/46/'
                   'Main_Gauche_ATB.png')
    brown_knife = ('http://img4.wikia.nocookie.net/__cb20130123233526/finalfantasy/images/2/2c/'
                   'Mage_Masher_ATB.png')
    light_green_knife = ('http://img3.wikia.nocookie.net/__cb20130123233509/finalfantasy/images/'
                         '6/6f/Air_Knife_ATB.png')
    circle_knife = ('http://img2.wikia.nocookie.net/__cb20130121182311/finalfantasy/images/4/4f/'
                    'Thief%27s_Knife_ATB.png')
    dark_red_knife = ('http://img4.wikia.nocookie.net/__cb20130121182343/finalfantasy/images/f/f0/'
                      'Assassin%27s_Dagger_ATB.png')
    gold_knife = ('http://img1.wikia.nocookie.net/__cb20130126030958/finalfantasy/images/e/ea/'
                  'Gladius_ATB.png')
    grey_rapier = ('http://img3.wikia.nocookie.net/__cb20140420230918/finalfantasy/images/e/e7/'
                   'Sabre.png')
    green_rapier = ('http://img2.wikia.nocookie.net/__cb20140420233627/finalfantasy/images/2/25/'
                    'Wyrmkiller.png')
    gold_rapier = ('http://img2.wikia.nocookie.net/__cb20140420231931/finalfantasy/images/1/1d/'
                   'Enhancer.png')
    grey_sword = ('http://img4.wikia.nocookie.net/__cb20111222092920/finalfantasy/images/a/ab/'
                  'FF4PSP_Weapon_Masamune.png')
    blue_sword = ('http://img2.wikia.nocookie.net/__cb20111222092919/finalfantasy/images/4/46/'
                  'FF4PSP_Weapon_Ashura.png')
    yellow_sword = ('http://img3.wikia.nocookie.net/__cb20111222092920/finalfantasy/images/8/80/'
                    'FF4PSP_Weapon_Kiku-ichimonji.png')
    red_sword = ('http://img1.wikia.nocookie.net/__cb20111222093045/finalfantasy/images/b/b7/'
                 'FF4PSP_Weapon_Deathbringer.png')
    purple_sword = ('http://img1.wikia.nocookie.net/__cb20111222092920/finalfantasy/images/a/ae/'
                    'FF4PSP_Weapon_Kotetsu.png')
    sun_sword = ('http://img3.wikia.nocookie.net/__cb20130121182444/finalfantasy/images/5/53/'
                 'Sun_Blade_ATB.png')
    glow_sword = ('http://img1.wikia.nocookie.net/__cb20130123233212/finalfantasy/images/0/0a/'
                  'Ultima_Weapon_%28Great_Sword%29_ATB.png')
    green_sword = ('http://img4.wikia.nocookie.net/__cb20130123233408/finalfantasy/images/0/08/'
                   'Ancient_Sword_ATB.png')
    flame_sword = ('http://img2.wikia.nocookie.net/__cb20130121182357/finalfantasy/images/8/8e/'
                   'Flametongue_ATB.png')
    dark_sword = ('http://img3.wikia.nocookie.net/__cb20130126031019/finalfantasy/images/1/14/'
                  'Arc_Sword_ATB.png')
    diamond_sword = ('http://img2.wikia.nocookie.net/__cb20130121182208/finalfantasy/images/3/37/'
                     'Diamond_Sword_ATB.png')
    tooth_sword = ('http://img2.wikia.nocookie.net/__cb20130123233131/finalfantasy/images/2/24/'
                   'Blood_Sword_ATB.png')
    white_sword = ('http://img1.wikia.nocookie.net/__cb20130121183942/finalfantasy/images/4/40/'
                   'Treaty_Blade_ATB.png')
    black_sword = ('http://img3.wikia.nocookie.net/__cb20130123233046/finalfantasy/images/e/ee/'
                   'Ragnarok_ATB.png')
    dark_red_sword = ('http://img4.wikia.nocookie.net/__cb20130121182154/finalfantasy/images/f/f6/'
                      'Excalibur_ATB.png')
    dark_blue_sword = ('http://img2.wikia.nocookie.net/__cb20130121182138/finalfantasy/images/'
                       '3/30/Excalipoor_ATB.png')
    crystal_sword = ('http://img3.wikia.nocookie.net/__cb20130121183030/finalfantasy/images/9/95/'
                     'Crystal_Blade_ATB.png')
    light_sword = ('http://img2.wikia.nocookie.net/__cb20130121182500/finalfantasy/images/2/2a/'
                   'Lightbringer_ATB.png')
    bladed_sword = ('http://img2.wikia.nocookie.net/__cb20130121183606/finalfantasy/images/d/df/'
                    'Nanatsusayanotachi_ATB.png')
    teal_sword = ('http://img1.wikia.nocookie.net/__cb20130121083536/finalfantasy/images/3/30/'
                  'Brotherhood_ATB.png')
    brown_flame_sword = ('http://img4.wikia.nocookie.net/__cb20130121083352/finalfantasy/images/'
                         '5/5b/Omega_Weapon_FF13_ATB.png')
    wide_sword = ('http://img1.wikia.nocookie.net/__cb20130121183015/finalfantasy/images/a/a4/'
                  'Hardedge_ATB.png')
    black_tooth_sword = ('http://img3.wikia.nocookie.net/__cb20130121182942/finalfantasy/images/'
                         'd/d0/Butterfly_Edge_ATB.png')
    grey_broadsword = ('http://img4.wikia.nocookie.net/__cb20140417043615/finalfantasy/images/'
                       '7/75/BarbarianSword.png')
    orange_broadsword = ('http://img2.wikia.nocookie.net/__cb20140420230948/finalfantasy/images/'
                         '2/21/Werebuster.png')
    green_broadsword = ('http://img2.wikia.nocookie.net/__cb20140420231831/finalfantasy/images/'
                        'c/cd/DefenderFF1.png')
    pink_broadsword = ('http://img3.wikia.nocookie.net/__cb20140420231704/finalfantasy/images/'
                       '4/43/Braveheart.png')
    black_broadsword = ('http://img1.wikia.nocookie.net/__cb20140420231237/finalfantasy/images/'
                        '2/2a/Dark_Claymore.png')
    yellow_broadsword = ('http://img1.wikia.nocookie.net/__cb20140420233042/finalfantasy/images/'
                         'c/c3/Lightbringer.png')
    grey_longsword = ('http://img4.wikia.nocookie.net/__cb20140420232559/finalfantasy/images/'
                      '3/34/Longsword.png')
    gold_longsword = ('http://img1.wikia.nocookie.net/__cb20140420232319/finalfantasy/images/9/94/'
                      'Rune_Blade.png')
    coral_longsword = ('http://img2.wikia.nocookie.net/__cb20140420232537/finalfantasy/images/'
                       'b/bd/Coral_Sword.png')
    blue_longsword = ('http://img2.wikia.nocookie.net/__cb20140420234028/finalfantasy/images/'
                      '9/91/MythrilSwordFF1.png')
    flame_longsword = ('http://img4.wikia.nocookie.net/__cb20140420233924/finalfantasy/images/'
                       '1/1f/Flame_Sword.png')
    ice_longsword = ('http://img3.wikia.nocookie.net/__cb20140420231118/finalfantasy/images/4/4e/'
                     'Icebrand.png')
    red_longsword = ('http://img2.wikia.nocookie.net/__cb20140420231202/finalfantasy/images/7/7c/'
                     'SunBlade.png')
    black_longsword = ('http://img1.wikia.nocookie.net/__cb20140420233022/finalfantasy/images/'
                       '8/8f/Deathbringer.png')
    crystal_longsword = ('http://img1.wikia.nocookie.net/__cb20140417043709/finalfantasy/images/'
                         '2/2a/UltimaBlade.png')
    tooth_longsword = ('http://img2.wikia.nocookie.net/__cb20130126030829/finalfantasy/images/'
                       '5/5c/Gluttony_Sword_ATB.png')
    grey_royal_sword = ('http://img1.wikia.nocookie.net/__cb20140417044022/finalfantasy/images/'
                        'f/fa/Excalibur.png')
    black_royal_sword = ('http://img2.wikia.nocookie.net/__cb20140417043836/finalfantasy/images/'
                         '3/37/RagnarokFF1.png')
    gold_royal_sword = ('http://img1.wikia.nocookie.net/__cb20111222093046/finalfantasy/images/'
                        '3/30/FF4PSP_Weapon_Excalibur.png')
    pink_royal_sword = ('http://img2.wikia.nocookie.net/__cb20111222093046/finalfantasy/images/'
                        '5/54/FF4PSP_Weapon_Lightbringer.png')
    orange_royal_sword = ('http://img2.wikia.nocookie.net/__cb20111222093044/finalfantasy/images/'
                          '8/8d/FF4PSP_Weapon_Ancient_Sword.png')
    red_royal_sword = ('http://img3.wikia.nocookie.net/__cb20111222093045/finalfantasy/images/'
                       '5/57/FF4PSP_Weapon_Blood_Sword.png')
    blue_royal_sword = ('http://img2.wikia.nocookie.net/__cb20111222093045/finalfantasy/images/'
                        'd/d6/FF4PSP_Weapon_Icebrand.png')
    purple_royal_sword = ('http://img2.wikia.nocookie.net/__cb20111222093045/finalfantasy/images/'
                          'c/cd/FF4PSP_Weapon_Stoneblade.png')
    rainbow_royal_sword = ('http://img1.wikia.nocookie.net/__cb20130121083519/finalfantasy/images/'
                           '4/4f/Caladabolg_ATB.png')
    flame_royal_sword = ('http://img1.wikia.nocookie.net/__cb20130121083502/finalfantasy/images/'
                         '1/1a/Blazefire_Saber_ATB.png')
    red_tooth_royal_sword = ('http://img4.wikia.nocookie.net/__cb20130121182958/finalfantasy/'
                             'images/7/75/Apocalypse_ATB.png')
    green_crystal_royal_sword = ('http://img2.wikia.nocookie.net/__cb20130126030807/finalfantasy/'
                                 'images/2/20/Ultima_Weapon_FFVII_ATB.png')
    dark_tooth_royal_sword = ('http://img3.wikia.nocookie.net/__cb20130126030936/finalfantasy/'
                              'images/4/4a/Masamune_ATB.png')
    grey_scimitar = ('http://img4.wikia.nocookie.net/__cb20140420235357/finalfantasy/images/e/e5/'
                     'Scimitar.png')
    red_scimitar = ('http://img3.wikia.nocookie.net/__cb20130121183747/finalfantasy/images/a/a1/'
                    'Wightslayer_ATB.png')
    yellow_scimitar = ('http://img2.wikia.nocookie.net/__cb20130123233438/finalfantasy/images/'
                       '4/44/Enhancer_ATB.png')
    grey_falchion = ('http://img1.wikia.nocookie.net/__cb20140420235502/finalfantasy/images/0/06/'
                     'FalchionFF1.png')
    green_falchion = ('http://img1.wikia.nocookie.net/__cb20111222092919/finalfantasy/images/3/34/'
                      'FF4PSP_Weapon_Mage_Masher.png')
    grey_shortsword = ('http://img1.wikia.nocookie.net/__cb20140420235657/finalfantasy/images/'
                       'a/ac/Sasuke%27s_Blade.png')
    purple_shortsword = ('http://img1.wikia.nocookie.net/__cb20140420235418/finalfantasy/images/'
                         '1/13/Kotetsu.png')
    red_shortsword = ('http://img3.wikia.nocookie.net/__cb20140420234857/finalfantasy/images/'
                      '5/52/Asura.png')
    green_shortsword = ('http://img1.wikia.nocookie.net/__cb20140420235943/finalfantasy/images/'
                        '4/4a/Murasame.png')
    black_shortsword = ('http://img1.wikia.nocookie.net/__cb20130123233350/finalfantasy/images/'
                        '8/8b/Claymore_ATB.png')
    silver_shortsword = ('http://img3.wikia.nocookie.net/__cb20130123233333/finalfantasy/images/'
                         '4/41/Surviver_ATB.png')
    grey_samurai_sword = ('http://img2.wikia.nocookie.net/__cb20140420234438/finalfantasy/images/'
                          '1/1b/Masamune.png')
    yellow_samurai_sword = ('http://img1.wikia.nocookie.net/__cb20140420234837/finalfantasy/'
                            'images/6/61/Kikuichimonji.png')
    red_nunchaku = ('http://img1.wikia.nocookie.net/__cb20140417043233/finalfantasy/images/7/7d/'
                    'Nunchaku.png')
    black_nunchaku = ('http://img2.wikia.nocookie.net/__cb20140420172602/finalfantasy/images/d/da/'
                      'Iron_Nunchaku.png')
    red_hand_axe = ('http://img4.wikia.nocookie.net/__cb20140420205628/finalfantasy/images/c/ca/'
                    'Battle_Axe.png')
    blue_hand_axe = ('http://img2.wikia.nocookie.net/__cb20140420210028/finalfantasy/images/0/00/'
                     'Mythril_Axe.png')
    yellow_hand_axe = ('http://img2.wikia.nocookie.net/__cb20130121182729/finalfantasy/images/'
                       '1/14/Light_Axe_ATB.png')
    grey_hand_axe = ('http://img2.wikia.nocookie.net/__cb20130121182714/finalfantasy/images/2/22/'
                     'Rune_Axe_ATB.png')
    red_great_axe = ('http://img1.wikia.nocookie.net/__cb20140420205650/finalfantasy/images/e/ed/'
                     'Great_Axe.png')
    black_great_axe = ('http://img2.wikia.nocookie.net/__cb20140420210626/finalfantasy/images/'
                       'f/f5/Ogrekiller.png')
    blue_great_axe = ('http://img2.wikia.nocookie.net/__cb20140420210213/finalfantasy/images/4/41/'
                      'Light_Axe.png')
    yellow_great_axe = ('http://img2.wikia.nocookie.net/__cb20140420210645/finalfantasy/images/'
                        '4/42/Rune_Axe.png')
    dark_purple_great_axe = ('http://img3.wikia.nocookie.net/__cb20140420210706/finalfantasy/'
                             'images/d/d2/Gigantaxe.png')
    orange_great_axe = ('http://img1.wikia.nocookie.net/__cb20111224101248/finalfantasy/images/'
                        '2/20/FF4PSP_Weapon_Dwarven_Axe.png')
    dark_blue_great_axe = ('http://img2.wikia.nocookie.net/__cb20111224101248/finalfantasy/images/'
                           '5/5c/FF4PSP_Weapon_Ogrekiller.png')
    purple_great_axe = ('http://img2.wikia.nocookie.net/__cb20130607162746/finalfantasy/images/'
                        '4/4b/FF4PSP_Weapon_Rune_Axe.png')
    brown_hammer = ('http://img4.wikia.nocookie.net/__cb20140420204306/finalfantasy/images/5/52/'
                    'HammerFF1.png')
    blue_hammer = ('http://img1.wikia.nocookie.net/__cb20140420203837/finalfantasy/images/6/6a/'
                   'Mythril_Hammer.png')
    red_hammer = ('http://img2.wikia.nocookie.net/__cb20111224101247/finalfantasy/images/0/01/'
                  'FF4PSP_Weapon_Mythril_Hammer.png')
    yellow_hammer = ('http://img2.wikia.nocookie.net/__cb20111224101248/finalfantasy/images/d/d0/'
                     'FF4PSP_Weapon_Gaia_Hammer.png')
    dark_blue_hammer = ('http://img4.wikia.nocookie.net/__cb20111224101248/finalfantasy/images/'
                        '3/3b/FF4PSP_Weapon_Thor%27s_Hammer.png')
    orange_hammer = ('http://img3.wikia.nocookie.net/__cb20111224101248/finalfantasy/images/a/a1/'
                     'FF4PSP_Weapon_Flare_Sledgehammer.png')
    purple_war_hammer = ('http://img4.wikia.nocookie.net/__cb20140420203922/finalfantasy/images/'
                         '9/96/Thor%27s_Hammer.png')
    black_war_hammer = ('http://img4.wikia.nocookie.net/__cb20140417035400/finalfantasy/images/'
                        '3/30/WarHammer.png')
    wooden_staff = ('http://img3.wikia.nocookie.net/__cb20140415225056/finalfantasy/images/'
                    'b/bb/Staff.png')
    green_wooden_staff = ('http://img1.wikia.nocookie.net/__cb20140417041415/finalfantasy/images/'
                          '8/82/PowerStaff.png')
    brown_staff = ('http://img1.wikia.nocookie.net/__cb20140417040855/finalfantasy/images/c/cf/'
                   'SagesStaff.png')
    blue_staff = ('http://img1.wikia.nocookie.net/__cb20111221160314/finalfantasy/images/f/f0/'
                  'FF4PSP_Weapon_Mythril_Staff.png')
    red_staff = ('http://img2.wikia.nocookie.net/__cb20111221160315/finalfantasy/images/6/64/'
                 'FF4PSP_Weapon_Sage%27s_Staff.png')
    green_staff = ('http://img1.wikia.nocookie.net/__cb20111221160314/finalfantasy/images/f/fc/'
                   'FF4PSP_Weapon_Rune_Staff.png')
    grey_staff = ('http://img4.wikia.nocookie.net/__cb20140417042120/finalfantasy/images/a/aa/'
                  'Crosier.png')
    flame_staff = ('http://img4.wikia.nocookie.net/__cb20130121181948/finalfantasy/images/1/11/'
                   'Mage%27s_Staff_ATB.png')
    purple_staff = ('http://img3.wikia.nocookie.net/__cb20130123233031/finalfantasy/images/7/7a/'
                    'High_Mage%27s_Staff_ATB.png')
    teal_staff = ('http://img2.wikia.nocookie.net/__cb20130119084715/finalfantasy/images/6/6a/'
                  'Rune_Staff_ATB.png')
    yellow_blue_staff = ('http://img3.wikia.nocookie.net/__cb20130121084219/finalfantasy/images/'
                         '1/13/Yuna%27s_Staff_ATB.png')
    purple_cross_staff = ('http://img4.wikia.nocookie.net/__cb20130126031038/finalfantasy/images/'
                          '0/04/Judicer%27s_Staff_ATB.png')
    red_feather_staff = ('http://img3.wikia.nocookie.net/__cb20130121083552/finalfantasy/images/'
                         '4/4c/Nirvana_ATB.png')
    yellow_purple_staff = ('http://img3.wikia.nocookie.net/__cb20130121182025/finalfantasy/images/'
                           'd/d6/Wizer_Rod_ATB.png')
    yellow_red_staff = ('http://img3.wikia.nocookie.net/__cb20130121083445/finalfantasy/images/'
                        '2/2b/Princess_Guard_ATB.png')
    red_green_staff = ('http://img1.wikia.nocookie.net/__cb20130121182005/finalfantasy/images/'
                       'e/ef/Wizard%27s_Staff_ATB.png')
    green_rod = ('http://img1.wikia.nocookie.net/__cb20140420172828/finalfantasy/images/f/f6/'
                 'Healing_Staff.png')
    blue_rod = ('http://img3.wikia.nocookie.net/__cb20140420172925/finalfantasy/images/2/28/'
                'Mage%27s_Staff.png')
    red_rod = ('http://img3.wikia.nocookie.net/__cb20140420203602/finalfantasy/images/7/71/'
               'Wizard%27s_Staff.png')
    orange_rod = ('http://img2.wikia.nocookie.net/__cb20140417042804/finalfantasy/images/6/6b/'
                  'JudgementStaff.png')
    yellow_rod = ('http://img2.wikia.nocookie.net/__cb20140417040236/finalfantasy/images/c/c4/'
                  'RuneStaff.png')
    pink_rod = ('http://img2.wikia.nocookie.net/__cb20111221160236/finalfantasy/images/6/65/'
                'FF4PSP_Weapon_Stardust_Rod.png')
    gold_rod = ('http://img1.wikia.nocookie.net/__cb20111221160235/finalfantasy/images/1/1a/'
                'FF4PSP_Weapon_Faerie_Rod.png')
    pink_circle_rod = ('http://img3.wikia.nocookie.net/__cb20130121183520/finalfantasy/images/'
                       '0/09/Stardust_Rod_ATB.png')
    ank_rod = ('http://img3.wikia.nocookie.net/__cb20130121183235/finalfantasy/images/7/7f/'
               'Mythril_Rod_ATB.png')
    flame_rod = ('http://img4.wikia.nocookie.net/__cb20130121183345/finalfantasy/images/4/4f/'
                 'Flame_Rod_ATB.png')
    light_rod = ('http://img1.wikia.nocookie.net/__cb20130123233003/finalfantasy/images/1/11/'
                 'Shining_Staff_ATB.png')
    gold_circle_rod = ('http://img2.wikia.nocookie.net/__cb20130121181824/finalfantasy/images/'
                       'a/a7/Mace_of_Zeus_ATB.png')
    ivy_rod = ('http://img2.wikia.nocookie.net/__cb20130121183303/finalfantasy/images/3/3e/'
               'Gaia_Rod_ATB.png')
    purple_rod = ('http://img2.wikia.nocookie.net/__cb20130121183504/finalfantasy/images/c/cf/'
                  'Thunder_Rod_ATB.png')
    teal_rod = ('http://img1.wikia.nocookie.net/__cb20130121183450/finalfantasy/images/0/06/'
                'Poison_Rod_ATB.png')
    dark_purple_rod = ('http://img2.wikia.nocookie.net/__cb20130121183539/finalfantasy/images/'
                       '6/65/Lilith_Rod_ATB.png')
    grey_spear = ('http://img3.wikia.nocookie.net/__cb20111221160146/finalfantasy/images/3/3f/'
                  'FF4PSP_Weapon_Spear.png')
    purple_spear = ('http://img1.wikia.nocookie.net/__cb20111221160146/finalfantasy/images/2/27/'
                    'FF4PSP_Weapon_Wind_Spear.png')
    red_spear = ('http://img1.wikia.nocookie.net/__cb20111221160145/finalfantasy/images/7/74/'
                 'FF4PSP_Weapon_Flame_Lance.png')
    blue_spear = ('http://img2.wikia.nocookie.net/__cb20111221160146/finalfantasy/images/f/f5/'
                  'FF4PSP_Weapon_Ice_Lance.png')
    yellow_spear = ('http://img3.wikia.nocookie.net/__cb20111221160146/finalfantasy/images/e/ef/'
                    'FF4PSP_Weapon_Wyvern_Lance.png')
    gold_spear = ('http://img1.wikia.nocookie.net/__cb20130123232643/finalfantasy/images/d/d5/'
                  'Golden_Spear_ATB.png')
    moon_spear = ('http://img1.wikia.nocookie.net/__cb20130121183216/finalfantasy/images/6/6b/'
                  'Impartisan_ATB.png')
    yellow_trident = ('http://img4.wikia.nocookie.net/__cb20130123232659/finalfantasy/images/6/64/'
                      'Javelin_ATB.png')
    grey_trident = ('http://img4.wikia.nocookie.net/__cb20130123232621/finalfantasy/images/2/2e/'
                    'Trident_ATB.png')
    blue_trident = ('http://img4.wikia.nocookie.net/__cb20130121183159/finalfantasy/images/a/a1/'
                    'Wind_Spear_ATB.png')
    dark_purple_spear = ('http://img2.wikia.nocookie.net/__cb20130119084746/finalfantasy/images/'
                         '7/79/Blood_Lance_ATB.png')
    rainbow_spear = ('http://img3.wikia.nocookie.net/__cb20130121182533/finalfantasy/images/e/e8/'
                     'Partisan_ATB.png')
    bladed_spear = ('http://img1.wikia.nocookie.net/__cb20130123232558/finalfantasy/images/9/91/'
                    'Holy_Lance_ATB.png')
    glow_spear = ('http://img1.wikia.nocookie.net/__cb20130121182607/finalfantasy/images/c/c2/'
                  'Radiant_Lance_ATB.png')
    purple_blue_spear = ('http://img3.wikia.nocookie.net/__cb20130126032412/finalfantasy/images/'
                         '2/29/Wyvern%27s_Lance_ATB.png')
    orange_bow = ('http://img4.wikia.nocookie.net/__cb20121021233857/finalfantasy/images/d/d8/'
                  'FF4PSP_Weapon_Bow_and_Arrows.png')
    blue_bow = ('http://img1.wikia.nocookie.net/__cb20121021233949/finalfantasy/images/c/ce/'
                'FF4PSP_Weapon_Crossbow_and_Arrows.png')
    grey_bow = ('http://img2.wikia.nocookie.net/__cb20121021233844/finalfantasy/images/d/d8/'
                'FF4PSP_Weapon_Perseus_Bow_and_Arrows.png')
    purple_bow = ('http://img1.wikia.nocookie.net/__cb20121021234008/finalfantasy/images/7/79/'
                  'FF4PSP_Weapon_Killer_Bow_and_Arrows.png')
    green_bow = ('http://img3.wikia.nocookie.net/__cb20121021234015/finalfantasy/images/8/80/'
                 'FF4PSP_Weapon_Elfin_Bow_and_Arrows.png')
    red_bow = ('http://img2.wikia.nocookie.net/__cb20121021234024/finalfantasy/images/0/09/'
               'FF4PSP_Weapon_Yoichi_Bow_and_Arrows.png')
    leaf_bow = ('http://img4.wikia.nocookie.net/__cb20130121182830/finalfantasy/images/5/55/'
                'Elven_Bow_ATB.png')
    red_feather_bow = ('http://img2.wikia.nocookie.net/__cb20130121182800/finalfantasy/images/'
                       'f/fa/Killer_Bow_ATB.png')
    white_bow = ('http://img2.wikia.nocookie.net/__cb20130123232536/finalfantasy/images/5/5a/'
                 'Artemis_Bow_ATB.png')
    brown_bow = ('http://img4.wikia.nocookie.net/__cb20130119084659/finalfantasy/images/8/8d/'
                 'Yoichi_Bow_ATB.png')
    pink_bow = ('http://img1.wikia.nocookie.net/__cb20130121182816/finalfantasy/images/0/00/'
                'Aevis_Killer_ATB.png')
    arrow = ('http://img2.wikia.nocookie.net/__cb20121022180755/finalfantasy/images/8/83/'
             'FFIV_PSP_Arrow.png')
    orange_whip = ('http://img2.wikia.nocookie.net/__cb20111220140556/finalfantasy/images/6/6b/'
                   'FF4PSP_Weapon_Whip.png')
    grey_whip = ('http://img1.wikia.nocookie.net/__cb20111220140557/finalfantasy/images/8/83/'
                 'FF4PSP_Weapon_Chain_Whip.png')
    yellow_whip = ('http://img2.wikia.nocookie.net/__cb20111220140557/finalfantasy/images/3/32/'
                   'FF4PSP_Weapon_Blitz_Whip.png')
    red_whip = ('http://img2.wikia.nocookie.net/__cb20111220140557/finalfantasy/images/9/9c/'
                'FF4PSP_Weapon_Flame_Whip.png')
    green_whip = ('http://img3.wikia.nocookie.net/__cb20111220140558/finalfantasy/images/4/47/'
                  'FF4PSP_Weapon_Dragon_Whisker.png')
    brown_whip = ('http://img2.wikia.nocookie.net/__cb20130123232511/finalfantasy/images/0/0b/'
                  'Beast_Killer_ATB.png')
    light_red_whip = ('http://img3.wikia.nocookie.net/__cb20130123232448/finalfantasy/images/8/8e/'
                      'Fire_Lash_ATB.png')
    white_green_whip = ('http://img4.wikia.nocookie.net/__cb20130126032353/finalfantasy/images/'
                        '9/98/Dragon_Whisker_ATB.png')
    grey_shuriken = ('http://img2.wikia.nocookie.net/__cb20111224101247/finalfantasy/images/6/6c/'
                     'FF4PSP_Weapon_Shuriken.png')
    red_shuriken = ('http://img2.wikia.nocookie.net/__cb20100701203229/finalfantasy/images/8/81/'
                    'FFT_Fuma_Shuriken.gif')
    orange_boomerang = ('http://img3.wikia.nocookie.net/__cb20111224101247/finalfantasy/images/'
                        '3/38/FF4PSP_Weapon_Boomerang.png')
    yellow_hoop = ('http://img1.wikia.nocookie.net/__cb20111224101247/finalfantasy/images/c/c2/'
                   'FF4PSP_Weapon_Moonring_Blade.png')
    red_gauntlets = ('http://img2.wikia.nocookie.net/__cb20111224155846/finalfantasy/images/3/34/'
                     'FF4PSP_Weapon_Flame_Claws.png')
    blue_gauntlets = ('http://img1.wikia.nocookie.net/__cb20111224155846/finalfantasy/images/c/c6/'
                      'FF4PSP_Weapon_Ice_Claws.png')
    yellow_gauntlets = ('http://img3.wikia.nocookie.net/__cb20111224155846/finalfantasy/images/'
                        '9/91/FF4PSP_Weapon_Lightning_Claws.png')
    green_gauntlets = ('http://img1.wikia.nocookie.net/__cb20111224155845/finalfantasy/images/'
                       '1/13/FF4PSP_Weapon_Faerie_Claws.png')
    orange_gauntlets = ('http://img1.wikia.nocookie.net/__cb20111224155845/finalfantasy/images/'
                        'd/d1/FF4PSP_Weapon_Cat_Claws.png')
    grey_gauntlets = ('http://img1.wikia.nocookie.net/__cb20111224155846/finalfantasy/images/f/f9/'
                      'FF4PSP_Weapon_Godhand.png')
    dark_gauntlets = ('http://img4.wikia.nocookie.net/__cb20130121084649/finalfantasy/images/a/ad/'
                      'Total_Eclipses_ATB.png')
    orange_harp = ('http://img4.wikia.nocookie.net/__cb20111222092919/finalfantasy/images/a/ad/'
                   'FF4PSP_Weapon_Dream_Harp.png')
    pink_harp = ('http://img4.wikia.nocookie.net/__cb20111222092919/finalfantasy/images/1/16/'
                 'FF4PSP_Weapon_Lamia_Harp.png')
    yellow_harp = ('http://img4.wikia.nocookie.net/__cb20111222092918/finalfantasy/images/7/74/'
                   'FF4PSP_Weapon_Apollo%27s_Harp.png')
    grey_flail = ('http://img3.wikia.nocookie.net/__cb20120522192637/finalfantasy/images/3/33/'
                  'Flail_-_FF5.png')
    blue_flail = ('http://img3.wikia.nocookie.net/__cb20120522192749/finalfantasy/images/5/5d/'
                  'Morning_Star_-_FF5.png')
    brown_flail = ('http://img4.wikia.nocookie.net/__cb20100630195823/finalfantasy/images/c/c9/'
                   'FFT_Iron_Flail.gif')
    red_flail = ('http://img1.wikia.nocookie.net/__cb20100630195824/finalfantasy/images/0/0f/'
                 'FFT_Scorpion_Tail.gif')
    yellow_flail = ('http://img2.wikia.nocookie.net/__cb20130205040910/finalfantasy/images/d/df/'
                    'FFT_Vesper.png')
    grey_claws = ('http://img3.wikia.nocookie.net/__cb20120813172600/finalfantasy/images/6/6d/'
                  'FFTA_Hard_Knuckles.PNG')
    silver_claws = ('http://img4.wikia.nocookie.net/__cb20120815041342/finalfantasy/images/2/2c/'
                    'FFTA_MythrilClaws.png')
    green_claws = ('http://img2.wikia.nocookie.net/__cb20120813172705/finalfantasy/images/9/99/'
                   'FFTA_Sick_Knuckles.PNG')
    blue_claws = ('http://img2.wikia.nocookie.net/__cb20120813172732/finalfantasy/images/9/94/'
                  'FFTA_Dream_Claws.PNG')
    silver_claws_3 = ('http://img3.wikia.nocookie.net/__cb20120813173007/finalfantasy/images/9/94/'
                      'FFTA_Godhand.PNG')
    gold_claws = ('http://img4.wikia.nocookie.net/__cb20120813173039/finalfantasy/images/d/de/'
                  'FFTA_Tiger_Fangs.PNG')
    brown_claws = ('http://img4.wikia.nocookie.net/__cb20120813172804/finalfantasy/images/c/c6/'
                   'FFTA_-_Kaiser_Claw.png')
    red_claws = ('http://img2.wikia.nocookie.net/__cb20120813173108/finalfantasy/images/3/3b/'
                 'FFTA_Death_Claws.PNG')
    purple_claws = ('http://img3.wikia.nocookie.net/__cb20130123232903/finalfantasy/images/c/cf/'
                    'Venom_Claws_ATB.png')
    green_claws_4 = ('http://img3.wikia.nocookie.net/__cb20130123232920/finalfantasy/images/8/8d/'
                     'Duel_Claws_ATB.png')
    red_gold_claws = ('http://img1.wikia.nocookie.net/__cb20130123232933/finalfantasy/images/2/2a/'
                      'Cat_Claws_ATB.png')
    pink_claws = ('http://img1.wikia.nocookie.net/__cb20130123232946/finalfantasy/images/0/06/'
                  'Poison_Knuckles_ATB.png')
    dark_red_claws = ('http://img1.wikia.nocookie.net/__cb20130121183141/finalfantasy/images/9/91/'
                      'Burning_Fists_ATB.png')
    dark_green_claws = ('http://img1.wikia.nocookie.net/__cb20130121183121/finalfantasy/images/'
                        '7/7c/Kaiser_Knuckles_ATB.png')
    brown_pistol = ('http://img1.wikia.nocookie.net/__cb20120813213641/finalfantasy/images/6/63/'
                    'FFTA_Aiot_Gun.PNG')
    white_pistol = ('http://img3.wikia.nocookie.net/__cb20120813214219/finalfantasy/images/3/31/'
                    'FFTA_Silver_Cannon.PNG')
    blue_pistol = ('http://img1.wikia.nocookie.net/__cb20120813215238/finalfantasy/images/9/9d/'
                   'FFTA_Lost_Gun.PNG')
    silver_pistol = ('http://img2.wikia.nocookie.net/__cb20120815041551/finalfantasy/images/4/4f/'
                     'FFTA_MythrilGun.png')
    pink_pistol = ('http://img2.wikia.nocookie.net/__cb20120813215634/finalfantasy/images/5/52/'
                   'FFTA_-_Peacemaker.png')
    dark_blue_pistol = ('http://img1.wikia.nocookie.net/__cb20120813221647/finalfantasy/images/'
                        '4/4c/FFTA_Giot_Gun.PNG')
    grey_pistol = ('http://img3.wikia.nocookie.net/__cb20120813215323/finalfantasy/images/f/ff/'
                   'FFTA_Longbarrel.PNG')
    red_pistol = ('http://img1.wikia.nocookie.net/__cb20120813215400/finalfantasy/images/a/a6/'
                  'FFTA_Outsider.PNG')
    scope_pistol = ('http://img3.wikia.nocookie.net/__cb20120815041612/finalfantasy/images/7/71/'
                    'FFTA_Bindsnipe.PNG')
    orange_pistol = ('http://img2.wikia.nocookie.net/__cb20120815041639/finalfantasy/images/c/c0/'
                     'FFTA_Calling_Gun.PNG')
    normal_pistol = ('http://img1.wikia.nocookie.net/__cb20130121182642/finalfantasy/images/0/0b/'
                     'Quicksilver_ATB.png')
    normal_rifle = ('http://img1.wikia.nocookie.net/__cb20130121182626/finalfantasy/images/8/8b/'
                    'Ulysses_ATB.png')
    flame_rifle = ('http://img2.wikia.nocookie.net/__cb20130121182109/finalfantasy/images/7/71/'
                   'Death_Penalty_ATB.png')
    orange_rifle = ('http://img2.wikia.nocookie.net/__cb20120813214248/finalfantasy/images/9/96/'
                    'FFTA_Riot_Gun.PNG')
    purple_rifle = ('http://img3.wikia.nocookie.net/__cb20120813214343/finalfantasy/images/e/ee/'
                    'FFTA_Chaos_Rifle.PNG')
    red_crossbow = ('http://img2.wikia.nocookie.net/__cb20100630201226/finalfantasy/images/7/71/'
                    'FFT_Bowgun.gif')
    dark_blue_crossbow = ('http://img4.wikia.nocookie.net/__cb20100630201227/finalfantasy/images/'
                          '7/74/FFT_Knightslayer.gif')
    green_crossbow = ('http://img1.wikia.nocookie.net/__cb20100630201227/finalfantasy/images/f/fa/'
                      'FFT_Crossbow.gif')
    purple_crossbow = ('http://img4.wikia.nocookie.net/__cb20100630201228/finalfantasy/images/'
                       '6/6a/FFT_Poison_Bow.gif')
    blue_crossbow = ('http://img4.wikia.nocookie.net/__cb20100630201227/finalfantasy/images/1/19/'
                     'FFT_Gastrophetes.gif')
    repeater_crossbow = 'http://www.pocketknives.biz/ImagesProductsLarge/mk45m.jpg'
    yellow_crossbow = 'http://www.neptuneusa.net/Pic/X9505-TWN.jpg'
    gem_crossbow = 'http://gamesdreams.com/attachment.php?attachmentid=19672&d=1358911506'
    brown_crossbow = ('http://img3.wikia.nocookie.net/__cb20130703182943/finalfantasy/images/5/59/'
                      'Bowgun-ffxii.png')
    grey_crossbow = ('http://img3.wikia.nocookie.net/__cb20130704165011/finalfantasy/images/7/7f/'
                     'ParaminaCrossbow-ffxii.png')
    diamond_crossbow = ('http://img4.wikia.nocookie.net/__cb20130704045448/finalfantasy/images/'
                        '2/2e/Gastrophetes-ffxii.png')
    blade_crossbow = ('http://img3.wikia.nocookie.net/__cb20130704170201/finalfantasy/images/'
                      '1/19/PenetratorCrossbow-ffxii.png')
    blunt_crossbow = ('http://img3.wikia.nocookie.net/__cb20130704062102/finalfantasy/images/4/4e/'
                      'HuntingCrossbow-ffxii.png')
    normal_shotgun = ('http://img2.wikia.nocookie.net/__cb20130121182658/finalfantasy/images/f/f7/'
                      'Bismarck_ATB.png')
    brown_shotgun = ('http://img1.wikia.nocookie.net/__cb20100630200757/finalfantasy/images/1/19/'
                     'FFT_Stoneshooter.gif')
    white_shotgun = ('http://img2.wikia.nocookie.net/__cb20130205041214/finalfantasy/images/8/83/'
                     'FFT_Fomalhaut.png')
    green_shotgun = ('http://img4.wikia.nocookie.net/__cb20100630200757/finalfantasy/images/2/23/'
                     'FFT_Glacial_Gun.gif')
    orange_shotgun = ('http://img3.wikia.nocookie.net/__cb20100630200756/finalfantasy/images/4/49/'
                      'FFT_Blaze_Gun.gif')
    blue_shotgun = ('http://img2.wikia.nocookie.net/__cb20100630200755/finalfantasy/images/7/7c/'
                    'FFT_Blaster.gif')
    white_two_handed_spear = ('http://img3.wikia.nocookie.net/__cb20130119205530/finalfantasy/'
                              'images/6/62/Butterfly_Sword_ATB.png')
    grey_wristblades = ('http://img1.wikia.nocookie.net/__cb20130121182255/finalfantasy/images/'
                        'c/cb/Dancing_Dagger_ATB.png')
    pink_wristblades = ('http://img2.wikia.nocookie.net/__cb20130121183434/finalfantasy/images/'
                        '6/61/Mythril_Claws_ATB.png')
    nail_mace = ('http://img4.wikia.nocookie.net/__cb20130121182410/finalfantasy/images/c/cd/'
                 'Nail_Bat_ATB.png')


class Weapon(Wearable):
    def __init__(self, name: str, picture: WeaponPicture, style: Style, min_dex: int=0,
                 rarity: Rarity=Rarity.common,
                 price: int=0, effect: str='', equip_type: Type=Type.light,
                 stren: int = 0, dex: int = 0, con: int = 0, intel: int = 0, wis: int = 0,
                 cha: int = 0,
                 ath: int = 0, ste: int = 0, fort: int = 0, apt: int = 0, per: int = 0,
                 spe: int = 0,
                 ap: int = 0, hp: int = 0, mp: int = 0, sp: int = 0, pdef: int = 0, mdef: int = 0,
                 pred: float = 0.0, mred: float = 0.0, reg: int = 0, rd: int = 0, speed: float = 0,
                 vis: int = 0, bpac: int = 0, bmac: int = 0,
                 is_two_handed: bool=False,
                 min_range: int=1, max_range: int=1, shape: Shape=Shape.melee_point,
                 attacks: int=1,
                 pac: int=0, damage_type: DamageType=DamageType.slashing,
                 cran: int=0, cdam: int=0,
                 pdam: dice.DiceFormula=None, mdam: dice.DiceFormula=None):
        self.picture = picture
        self.style = style
        self.is_two_handed = is_two_handed
        self.min_range = min_range
        self.max_range = max_range
        self.shape = shape
        self.attacks = attacks
        self.pac = pac
        self.damage_type = damage_type
        self.cran = cran
        self.cdam = cdam
        self.pdam = pdam
        self.mdam = mdam
        super().__init__(slot=Slot.weapon, name=name, min_attribute=Attribute.dex,
                         min_attribute_value=min_dex, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)

    @property
    def macro(self):
        common_template = ('{template_tag}'
                           '{color}'
                           '{{{{title=**{name}** [p]({picture})}}}}'
                           '{{{{subheader={type} {style} Weapon}}}}'
                           '{{{{subheaderright={time}}}}}'
                           '{attacks}'
                           '{{{{emote=@{{Name}} attacks @{{target|Name}}}}}}'
                           '{{{{Crit=[[{cdam}]]CDAM}}}}'
                           '{{{{Range=[[{min_range}]]-[[{max_range}]]}}}}'
                           '{{{{Shape=[p]({shape_picture}) ({shape})}}}}'
                           '{template_terminator}')

        if self.attacks > 1:
            attacks = ('{{{{Attacks=[[?{{Attacks (max={attacks})|'
                       '{attacks}}}]]/{attacks}}}}}').format(attacks=self.attacks)
        else:
            attacks = ''

        macro_str = common_template.format(template_tag=macro.template_tag,
                                           color=macro.MacroColorTag.green.value,
                                           name=self.name,
                                           picture=self.picture.value,
                                           type=self.type.name,
                                           style=self.style.name,
                                           time='StdA',
                                           attacks=attacks,
                                           cdam=self.cdam,
                                           min_range=self.min_range,
                                           max_range=self.max_range,
                                           shape_picture=self.shape.value,
                                           shape=self.shape.name,
                                           template_terminator=macro.template_terminator)

        for i in range(self.attacks):
            attack_template = ('{template_tag}'
                               '{{{{title=Attack}}}}'
                               '{color}'
                               '{hit}'
                               '{pdam}'
                               '{mdam}'
                               '{template_terminator}')

            hit = ('{{{{Hit=[[{{d20cs>{cran}+@{{BPAC}}+{weapon_pac}}}>'
                   '@{{target|PDEF}}]] vs PDEF}}}}'.format(
                        cran=(20 - self.cran),
                        weapon_pac=self.pac))

            damage_template = ('{{{{{damage_category}='
                               '[[round({dam}-@{{target|{reduction_type}}})'
                               '*(1+@{{target|{damage_type}VUL}})'
                               '/(1+@{{target|{damage_type}RES}})'
                               '*(1-@{{target|{damage_type}IMU}})'
                               ']]{damage_category} [{damage_type}]}}}}'
                               '{{{{{damage_type}='
                               'VUL:@{{target|{damage_type}VUL}} '
                               'RES:@{{target|{damage_type}RES}} '
                               'IMU:@{{target|{damage_type}IMU}}'
                               '}}}}')

            pdam = ''
            if self.pdam is not None:
                pdam = damage_template.format(damage_category='PDAM',
                                              dam=self.pdam,
                                              reduction_type='PRED',
                                              damage_type=self.damage_type.cap_name)

            mdam = ''
            if self.mdam is not None:
                mdam = damage_template.format(damage_category='MDAM',
                                              dam=self.mdam,
                                              reduction_type='MRED',
                                              damage_type=self.damage_type.cap_name)

            macro_str += '\n' + attack_template.format(
                template_tag=macro.template_tag,
                color=macro.MacroColorTag.green.value,
                hit=hit,
                pdam=pdam,
                mdam=mdam,
                template_terminator=macro.template_terminator,
            )

        return macro.escape_attributes(macro_str)
