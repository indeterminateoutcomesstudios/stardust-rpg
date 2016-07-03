from ..ability import Ability, AbilityPicture, DurationUnit, Time
from ..class_type import Class
from ..equipment import DamageType, Shape

reflect_1 = Ability(
    name='Reflect [Counter] I', picture=AbilityPicture.shield_oath,
    mp_cost=1, target_area='Self', time=Time.free_a,
    effect='If hit with melee attack, can reflect 1PDAM as TDAM. '
           'Does not reduce incoming damage.'
)

reflect_2 = Ability(
    name='Reflect [Counter] II', picture=AbilityPicture.shield_oath,
    mp_cost=2, target_area='Self', time=Time.free_a,
    effect='If hit with melee attack, can reflect [[1+WIS]]PDAM as TDAM. '
           'Does not reduce incoming damage.',
    prerequisites=(reflect_1,),
)

reflect_3 = Ability(
    name='Reflect [Counter] III', picture=AbilityPicture.shield_oath,
    mp_cost=2, target_area='Self', time=Time.free_a,
    effect='If hit with magic attack, can reflect [[1+WIS]]MDAM as TDAM. '
           'DOes not reduce incoming damage.',
    prerequisites=(reflect_2,),
)

telekinesis_1 = Ability(
    name='Telekinesis I', picture=AbilityPicture.huton,
    mp_cost=1, attacks=1, mdam='1d6',
    damage_type=DamageType.force, targets_mdef=True, max_range='8',
    target_area='Object < 20lb (Small)',
    effect='Can telekinetically interact/(move 4DIS) object (or self) doing MDAM if thrown '
           'against a surface'
)

telekinesis_2 = Ability(
    name='Telekinesis II', picture=AbilityPicture.huton,
    mp_cost=2, attacks=1, mdam='1d8 + WIS',
    damage_type=DamageType.force, targets_mdef=True, max_range='8',
    target_area='Object < 200lb (Medium)',
    effect='Can telekinetically interact/(move 6DIS) object (or self) doing MDAM if thrown '
           'against a surface',
    prerequisites=(telekinesis_1,),
)

telekinesis_3 = Ability(
    name='Telekinesis III', picture=AbilityPicture.huton,
    mp_cost=4, attacks=1, mdam='1d12 + 2*WIS',
    damage_type=DamageType.force, targets_mdef=True, max_range='8',
    target_area='Object < 800lb (Large)',
    effect='Can telekinetically interact/(move 8DIS) object (or self) doing MDAM if thrown '
           'against a surface',
    prerequisites=(telekinesis_2,),
)

protect_1 = Ability(
    name='Protect I', picture=AbilityPicture.cover,
    mp_cost=1, max_range='1', target_area='One ally',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Protected target and caster gain +1PRED. Take ½ DAM for protected target. '
           'Must be adjacent for effect.'
)

protect_2 = Ability(
    name='Protect II', picture=AbilityPicture.cover,
    mp_cost=2, max_range='1', target_area='One ally',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Protected target and caster gain +2PRED. Take full DAM for protected target. '
           'Must be adjacent for effect.',
    prerequisites=(protect_1,),
)

protect_3 = Ability(
    name='Protect III', picture=AbilityPicture.cover,
    mp_cost=3, max_range='1', target_area='One ally',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Protected target and caster gain +[[2+WIS]]PRED. Take full DAM for protected target. '
           'Must be adjacent for effect.',
    prerequisites=(protect_2,),
)

earth_breaker_1 = Ability(
    name='Earth Breaker I', picture=AbilityPicture.rock_breaker,
    mp_cost=2, attacks=1, mdam='1d4',
    damage_type=DamageType.force, targets_mdef=True, max_range='1',
    shape=Shape.line, target_area='5DIS long, 1DIS wide, 4DIS deep',
    effect='Wave rips crevasses into the earth. 15ATH (Jump) check required to cross. '
           '20ATH (Climb) to escape.'
)

earth_breaker_2 = Ability(
    name='Earth Breaker II', picture=AbilityPicture.rock_breaker,
    mp_cost=3, attacks=2, mdam='1d6',
    damage_type=DamageType.force, targets_mdef=True, max_range='1',
    shape=Shape.line, target_area='[[5+WIS]]DIS long, 1DIS wide, 4DIS deep',
    effect='Wave rips crevasses into the earth. 15ATH (Jump) check required to cross. '
           '20ATH (Climb) to escape.',
    prerequisites=(earth_breaker_1,)
)

earth_breaker_3 = Ability(
    name='Earth Breaker III', picture=AbilityPicture.rock_breaker,
    mp_cost=4, attacks=3, mdam='1d8+WIS',
    damage_type=DamageType.force, targets_mdef=True, max_range='1',
    shape=Shape.line, target_area='[[5+2*WIS]]DIS long, 1DIS wide, 4DIS deep',
    effect='Wave rips crevasses into the earth. 15ATH (Jump) check required to cross. '
           '20ATH (Climb) to escape.',
    prerequisites=(earth_breaker_2,)
)

barrier_1 = Ability(
    name='Barrier I', picture=AbilityPicture.protect,
    mp_cost=2, time=Time.free_a, max_range='2', target_area='One ally',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='+2PDEF, can only cast once per RND.'
)

barrier_2 = Ability(
    name='Barrier II', picture=AbilityPicture.protect,
    mp_cost=4, time=Time.free_a, max_range='2', target_area='One ally',
    duration='4+WIS', duration_unit=DurationUnit.rnd,
    effect='+[[2+WIS]]PDEF, can only cast once per RND.',
    prerequisites=(barrier_1,)
)

barrier_3 = Ability(
    name='Barrier III', picture=AbilityPicture.protect,
    mp_cost=6, time=Time.free_a, max_range='2+WIS', target_area='One ally',
    duration='6+WIS', duration_unit=DurationUnit.rnd,
    effect='+[[3+WIS]]PDEF, can only cast once per RND.',
    prerequisites=(barrier_2,)
)

# Tier 2.
shell_1 = Ability(
    name='Shell I', picture=AbilityPicture.sacred_soil,
    mp_cost=5, time=Time.full_a, shape=Shape.circle,
    target_area='Up to [[4+WIS]]RAD',
    duration='1+WIS', duration_unit=DurationUnit.rnd,
    effect='Protective spherical shield blocks abilities/projectiles/objects. '
           '+1 MRED to magic attacks that passes through. '
           '25% chance inanimate projectiles to reflect off. Enemies cannot pass through',
    prerequisites=(reflect_2, barrier_3),
)

shell_2 = Ability(
    name='Shell II', picture=AbilityPicture.sacred_soil,
    mp_cost=7, time=Time.full_a, shape=Shape.circle,
    target_area='Up to [[4+(2*WIS)]]RAD',
    duration='2+WIS', duration_unit=DurationUnit.rnd,
    effect='Protective spherical shield blocks abilities/projectiles/objects. '
           '+[[2+WIS]] MRED to magic attacks that passes through. '
           '50% chance inanimate projectiles to reflect off. Enemies cannot pass through',
    prerequisites=(shell_1,),
)

shell_3 = Ability(
    name='Shell III', picture=AbilityPicture.sacred_soil,
    mp_cost=9, time=Time.full_a, shape=Shape.circle,
    target_area='Up to [[4+(2*WIS)]]RAD',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Protective spherical shield blocks abilities/projectiles/objects. '
           '+[[3+2*WIS]] MRED to magic attacks that passes through. '
           '75% chance inanimate projectiles to reflect off. Enemies cannot pass through',
    prerequisites=(shell_2,),
)

vortex_1 = Ability(
    name='Vortex I', picture=AbilityPicture.perfect_balance,
    mp_cost=4, attacks=1, mdam='1d4',
    damage_type=DamageType.force, targets_mdef=True,
    shape=Shape.circle, target_area='[[2+WIS]]RAD',
    effect='Sucks objects and enemies towards caster and immobilizes.',
    prerequisites=(reflect_1, telekinesis_3)
)

vortex_2 = Ability(
    name='Vortex II', picture=AbilityPicture.perfect_balance,
    mp_cost=5, attacks=1, mdam='1d6+WIS',
    damage_type=DamageType.force, targets_mdef=True,
    shape=Shape.circle, target_area='[[2+WIS]]RAD',
    effect='Sucks objects and enemies towards caster and disables.',
    prerequisites=(vortex_1,)
)

vortex_3 = Ability(
    name='Vortex III', picture=AbilityPicture.perfect_balance,
    mp_cost=6, attacks=1, mdam='1d8+2*WIS',
    damage_type=DamageType.force, targets_mdef=True,
    shape=Shape.circle, target_area='[[2+WIS]]RAD',
    effect='Sucks objects and enemies towards caster and stuns.',
    prerequisites=(vortex_2,)
)

provoke_1 = Ability(
    name='Provoke I', picture=AbilityPicture.provoke,
    mp_cost=2, target_area='2 enemies in [[10+WIS]]DIS',
    targets_mdef=True, shape=Shape.multi_point, duration='1+WIS', duration_unit=DurationUnit.rnd,
    effect='Provokes enemies to attack caster. Can end early.',
    prerequisites=(protect_2, earth_breaker_2)
)

provoke_2 = Ability(
    name='Provoke II', picture=AbilityPicture.provoke,
    mp_cost=3, target_area='3 enemies in [[10+WIS]]DIS',
    targets_mdef=True, shape=Shape.multi_point, duration='1+WIS', duration_unit=DurationUnit.rnd,
    effect='Provokes enemies to attack caster and allures. Can end early.',
    prerequisites=(provoke_1,)
)

provoke_3 = Ability(
    name='Provoke III', picture=AbilityPicture.provoke,
    mp_cost=4, target_area='All enemies in [[10+WIS]]DIS',
    targets_mdef=True, shape=Shape.multi_point, duration='1+WIS', duration_unit=DurationUnit.rnd,
    effect='Provokes enemies to attack caster and allures. Can end early.',
    prerequisites=(provoke_2,)
)

shatter_1 = Ability(
    name='Shatter I', picture=AbilityPicture.sword_oath,
    mp_cost=3, target_area='Self',
    effect='Next successful weapon attack immobilizes for 1RND.',
    prerequisites=(telekinesis_3, earth_breaker_2)
)

shatter_2 = Ability(
    name='Shatter II', picture=AbilityPicture.sword_oath,
    mp_cost=4, target_area='Self',
    effect='Next successful weapon attack disables for 1RND.',
    prerequisites=(shatter_1,)
)

shatter_3 = Ability(
    name='Shatter III', picture=AbilityPicture.sword_oath,
    mp_cost=6, target_area='Self',
    effect='Next successful weapon attack stuns for 1RND.',
    prerequisites=(shatter_1,)
)

mass_barrier_1 = Ability(
    name='Mass Barrier I', picture=AbilityPicture.protect,
    mp_cost=4, max_range='4', target_area='[[2+WIS]] allies',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='+2PDEF',
    prerequisites=(protect_2, barrier_3)
)

mass_barrier_2 = Ability(
    name='Mass Barrier II', picture=AbilityPicture.protect,
    mp_cost=8, max_range='4', target_area='[[2+WIS]] allies',
    duration='4+WIS', duration_unit=DurationUnit.rnd,
    effect='+[[2+WIS]]PDEF',
    prerequisites=(mass_barrier_1,)
)

mass_barrier_3 = Ability(
    name='Mass Barrier III', picture=AbilityPicture.protect,
    mp_cost=12, max_range='4+WIS', target_area='[[2+WIS]] allies',
    duration='6+WIS', duration_unit=DurationUnit.rnd,
    effect='+[[3+WIS]]PDEF',
    prerequisites=(mass_barrier_2,)
)

# Tier 3.
shockwave_1 = Ability(
    name='Shockwave I', picture=AbilityPicture.savage_blade,
    mp_cost=10, attacks=1, mdam='1d20',
    damage_type=DamageType.force, targets_mdef=True, time=Time.full_a,
    shape=Shape.circle, target_area='[[WIS]]RAD',
    effect='Paladin sends a shockwave of telekinetic energy in every direction; 4DIS Knockback',
    prerequisites=(shell_3, shatter_2)
)

shockwave_2 = Ability(
    name='Shockwave II', picture=AbilityPicture.savage_blade,
    mp_cost=12, attacks=1, mdam='1d20+2*WIS',
    damage_type=DamageType.force, targets_mdef=True, time=Time.full_a,
    shape=Shape.circle, target_area='[[WIS]]RAD',
    effect='Paladin sends a shockwave of telekinetic energy in every direction; 6DIS Knockback',
    prerequisites=(shell_3, shatter_2)
)

shockwave_3 = Ability(
    name='Shockwave III', picture=AbilityPicture.savage_blade,
    mp_cost=15, attacks=1, mdam='1d20+1d10+4*WIS',
    damage_type=DamageType.force, targets_mdef=True, time=Time.full_a,
    shape=Shape.circle, target_area='[[WIS]]RAD',
    effect='Paladin sends a shockwave of telekinetic energy in every direction; 8DIS Knockback',
    prerequisites=(shell_3, shatter_2)
)

animate_weapon_1 = Ability(
    name='Animate Weapon I', picture=AbilityPicture.throwing_dagger,
    mp_cost=3, attacks=1, mdam='1d8', max_range='2',
    damage_type=DamageType.force, time=Time.std_a,
    shape=Shape.circle, target_area='Self',
    effect='Caster telekinetically wields melee weapon at range, dealing extra MDAM on hit',
    prerequisites=(vortex_1, shell_2, shatter_1)
)

animate_weapon_2 = Ability(
    name='Animate Weapon II', picture=AbilityPicture.throwing_dagger,
    mp_cost=5, attacks=1, mdam='2d8+WIS', max_range='4+WIS',
    damage_type=DamageType.force, time=Time.std_a,
    shape=Shape.circle, target_area='Self',
    effect='Caster telekinetically wields melee weapon at range, dealing extra MDAM on hit',
    prerequisites=(animate_weapon_1,)
)

animate_weapon_3 = Ability(
    name='Animate Weapon III', picture=AbilityPicture.throwing_dagger,
    mp_cost=8, attacks=1, mdam='3d8+2*WIS', max_range='6+WIS',
    damage_type=DamageType.force, time=Time.std_a,
    shape=Shape.circle, target_area='Self',
    effect='Caster telekinetically wields melee weapon at range, dealing extra MDAM on hit',
    prerequisites=(animate_weapon_2,)
)

mass_telekinesis_1 = Ability(
    name='Mass Telekinesis I', picture=AbilityPicture.huton,
    mp_cost=8, attacks=1, mdam='2d6+WIS',
    damage_type=DamageType.force, targets_mdef=True, max_range='10',
    shape=Shape.multi_point, target_area='[[WIS]] Objects < 200lb (Medium)',
    effect='Can telekinetically interact/(move 4DIS) object (or self) doing MDAM if thrown '
           'against a surface',
    prerequisites=(shell_2, vortex_3, shatter_1)
)

mass_telekinesis_2 = Ability(
    name='Mass Telekinesis II', picture=AbilityPicture.huton,
    mp_cost=15, attacks=1, mdam='2d8+2*WIS',
    damage_type=DamageType.force, targets_mdef=True, max_range='12+WIS',
    shape=Shape.multi_point, target_area='[[WIS]] Objects < 800lb (Large)',
    effect='Can telekinetically interact/(move 4DIS) object (or self) doing MDAM if thrown '
           'against a surface',
    prerequisites=(mass_telekinesis_1,)
)

mass_telekinesis_3 = Ability(
    name='Mass Telekinesis III', picture=AbilityPicture.huton,
    mp_cost=35, attacks=1, mdam='3d20+2*WIS',
    damage_type=DamageType.force, targets_mdef=True, max_range='20+WIS',
    shape=Shape.multi_point, target_area='[[WIS]] Objects < 800lb (Large)',
    effect='1 Object < 50,000lb (Huge, Colossal, or Structure)',
    prerequisites=(mass_telekinesis_2,)
)

# Ability slot.

master_telekinetic_1 = Ability(
    name='Master Telekinetic [Passive] I', picture=AbilityPicture.tempered_will,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='2*DAM to enemies hit with Reflect',
    prerequisites=(provoke_2, vortex_2, mass_barrier_2)
)

master_telekinetic_2 = Ability(
    name='Master Telekinetic [Passive] II', picture=AbilityPicture.tempered_will,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='+50% DIS, 2*DAM on Telekinesis',
    prerequisites=(master_telekinetic_1,)
)

master_telekinetic_3 = Ability(
    name='Master Telekinetic [Passive] III', picture=AbilityPicture.tempered_will,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='Barriers also add to MDEF',
    prerequisites=(master_telekinetic_2,)
)


class Paladin(Class):
    def __init__(self) -> None:
        super().__init__(
            name=self.__class__.__name__, hd=12, md=4, sd=2, speed=4, pdef=6, mdef=0.75,
            pred=1, mred=0, reg=0.75, vis=2, pac=1, mac=0.5, ath=4, ste=1, fort=4, apt=1,
            per=2, spe=2, starting_ap=4, use_melee_light=True, use_melee_medium=True,
            use_melee_heavy=True, use_light_armor=True, use_medium_armor=True,
            use_heavy_armor=True,
            abilities=(reflect_1, reflect_2, reflect_3,
                       telekinesis_1, telekinesis_2, telekinesis_3,
                       protect_1, protect_2, protect_3,
                       earth_breaker_1, earth_breaker_2, earth_breaker_3,
                       barrier_1, barrier_2, barrier_3,
                       shell_1, shell_2, shell_3,
                       vortex_1, vortex_2, vortex_3,
                       provoke_1, provoke_2, provoke_3,
                       shatter_1, shatter_2, shatter_3,
                       mass_barrier_1, mass_barrier_2, mass_barrier_3,
                       shockwave_1, shockwave_2, shockwave_3,
                       animate_weapon_1, animate_weapon_2, animate_weapon_3,
                       mass_telekinesis_1, mass_telekinesis_2, mass_telekinesis_3,
                       master_telekinetic_1, master_telekinetic_2, master_telekinetic_3))
