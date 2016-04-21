#!/usr/bin/env python3

import abc
import enum

import aenum

from . import dice


@enum.unique
class Attribute(enum.Enum):
    stren = 1
    dex = 2
    con = 3
    intel = 4
    wis = 5
    cha = 6

    @classmethod
    def from_str(cls, string_name: str) -> 'Attribute':
        for attribute in cls:
            if attribute.name == string_name:
                return attribute
        raise ValueError('Invalid {} name.'.format(cls.__name__))


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


class Equipment(abc.ABC):
    def __init__(self, slot: Slot, name: str, rarity: Rarity, price: int, effect: str):
        self.slot = slot
        self.name = name
        self.rarity = rarity
        self.price = price
        self.effect = effect


class Wearable(Equipment):
    def __init__(self, slot: Slot, name: str, min_attribute: Attribute, min_attribute_value: int=0,
                 rarity: Rarity=Rarity.common, price: int=0,
                 effect: str='', equip_type: Type=Type.light,
                 stren: int = 0, dex: int = 0, con: int = 0, intel: int = 0, wis: int = 0,
                 cha: int = 0,
                 ath: int = 0, ste: int = 0, fort: int = 0, apt: int = 0, per: int = 0,
                 spe: int = 0,
                 ap: int = 0, hp: int = 0, mp: int = 0, sp: int = 0, pdef: int = 0, mdef: int = 0,
                 pred: float = 0.0, mred: float = 0.0, reg: int = 0, rd: int = 0, speed: float = 0,
                 vis: int = 0, bpac: int = 0, bmac: int = 0):
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
        super().__init__(slot=slot, name=name, rarity=rarity, price=price, effect=effect)


class Utility(Wearable):
    def __init__(self, name: str, min_attribute_value: int=0, rarity: Rarity=Rarity.common,
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
                         min_attribute_value=min_attribute_value, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Head(Wearable):
    def __init__(self, name: str, min_attribute_value: int=0, rarity: Rarity=Rarity.common,
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
                         min_attribute_value=min_attribute_value, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Neck(Wearable):
    def __init__(self, name: str, min_attribute_value: int=0, rarity: Rarity=Rarity.common,
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
                         min_attribute_value=min_attribute_value, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Chest(Wearable):
    def __init__(self, name: str, min_attribute_value: int=0, rarity: Rarity=Rarity.common,
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
                         min_attribute_value=min_attribute_value, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Shield(Wearable):
    def __init__(self, name: str, min_attribute_value: int=0, rarity: Rarity=Rarity.common,
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
                         min_attribute_value=min_attribute_value, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Feet(Wearable):
    def __init__(self, name: str, min_attribute_value: int=0, rarity: Rarity=Rarity.common,
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
                         min_attribute_value=min_attribute_value, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Hand(Wearable):
    def __init__(self, name: str, min_attribute_value: int=0, rarity: Rarity=Rarity.common,
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
                         min_attribute_value=min_attribute_value, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)


class Weapon(Wearable):
    def __init__(self, name: str, style: Style, min_attribute_value: int=0,
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
                 min_range: int=1, max_range: int=1, shape: Shape=Shape.point,
                 attacks: int=1,
                 pac: int=0, damage_type: DamageType=DamageType.slashing,
                 cran: int=0, cdam: int=0,
                 pdam: dice.DiceFormula=None, mdam: dice.DiceFormula=None):
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
        super().__init__(slot=Slot.weapon, name=name, min_attribute=Attribute.stren,
                         min_attribute_value=min_attribute_value, rarity=rarity, price=price,
                         effect=effect,
                         stren=stren, dex=dex, con=con, intel=intel, wis=wis, cha=cha,
                         ath=ath, ste=ste, fort=fort, apt=apt, per=per, spe=spe, ap=ap, hp=hp,
                         mp=mp, sp=sp, pdef=pdef, mdef=mdef, pred=pred, mred=mred, reg=reg, rd=rd,
                         speed=speed, vis=vis, bpac=bpac, bmac=bmac,
                         equip_type=equip_type)
