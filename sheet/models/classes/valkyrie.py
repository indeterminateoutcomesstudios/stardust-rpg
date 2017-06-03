from ..ability import Ability, AbilityPicture, DurationUnit, Time
from ..class_type import Class
from ..equipment import DamageType, Shape

# Tier 1.
fly_1 = Ability(
    name='Fly I', picture=AbilityPicture.huton,
    mp_cost=2, target_area='Self', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Fly at ½ SPEED.'
)

fly_2 = Ability(
    name='Fly II', picture=AbilityPicture.huton,
    mp_cost=2, target_area='Self', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Fly at ¾ SPEED. +1PRED.',
    prerequisites=(fly_1,),
)

fly_3 = Ability(
    name='Fly III', picture=AbilityPicture.huton,
    mp_cost=2, target_area='Self', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Fly at Full SPEED. +1PRED +1MRED.',
    prerequisites=(fly_2,),
)

blink_1 = Ability(
    name='Blink I', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=1, target_area='Self', time=Time.free_a,
    effect='Teleport 3DIS within line of sight. Can be casted once per RND.'
)

blink_2 = Ability(
    name='Blink II', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=2, target_area='Self', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Teleport [[4+WIS]]DIS within line of sight. Can be casted once per RND.',
    prerequisites=(blink_1,),
)

blink_3 = Ability(
    name='Blink III', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=4, target_area='Self', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Teleport [[5+2*WIS]]DIS within line of sight. Can be casted once per RND.',
    prerequisites=(blink_2,),
)

gale_1 = Ability(
    name='Gale I', picture=AbilityPicture.aero,
    mp_cost=2, attacks=1, mdam='1d4',
    damage_type=DamageType.force, targets_mdef=True, max_range='3',
    shape=Shape.double_line, target_area='5DIS long, 2DIS wide line', time=Time.ab_a,
    effect='-1SPEED movement opposing direction of wind.'
)

gale_2 = Ability(
    name='Gale II', picture=AbilityPicture.aero,
    mp_cost=3, attacks=1, mdam='1d4 + WIS',
    damage_type=DamageType.force, targets_mdef=True, max_range='3+WIS',
    shape=Shape.double_line, target_area='[[5+WIS]]DIS long, 2DIS wide line', time=Time.ab_a,
    effect='-[[1+WIS]]SPEED movement opposing direction of wind.',
    prerequisites=(gale_1,),
)

gale_3 = Ability(
    name='Gale III', picture=AbilityPicture.aero,
    mp_cost=5, attacks=1, mdam='1d6 + WIS',
    damage_type=DamageType.force, targets_mdef=True, max_range='5+WIS',
    shape=Shape.double_line, target_area='[[7+WIS]]DIS long, 4DIS wide line', time=Time.ab_a,
    effect='-[[2+WIS]]SPEED movement opposing direction of wind.',
    prerequisites=(gale_2,),
)

piercing_shot_1 = Ability(
    name='Piercing Shot I', picture=AbilityPicture.blood_letter,
    mp_cost=3, target_area='[[2+WIS]]DIS Line', shape=Shape.line, time=Time.std_ab_a,
    effect='Next ranged attack ignores PRED and pierces through enemies.'
)

piercing_shot_2 = Ability(
    name='Piercing Shot II', picture=AbilityPicture.blood_letter,
    mp_cost=4, target_area='[[6+WIS]]DIS Line', shape=Shape.line, time=Time.std_ab_a,
    effect='Next ranged attack ignores PRED and pierces through enemies.',
    prerequisites=(piercing_shot_1,),
)

piercing_shot_3 = Ability(
    name='Piercing Shot III', picture=AbilityPicture.blood_letter,
    mp_cost=5, target_area='[[6+2*WIS]]DIS Line', shape=Shape.line, time=Time.std_ab_a,
    effect='Next ranged attack ignores PRED and pierces through enemies.',
    prerequisites=(piercing_shot_2,),
)

wind_stride_1 = Ability(
    name='Wind Stride I', picture=AbilityPicture.chaos_thrust,
    mp_cost=2, target_area='Self + Allies in 4DIS', shape=Shape.circle,
    time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='+1SPEED. Can be cast once per RND.'
)

wind_stride_2 = Ability(
    name='Wind Stride II', picture=AbilityPicture.chaos_thrust,
    mp_cost=4, target_area='Self + Allies in [[4+WIS]]DIS', shape=Shape.circle,
    time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='+[[1+WIS]]SPEED. Can be cast once per RND.',
    prerequisites=(wind_stride_1,),
)

wind_stride_3 = Ability(
    name='Wind Stride III', picture=AbilityPicture.chaos_thrust,
    mp_cost=5, target_area='Self + Allies in [[6+WIS]]DIS', shape=Shape.circle,
    time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='+[[2+WIS]]SPEED. Can be cast once per RND.',
    prerequisites=(wind_stride_2,),
)

# Tier 2.

mass_fly_1 = Ability(
    name='Mass Fly I', picture=AbilityPicture.huton,
    mp_cost=3, target_area='Self + 1 medium creature', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Fly at ½ SPEED.',
    prerequisites=(),
)

mass_fly_2 = Ability(
    name='Mass Fly II', picture=AbilityPicture.huton,
    mp_cost=3, target_area='Self + 1 medium creature', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Fly at ¾ SPEED. +1PRED.',
    prerequisites=(mass_fly_1,),
)

mass_fly_3 = Ability(
    name='Mass Fly III', picture=AbilityPicture.huton,
    mp_cost=3, target_area='Self + 1 large or 2 medium creatures', time=Time.free_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Fly at Full SPEED. +1PRED +1MRED.',
    prerequisites=(mass_fly_2,),
)

mass_blink_1 = Ability(
    name='Mass Blink I', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=2, target_area='Self + 1 up to medium creature', time=Time.ab_a,
    targets_mdef=True, attacks=1,
    effect='Teleports 3DIS within line of sight. -1MRED to enemies.',
    prerequisites=(),
)

mass_blink_2 = Ability(
    name='Mass Blink II', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=3, target_area='Self + 1 up to medium creature', time=Time.ab_a,
    targets_mdef=True, attacks=1,
    effect='Teleports [[4+WIS]]DIS within line of sight. -1MRED to enemies.',
    prerequisites=(mass_blink_1,),
)

mass_blink_3 = Ability(
    name='Mass Blink III', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=4, target_area='Self + 1 up to large creature', time=Time.ab_a,
    targets_mdef=True, attacks=1,
    effect='Teleports [[5+2*WIS]]DIS within line of sight. -[[1+WIS]]MRED to enemies. '
           'Caster has option to return to original location.',
    prerequisites=(mass_blink_2,),
)

counter_blink_1 = Ability(
    name='Counter Blink I', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='Can use Blink ability if target of melee attack to attempt to avoid AOE for +1MP.'
)

counter_blink_2 = Ability(
    name='Counter Blink II', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='Can use Blink ability if target of ranged attack to attempt to avoid AOE for +1MP.',
    prerequisites=(counter_blink_1,),
)

counter_blink_3 = Ability(
    name='Counter Blink III', picture=AbilityPicture.aetherial_manipulation,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='Can use Blink ability if target of magic attack to attempt to avoid AOE for +2MP.',
    prerequisites=(counter_blink_1,),
)

cyclone_1 = Ability(
    name='Cyclone I', picture=AbilityPicture.bio_2,
    mp_cost=4, attacks=1, mdam='1d4',
    damage_type=DamageType.force, targets_mdef=True, time=Time.ab_a, max_range='6',
    shape=Shape.circle, target_area='2RAD',
    effect='Targets are moved 1DIS of caster\'s choosing',
)

cyclone_2 = Ability(
    name='Cyclone II', picture=AbilityPicture.bio_2,
    mp_cost=4, attacks=1, mdam='1d6',
    damage_type=DamageType.force, targets_mdef=True, time=Time.ab_a, max_range='7',
    shape=Shape.circle, target_area='[[2+WIS]]RAD',
    effect='Targets are moved 1DIS of caster\'s choosing',
    prerequisites=(cyclone_1,),
)

cyclone_3 = Ability(
    name='Cyclone III', picture=AbilityPicture.bio_2,
    mp_cost=4, attacks=1, mdam='1d8',
    damage_type=DamageType.force, targets_mdef=True, time=Time.ab_a, max_range='8',
    shape=Shape.circle, target_area='[[2+WIS]]RAD',
    effect='Targets are moved 2DIS of caster\'s choosing',
    prerequisites=(cyclone_2,),
)

# Tier 3.

# Tornado

sky_watch_1 = Ability(
    name='Sky Watch [Passive] I', picture=AbilityPicture.shoulder_tackle,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='Absorb 1MDAM into MP while flying',
    prerequisites=(),
)

sky_watch_2 = Ability(
    name='Sky Watch [Passive] II', picture=AbilityPicture.shoulder_tackle,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='Can use Mass Blink if ally within range is target of melee attack or enemy who is '
           'targeting ally is within 1DIS to move either such that AOE no longer hits.',
    prerequisites=(sky_watch_1,),
)

sky_watch_3 = Ability(
    name='Sky Watch [Passive] III', picture=AbilityPicture.shoulder_tackle,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='Can perform two Blinks per RND.',
    prerequisites=(sky_watch_2,),
)


class Valkyrie(Class):
    def __init__(self) -> None:
        super().__init__(
            name=self.__class__.__name__, hd=10, md=6, sd=2, speed=5, pdef=6, mdef=1,
            pred=0, mred=0, reg=1, vis=3, pac=0.5, mac=0.75, ath=2, ste=2, fort=1, apt=1,
            per=4, spe=4, starting_ap=4, use_melee_light=True, use_melee_medium=True,
            use_ranged_light=True, use_ranged_medium=True, use_ranged_heavy=True,
            use_light_armor=True,
            abilities=(
                fly_1, fly_2, fly_3, blink_1, blink_2, blink_3, gale_1, gale_2, gale_3,
                piercing_shot_1, piercing_shot_2, piercing_shot_3, wind_stride_1, wind_stride_2,
                wind_stride_3, mass_fly_1, mass_fly_2, mass_fly_3, mass_blink_1, mass_blink_2,
                mass_blink_3, counter_blink_1, counter_blink_2, counter_blink_3, cyclone_1,
                cyclone_2, cyclone_3, sky_watch_1, sky_watch_2, sky_watch_3
            ))
