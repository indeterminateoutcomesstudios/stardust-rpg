from ..ability import Ability, AbilityPicture, DurationUnit, Time
from ..class_type import Class
from ..equipment import DamageType, Shape

invisibility_1 = Ability(
    name='Invisibility I', picture=AbilityPicture.hide,
    mp_cost=2, target_area='Self', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster becomes invisible and moves at ½SPEED.  Attacks while invisible have +1PAC',
)

invisibility_2 = Ability(
    name='Invisibility II', picture=AbilityPicture.hide,
    mp_cost=2, target_area='Self', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster becomes invisible and moves at 3/4SPEED.  Attacks while invisible have +2PAC',
    prerequisites=(invisibility_1,),
)

invisibility_3 = Ability(
    name='Invisibility III', picture=AbilityPicture.hide,
    mp_cost=2, target_area='Self', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster becomes invisible and moves at Full SPEED.  Attacks while invisible have +3PAC',
    prerequisites=(invisibility_2,),
)

blinding_ray_1 = Ability(
    name='Blinding Ray I', picture=AbilityPicture.demolish,
    mp_cost=2,
    attacks=1, targets_mdef=True, max_range='1',
    shape=Shape.line, target_area='4DIS Line',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Stream of light causes temporary blindness, staggering creatures',
)

blinding_ray_2 = Ability(
    name='Blinding Ray II', picture=AbilityPicture.demolish,
    mp_cost=2,
    attacks=1, targets_mdef=True, max_range='1',
    shape=Shape.line, target_area='[[4+WIS]]DIS Line',
    duration='2', duration_unit=DurationUnit.rnd,
    effect='Stream of light causes temporary blindness, staggering creatures',
    prerequisites=(blinding_ray_1,),
)

blinding_ray_3 = Ability(
    name='Blinding Ray III', picture=AbilityPicture.demolish,
    mp_cost=3,
    attacks=1, targets_mdef=True, max_range='1',
    shape=Shape.double_line, target_area='2 Wide x [[5+WIS]] Long Line',
    duration='2', duration_unit=DurationUnit.rnd,
    effect='Stream of light causes temporary blindness, staggering creatures',
    prerequisites=(blinding_ray_2,),
)

trap_1 = Ability(
    name='Trap I', picture=AbilityPicture.assassinate,
    mp_cost=2, time=Time.std_ab_a, attacks=1, mdam='1d8', damage_type=DamageType.piercing,
    targets_mdef=True, max_range='2',
    shape=Shape.square, target_area='[[WIS*WIS]]DIS square, 1 medium creature',
    duration='5', duration_unit=DurationUnit.rnd,
    effect='Deploys 1 maximum trap: Alarm: Sounds high pitch wale.  Trap lasts 1 hour.',
)

trap_2 = Ability(
    name='Trap II', picture=AbilityPicture.assassinate,
    mp_cost=6, time=Time.std_ab_a, attacks=1, mdam='1d12+WIS', damage_type=DamageType.piercing,
    targets_mdef=True, max_range='2',
    shape=Shape.square, target_area='[[WIS*WIS]]DIS square, 1 medium creature',
    duration='5+WIS', duration_unit=DurationUnit.rnd,
    effect='Deploys up to 2 traps: Snare: Immobilizes one creature.  Trap lasts 2 hours.',
    prerequisites=(trap_1,),
)

trap_3 = Ability(
    name='Trap III', picture=AbilityPicture.assassinate,
    mp_cost=10, time=Time.std_ab_a, attacks=1, mdam='1d20+2*WIS', damage_type=DamageType.piercing,
    targets_mdef=True, max_range='2',
    shape=Shape.square, target_area='[[WIS*WIS]]DIS square, 1 medium creature',
    duration='5+WIS', duration_unit=DurationUnit.rnd,
    effect='Deploys up to 3 traps: Snare: Stuns one creature. Trap lasts [[2+WIS]] hours',
    prerequisites=(trap_2,),
)

darkness_1 = Ability(
    name='Darkness I', picture=AbilityPicture.apocatastasis,
    mp_cost=2,
    max_range='2', shape=Shape.circle, target_area='2RAD',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Releases magical darkness. Only one darkness cloud allowed at a time',
)

darkness_2 = Ability(
    name='Darkness II', picture=AbilityPicture.apocatastasis,
    mp_cost=3,
    max_range='2', shape=Shape.circle, target_area='[[2+WIS]]RAD',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Releases magical darkness. Only one darkness cloud allowed at a time',
    prerequisites=(darkness_1,),
)

darkness_3 = Ability(
    name='Darkness III', picture=AbilityPicture.apocatastasis,
    mp_cost=4,
    max_range='2', shape=Shape.circle, target_area='[[3+2*WIS]]RAD',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Releases magical darkness. Only one darkness cloud allowed at a time',
    prerequisites=(darkness_2,),
)

spectre_arts_1 = Ability(
    name='Spectre Arts I', picture=AbilityPicture.aeolian_edge,
    mp_cost=0, target_area='Self',
    effect='[Passive] Night vision, +2VIS',
)

spectre_arts_2 = Ability(
    name='Spectre Arts II', picture=AbilityPicture.aeolian_edge,
    mp_cost=0, target_area='Self',
    effect='[Passive] Wall walk at ½SPEED',
    prerequisites=(spectre_arts_1,),
)

spectre_arts_3 = Ability(
    name='Spectre Arts III', picture=AbilityPicture.aeolian_edge,
    mp_cost=0, target_area='Self',
    effect='[Passive] Critical hits stagger for 1RND',
    prerequisites=(spectre_arts_2,),
)

# Tier 2.

mass_invisibility_1 = Ability(
    name='Mass Invisibility I', picture=AbilityPicture.hide,
    mp_cost=4,
    target_area='Self + [[1+WIS]] allies in [[2+WIS]]RAD', shape=Shape.circle,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster and allies becomes invisible and moves at ½SPEED. '
           'Attacks while invisible have +1PAC',
    prerequisites=(invisibility_3, darkness_2),
)

mass_invisibility_2 = Ability(
    name='Mass Invisibility II', picture=AbilityPicture.hide,
    mp_cost=5,
    target_area='Self + [[1+WIS]] allies in [[2+WIS]]RAD', shape=Shape.circle,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster and allies becomes invisible and moves at 3/4SPEED. '
           'Attacks while invisible have +2PAC',
    prerequisites=(mass_invisibility_1,),
)

mass_invisibility_3 = Ability(
    name='Mass Invisibility III', picture=AbilityPicture.hide,
    mp_cost=5,
    target_area='Self + [[1+WIS]] allies in [[3+WIS]]RAD', shape=Shape.circle,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster and allies becomes invisible and moves at Full SPEED. '
           'Attacks while invisible have +3PAC',
    prerequisites=(mass_invisibility_2,),
)

farsight_1 = Ability(
    name='Farsight I', picture=AbilityPicture.invigorate,
    mp_cost=2, target_area='Self', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster can see through 1DIS of material. +1VIS',
    prerequisites=(invisibility_2, blinding_ray_3,),
)

farsight_2 = Ability(
    name='Farsight II', picture=AbilityPicture.invigorate,
    mp_cost=3, target_area='Self', time=Time.free_a,
    max_range='1+WIS',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster can see through [[1+WIS]]DIS material. +[[1+WIS]]VIS',
    prerequisites=(farsight_1,),
)

farsight_3 = Ability(
    name='Farsight III', picture=AbilityPicture.invigorate,
    mp_cost=3, target_area='Self', time=Time.free_a,
    max_range='3+WIS',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster can see through [[3+WIS]]DIS material. +[[3+WIS]]VIS',
    prerequisites=(farsight_2,),
)

large_trap_1 = Ability(
    name='Large Trap I', picture=AbilityPicture.assassinate,
    mp_cost=3, time=Time.std_ab_a, attacks=1, mdam='2d8', damage_type=DamageType.piercing,
    targets_mdef=True, max_range='2',
    shape=Shape.square, target_area='[[WIS*WIS]]DIS square, 1 large creature',
    duration='5', duration_unit=DurationUnit.rnd,
    effect='Deploys 1 maximum trap: Alarm: Sounds high pitch wale.  Trap lasts 1 hour.',
    prerequisites=(trap_2, darkness_3,),
)

large_trap_2 = Ability(
    name='Large Trap II', picture=AbilityPicture.assassinate,
    mp_cost=9, time=Time.std_ab_a, attacks=1, mdam='2d12+WIS', damage_type=DamageType.piercing,
    targets_mdef=True, max_range='2',
    shape=Shape.square, target_area='[[WIS*WIS]]DIS square, 1 large creature',
    duration='5', duration_unit=DurationUnit.rnd,
    effect='Deploys up to 2 traps: Snare: Immobilizes one creature. Trap lasts 2 hours.',
    prerequisites=(large_trap_1,),
)

large_trap_3 = Ability(
    name='Large Trap III', picture=AbilityPicture.assassinate,
    mp_cost=15, time=Time.std_ab_a, attacks=1, mdam='2d20+2*WIS', damage_type=DamageType.piercing,
    targets_mdef=True, max_range='2',
    shape=Shape.square, target_area='[[WIS*WIS]]DIS square, 1 large creature',
    duration='5', duration_unit=DurationUnit.rnd,
    effect='Deploys up to 3 traps: Snare: Stuns one creature. Trap lasts 2+WIS hours.',
    prerequisites=(large_trap_2,),
)

sleep_powder_1 = Ability(
    name='Sleep Powder I', picture=AbilityPicture.sleep,
    mp_cost=2, attacks=1, targets_mdef=True, max_range='2',
    shape=Shape.circle, target_area='1RAD',
    duration='WIS', duration_unit=DurationUnit.rnd,
    effect='Causes enemies to briefly fall into sleep',
    prerequisites=(trap_2, darkness_3,),
)

sleep_powder_2 = Ability(
    name='Sleep Powder II', picture=AbilityPicture.sleep,
    mp_cost=3, attacks=1, targets_mdef=True, max_range='2+WIS',
    shape=Shape.circle, target_area='1RAD',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Causes enemies to briefly fall into sleep',
    prerequisites=(sleep_powder_1,),
)

sleep_powder_3 = Ability(
    name='Sleep Powder III', picture=AbilityPicture.sleep,
    mp_cost=4, attacks=1, targets_mdef=True, max_range='3+WIS',
    shape=Shape.circle, target_area='1RAD',
    duration='5+WIS', duration_unit=DurationUnit.rnd,
    effect='Causes enemies to briefly fall into sleep',
    prerequisites=(sleep_powder_2,),
)

teamwork_1 = Ability(
    name='Teamwork I', picture=AbilityPicture.trick_attack,
    mp_cost=1, target_area='Self + 1 flanking ally', time=Time.free_a,
    max_range='3', shape=Shape.point,
    duration_unit=DurationUnit.instant,
    effect='+1PRED',
    prerequisites=(blinding_ray_2, spectre_arts_3,),
)

teamwork_2 = Ability(
    name='Teamwork II', picture=AbilityPicture.trick_attack,
    mp_cost=2, target_area='Self + 1 flanking ally', time=Time.free_a,
    max_range='3', shape=Shape.point,
    duration_unit=DurationUnit.instant,
    effect='+[[1+WIS]]PDAM on physical attacks',
    prerequisites=(teamwork_1,),
)

teamwork_3 = Ability(
    name='Teamwork III', picture=AbilityPicture.trick_attack,
    mp_cost=2, target_area='Self + 1 flanking ally', time=Time.free_a,
    max_range='3', shape=Shape.point,
    duration_unit=DurationUnit.instant,
    effect='+[[2+WIS]]PDAM on physical attacks, +2PRED',
    prerequisites=(teamwork_2,),
)

# Tier 3.

colossal_invisibility_1 = Ability(
    name='Colossal Invisibility I', picture=AbilityPicture.hide,
    mp_cost=7,
    target_area='Self + objects/creatures within 6RAD', shape=Shape.circle,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster and objects and creatures around him become invisible',
    prerequisites=(mass_invisibility_2, large_trap_2),
)

colossal_invisibility_2 = Ability(
    name='Colossal Invisibility II', picture=AbilityPicture.hide,
    mp_cost=8,
    target_area='Self + objects/creatures within [[8+WIS]]RAD', shape=Shape.circle,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster and objects and creatures around him become invisible',
    prerequisites=(colossal_invisibility_1,),
)

colossal_invisibility_3 = Ability(
    name='Colossal Invisibility III', picture=AbilityPicture.hide,
    mp_cost=8,
    target_area='Self + objects/creatures within [[8+2*WIS]]RAD', shape=Shape.circle,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster and objects and creatures around him become invisible',
    prerequisites=(colossal_invisibility_2,),
)

star_fire_1 = Ability(
    name='Star Fire I', picture=AbilityPicture.hallowed_ground,
    mp_cost=8, attacks=1, mdam='2d8', damage_type=DamageType.fire,
    targets_mdef=True, max_range='4',
    shape=Shape.circle, target_area='4RAD',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Exploding sphere of sunlight temporarily blinds, burns, and staggers creatures.',
    prerequisites=(farsight_3, sleep_powder_3),
)

star_fire_2 = Ability(
    name='Star Fire II', picture=AbilityPicture.hallowed_ground,
    mp_cost=10, attacks=1, mdam='2d12+WIS', damage_type=DamageType.fire,
    targets_mdef=True, max_range='4+WIS',
    shape=Shape.circle, target_area='[[4+WIS]]RAD',
    duration='1+WIS', duration_unit=DurationUnit.rnd,
    effect='Exploding sphere of sunlight temporarily blinds, burns, and staggers creatures.',
    prerequisites=(star_fire_1,),
)

star_fire_3 = Ability(
    name='Star Fire III', picture=AbilityPicture.hallowed_ground,
    mp_cost=14, attacks=1, mdam='2d20+2*WIS', damage_type=DamageType.fire,
    targets_mdef=True, max_range='4+WIS',
    shape=Shape.circle, target_area='[[4+WIS]]RAD',
    duration='2+WIS', duration_unit=DurationUnit.rnd,
    effect='Exploding sphere of sunlight temporarily blinds, burns, and staggers creatures.',
    prerequisites=(star_fire_2,),
)

# Blackout - causes fear.

dodge_1 = Ability(
    name='Dodge I', picture=AbilityPicture.perfect_dodge,
    mp_cost=4, target_area='Self', time=Time.free_a,
    effect='[Counter] If a single melee attack hits caster, can choose to ignore 1/2 PDAM.',
    prerequisites=(farsight_2, teamwork_3,),
)

dodge_2 = Ability(
    name='Dodge II', picture=AbilityPicture.perfect_dodge,
    mp_cost=5, target_area='Self', time=Time.free_a,
    effect='[Counter] If a single melee or range attack hits caster, can choose to ignore 3/4 '
           'PDAM.',
    prerequisites=(dodge_1,),
)

dodge_3 = Ability(
    name='Dodge III', picture=AbilityPicture.perfect_dodge,
    mp_cost=6, target_area='Self', time=Time.free_a,
    effect='[Counter] If a single melee or range attack hits caster, can choose to ignore Full '
           'PDAM.',
    prerequisites=(dodge_2,),
)

phantom_1 = Ability(
    name='Phantom I', picture=AbilityPicture.ninjutsu,
    mp_cost=0, target_area='Self',
    effect='[Passive] +3RAD on invisibility abilities.',
    prerequisites=(mass_invisibility_3, large_trap_2, teamwork_2,)
)

phantom_2 = Ability(
    name='Phantom II', picture=AbilityPicture.ninjutsu,
    mp_cost=0, target_area='Self',
    effect='[Passive] Critical hits stun for 1RND.',
    prerequisites=(phantom_1,),
    )

phantom_3 = Ability(
    name='Phantom III', picture=AbilityPicture.ninjutsu,
    mp_cost=0, target_area='Self',
    effect='[Passive] Successful REG makes caster invisible for 1RND.',
    prerequisites=(phantom_2,),
)


class Spectre(Class):
    def __init__(self) -> None:
        super().__init__(
            name=self.__class__.__name__, hd=8, md=6, sd=4, speed=5, pdef=6, mdef=0.5,
            pred=0, mred=0, reg=0.5, vis=3, pac=0.75, mac=0.5, ath=4, ste=4, fort=1, apt=2,
            per=2, spe=1, starting_ap=5, use_melee_light=True, use_melee_medium=True,
            use_ranged_light=True, use_ranged_medium=True,
            use_light_armor=True, use_medium_armor=True,
            abilities=(invisibility_1, invisibility_2, invisibility_3,
                       blinding_ray_1, blinding_ray_2, blinding_ray_3,
                       trap_1, trap_2, trap_3,
                       darkness_1, darkness_2, darkness_3,
                       spectre_arts_1, spectre_arts_2, spectre_arts_3,
                       mass_invisibility_1, mass_invisibility_2, mass_invisibility_3,
                       farsight_1, farsight_2, farsight_3,
                       large_trap_1, large_trap_2, large_trap_3,
                       sleep_powder_1, sleep_powder_2, sleep_powder_3,
                       teamwork_1, teamwork_2, teamwork_3,
                       colossal_invisibility_1, colossal_invisibility_2, colossal_invisibility_3,
                       star_fire_1, star_fire_2, star_fire_3,
                       dodge_1, dodge_2, dodge_3,
                       phantom_1, phantom_2, phantom_3,))
