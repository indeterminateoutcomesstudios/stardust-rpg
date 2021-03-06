from ..ability import Ability, AbilityPicture, DurationUnit, Time
from ..class_type import Class
from ..equipment import Shape

# Tier 1.
time_warp_1 = Ability(
    name='Time Warp I', picture=AbilityPicture.swift_song,
    mp_cost=2, target_area='Self', time=Time.bon_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Double SPEED on caster.'
)

time_warp_2 = Ability(
    name='Time Warp II', picture=AbilityPicture.swift_song,
    mp_cost=3, target_area='Self', time=Time.bon_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='+1AbA or BoA on caster.',
    prerequisites=(time_warp_1,)
)

time_warp_3 = Ability(
    name='Time Warp III', picture=AbilityPicture.swift_song,
    mp_cost=4, target_area='Self', time=Time.bon_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Double SPEED and +1AbA or BoA on caster.',
    prerequisites=(time_warp_2,)
)

slow_1 = Ability(
    name='Slow I', picture=AbilityPicture.lethargy,
    mp_cost=1, attacks=1, targets_mdef=True,
    max_range='8', shape=Shape.circle, target_area='1RAD', time=Time.ab_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Slows time in an area and enemies gets -3SPEED'
)

slow_2 = Ability(
    name='Slow II', picture=AbilityPicture.lethargy,
    mp_cost=2, attacks=1, targets_mdef=True,
    max_range='8', shape=Shape.circle, target_area='1RAD', time=Time.ab_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Slows time in an area and immobilizes enemies',
    prerequisites=(slow_1,)
)

slow_3 = Ability(
    name='Slow III', picture=AbilityPicture.lethargy,
    mp_cost=2, attacks=1, targets_mdef=True,
    max_range='8', shape=Shape.circle, target_area='1RAD', time=Time.ab_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Slows time in an area and either staggers or silences enemies',
    prerequisites=(slow_2,)
)

rebound_1 = Ability(
    name='Rebound I', picture=AbilityPicture.feint,
    mp_cost=0, target_area='Self', time=Time.re_a,
    effect='[Counter] Caster bends time in order to cast Slow after target of melee attack. '
           'MP cost = ability cast.'
)

rebound_2 = Ability(
    name='Rebound II', picture=AbilityPicture.feint,
    mp_cost=0, target_area='Self', time=Time.re_a,
    effect='[Counter] Caster bends time in order to cast cast Cure after target of melee attack. '
           'MP cost = ability cast.',
    prerequisites=(rebound_1,)
)

rebound_3 = Ability(
    name='Rebound III', picture=AbilityPicture.feint,
    mp_cost=0, target_area='Self', time=Time.re_a,
    effect='[Counter] Caster bends time in order to cast cast Stop after target of melee attack. '
           'MP cost = ability cast.',
    prerequisites=(rebound_2,)
)

rapid_regen_1 = Ability(
    name='Rapid Regen I', picture=AbilityPicture.leeches,
    mp_cost=0, target_area='Self', time=Time.std_ab_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Automatic success on REG, 2x MP per Regen',
)

rapid_regen_2 = Ability(
    name='Rapid Regen II', picture=AbilityPicture.leeches,
    mp_cost=0, target_area='Self + allies in [[1+WIS]]RAD', time=Time.full_a, shape=Shape.circle,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Automatic success on REG, 2x MP per Regen',
    prerequisites=(rapid_regen_1,)
)

rapid_regen_3 = Ability(
    name='Rapid Regen III', picture=AbilityPicture.leeches,
    mp_cost=0, target_area='Self + allies in [[3+WIS]]RAD', time=Time.full_a, shape=Shape.circle,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Automatic success on REG, 2x + WIS MP per Regen',
    prerequisites=(rapid_regen_2,)
)

cure_1 = Ability(
    name='Cure I', picture=AbilityPicture.cure,
    mp_cost=1, target_area='1 ally', max_range='2',
    effect='+[[1d4]]HP',
)

cure_2 = Ability(
    name='Cure II', picture=AbilityPicture.cure,
    mp_cost=2, target_area='1 ally', max_range='2',
    effect='+[[1d6+WIS]]HP',
    prerequisites=(cure_1,)
)

cure_3 = Ability(
    name='Cure III', picture=AbilityPicture.cure,
    mp_cost=3, target_area='1 ally', max_range='2',
    effect='+[[1d8+2*WIS]]HP',
    prerequisites=(cure_2,)
)

# Tier 2.
mass_time_warp_1 = Ability(
    name='Mass Time Warp I', picture=AbilityPicture.swift_cast,
    mp_cost=3, target_area='Self + allies in [[4+WIS]]RAD', time=Time.bon_a, max_range='6',
    shape=Shape.circle, duration='1', duration_unit=DurationUnit.rnd,
    effect='Double SPEED on affected allies.',
    prerequisites=(time_warp_3, slow_2)
)

mass_time_warp_2 = Ability(
    name='Mass Time Warp II', picture=AbilityPicture.swift_cast,
    mp_cost=6, target_area='Self + allies in [[4+WIS]]RAD', time=Time.bon_a, max_range='6',
    shape=Shape.circle, duration='1', duration_unit=DurationUnit.rnd,
    effect='+1AbA or BoA on caster.',
    prerequisites=(mass_time_warp_1,)
)

mass_time_warp_3 = Ability(
    name='Mass Time Warp III', picture=AbilityPicture.swift_cast,
    mp_cost=7, target_area='Self + allies in [[4+WIS]]RAD', time=Time.bon_a, max_range='6',
    shape=Shape.circle, duration='1', duration_unit=DurationUnit.rnd,
    effect='Double SPEED and +1AbA or BoA on affected allies.',
    prerequisites=(mass_time_warp_2,)
)

stop_1 = Ability(
    name='Stop I', picture=AbilityPicture.shroud_of_saints,
    mp_cost=6, attacks=1, targets_mdef=True,
    shape=Shape.circle, target_area='Up to [[WIS]]RAD', time=Time.full_a,
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Causes a bubble of time to completely stop for a short amount of time. '
           'Must continue to cast Stop or effect ends. '
           'REG is inhibited for all creatures who are not stopped.',
    prerequisites=(time_warp_3, slow_3)
)

stop_2 = Ability(
    name='Stop II', picture=AbilityPicture.shroud_of_saints,
    mp_cost=10, attacks=1, targets_mdef=True,
    shape=Shape.circle, target_area='Up to [[2+WIS]]RAD', time=Time.full_a,
    duration='6', duration_unit=DurationUnit.rnd,
    effect='Causes a bubble of time to completely stop for a short amount of time. '
           'Must continue to cast Stop or effect ends. '
           'Can reverse the polarity of stopped time (inside/out). '
           'REG is inhibited for all creatures who are not stopped.',
    prerequisites=(stop_1,)
)

stop_3 = Ability(
    name='Stop III', picture=AbilityPicture.shroud_of_saints,
    mp_cost=18, attacks=1, targets_mdef=True, max_range='2+WIS',
    shape=Shape.circle, target_area='Up to [[2+WIS]]RAD', time=Time.full_a,
    duration='10', duration_unit=DurationUnit.rnd,
    effect='Causes a bubble of time to completely stop for a short amount of time. '
           'Must continue to cast Stop or effect ends. '
           'Can reverse the polarity of stopped time (inside/out). '
           'REG is inhibited for all creatures who are not stopped.',
    prerequisites=(stop_2,)
)

destiny_1 = Ability(
    name='Destiny I', picture=AbilityPicture.tri_disaster,
    mp_cost=6, target_area='2RAD', time=Time.std_ab_a,
    mdam='3d6', attacks=1, targets_mdef=True, shape=Shape.circle,
    effect='Tears fabric of time 1RND in the future causing damage at the beginning of caster\'s '
           'next turn.',
    prerequisites=(rebound_2,)
)

destiny_2 = Ability(
    name='Destiny II', picture=AbilityPicture.tri_disaster,
    mp_cost=10, target_area='2RAD', time=Time.std_ab_a,
    mdam='2d12+WIS', attacks=1, targets_mdef=True, shape=Shape.circle,
    effect='Tears fabric of time 1RND in the future causing damage at the beginning of caster\'s '
           'next turn.',
    prerequisites=(destiny_1,)
)

destiny_3 = Ability(
    name='Destiny III', picture=AbilityPicture.tri_disaster,
    mp_cost=12, target_area='3RAD', time=Time.std_ab_a,
    mdam='2d12+2*WIS', attacks=1, targets_mdef=True, shape=Shape.circle,
    effect='Tears fabric of time 1RND in the future causing damage at the beginning of caster\'s '
           'next turn.',
    prerequisites=(destiny_2,)
)

healing_wind_1 = Ability(
    name='Healing Wind I', picture=AbilityPicture.cure_2,
    mp_cost=2, target_area='Self + allies in [[4+WIS]]RAD', shape=Shape.circle,
    effect='Heals allies +[[1d4]]HP',
    prerequisites=(rapid_regen_2, cure_3)
)

healing_wind_2 = Ability(
    name='Healing Wind II', picture=AbilityPicture.cure_2,
    mp_cost=4, target_area='Self + allies in [[4+WIS]]RAD', shape=Shape.circle,
    effect='Heals allies +[[1d6+WIS]]HP',
    prerequisites=(healing_wind_1,)
)

healing_wind_3 = Ability(
    name='Healing Wind III', picture=AbilityPicture.cure_2,
    mp_cost=6, target_area='Self + allies in [[4+WIS]]RAD', shape=Shape.circle,
    effect='Heals allies +[[1d8+2*WIS]]HP',
    prerequisites=(healing_wind_2,)
)

esuna_1 = Ability(
    name='Esuna I', picture=AbilityPicture.esuna,
    mp_cost=1, target_area='Allies in [[1+WIS]]RAD', shape=Shape.circle, max_range='4',
    effect='Removes status effects',
    prerequisites=(rapid_regen_3, cure_2)
)

esuna_2 = Ability(
    name='Esuna II', picture=AbilityPicture.esuna,
    mp_cost=2, target_area='Allies in [[1+WIS]]RAD', shape=Shape.circle, max_range='4',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Removes status, protects from status effects for duration',
    prerequisites=(esuna_1,)
)

esuna_3 = Ability(
    name='Esuna III', picture=AbilityPicture.esuna,
    mp_cost=3, target_area='Allies in [[1+WIS]]RAD', shape=Shape.circle, max_range='4',
    effect='Raises KO\'d allies to [[d8+2*WIS]]HP',
    prerequisites=(esuna_2,)
)

# Tier 3.
reset_1 = Ability(
    name='Reset I', picture=AbilityPicture.repelling_shot,
    mp_cost=8, target_area='Self or 1 ally', time=Time.bon_a, max_range='1',
    effect='Undo a MovA or Skill Check. Can be cast during ally\'s turn, once per instance.',
    prerequisites=(mass_time_warp_1, stop_2)
)

reset_2 = Ability(
    name='Reset II', picture=AbilityPicture.repelling_shot,
    mp_cost=10, target_area='Self or 1 ally', time=Time.bon_a, max_range='1',
    effect='Undo a StdA or AbA. Can be cast during ally\'s turn, once per instance. '
           'Does not refund MP cost of reset abilities.',
    prerequisites=(reset_1,)
)

reset_3 = Ability(
    name='Reset III', picture=AbilityPicture.repelling_shot,
    mp_cost=12, target_area='Self or 1 ally', time=Time.bon_a, max_range='1',
    effect='Undo FullA. Can be cast during ally\'s turn, once per instance.'
           'Does not refund MP cost of reset abilities.',
    prerequisites=(reset_2,)
)

decay_1 = Ability(
    name='Decay I', picture=AbilityPicture.miserys_end,
    mp_cost=5, attacks=1, targets_mdef=True, max_range='4',
    shape=Shape.point, target_area='1 creature',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Hyper accelerates time around the targets armor, causing -3PRED, -3MRED',
    prerequisites=(mass_time_warp_2, destiny_2)
)

decay_2 = Ability(
    name='Decay II', picture=AbilityPicture.miserys_end,
    mp_cost=7, attacks=1, targets_mdef=True, max_range='4+WIS',
    shape=Shape.circle, target_area='1 creature',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Hyper accelerates time around the targets armor, causing -4PRED, -4MRED',
    prerequisites=(decay_1,)
)

decay_3 = Ability(
    name='Decay III', picture=AbilityPicture.miserys_end,
    mp_cost=12, attacks=1, targets_mdef=True, max_range='4+WIS',
    shape=Shape.circle, target_area='1 creature',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Hyper accelerates time around the targets armor, causing -[[4+WIS]]PRED, '
           '-[[4+WIS]]MRED',
    prerequisites=(decay_2,)
)

time_cloud_1 = Ability(
    name='Time Cloud I', picture=AbilityPicture.shadow_bind,
    mp_cost=12, target_area='Self + allies in [[WIS]]RAD', time=Time.std_ab_a, shape=Shape.circle,
    effect='Bends time in a certain area to heal allies +[[1d8+2*WIS]]HP. '
           'Only one Time Cloud can exist at once',
    prerequisites=(destiny_1, healing_wind_2, esuna_1)
)

time_cloud_2 = Ability(
    name='Time Cloud II', picture=AbilityPicture.shadow_bind,
    mp_cost=10, target_area='Self + allies in [[WIS]]RAD', time=Time.std_ab_a, shape=Shape.circle,
    effect='Cloud regenerates +[[1d4+WIS]]MP. Only one Time Cloud can exist at once',
    prerequisites=(time_cloud_1,)
)

time_cloud_3 = Ability(
    name='Time Cloud III', picture=AbilityPicture.shadow_bind,
    mp_cost=6, target_area='Self + allies in [[WIS]]RAD', time=Time.std_ab_a, shape=Shape.circle,
    effect='Cloud causes -1MP ability cost. Only one Time Cloud can exist at once',
    prerequisites=(time_cloud_1,)
)

curaga_1 = Ability(
    name='Curaga I', picture=AbilityPicture.cure_3,
    mp_cost=5, target_area='1 ally', max_range='6',
    effect='Heals ally [[2d8+2*WIS]]HP',
    prerequisites=(healing_wind_2, esuna_2)
)

curaga_2 = Ability(
    name='Curaga II', picture=AbilityPicture.cure_3,
    mp_cost=8, target_area='1 ally', max_range='6',
    effect='Heals ally +[[2d10+3*WIS]]HP',
    prerequisites=(curaga_1,)
)

curaga_3 = Ability(
    name='Curaga III', picture=AbilityPicture.cure_3,
    mp_cost=10, target_area='1 ally', max_range='6',
    effect='Heals ally +[[2d20+4*WIS]]HP',
    prerequisites=(curaga_2,)
)

time_lord_1 = Ability(
    name='Time Lord I', picture=AbilityPicture.presence_of_mind,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='Passive: +2RAD to all abilities',
    prerequisites=(mass_time_warp_2, stop_2, healing_wind_2)
)

time_lord_2 = Ability(
    name='Time Lord II', picture=AbilityPicture.presence_of_mind,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='Passive: +50% to all healing',
    prerequisites=(time_lord_1,)
)

time_lord_3 = Ability(
    name='Time Lord III', picture=AbilityPicture.presence_of_mind,
    mp_cost=0, target_area='Self', time=Time.free_a,
    effect='Passive: Time Warp allows +2AbA',
    prerequisites=(time_cloud_2,)
)


class Templar(Class):
    def __init__(self) -> None:
        super().__init__(
            name=self.__class__.__name__, hd=10, md=6, sd=4, speed=5, pdef=5, mdef=1,
            pred=0, mred=0, reg=1, vis=2, pac=0.5, mac=0.75, ath=2, ste=4, fort=2, apt=2,
            per=1, spe=4, starting_ap=4, use_melee_light=True, use_melee_medium=True,
            use_ranged_light=True, use_magic_light=True, use_magic_medium=True,
            use_light_armor=True, use_medium_armor=True,
            abilities=(time_warp_1, time_warp_2, time_warp_3,
                       slow_1, slow_2, slow_3,
                       rebound_1, rebound_2, rebound_3,
                       rapid_regen_1, rapid_regen_2, rapid_regen_3,
                       cure_1, cure_2, cure_3,
                       mass_time_warp_1, mass_time_warp_2, mass_time_warp_3,
                       stop_1, stop_2, stop_3,
                       destiny_1, destiny_2, destiny_3,
                       healing_wind_1, healing_wind_2, healing_wind_3,
                       esuna_1, esuna_2, esuna_3,
                       reset_1, reset_2, reset_3,
                       decay_1, decay_2, decay_3,
                       time_cloud_1, time_cloud_2, time_cloud_3,
                       curaga_1, curaga_2, curaga_3,
                       time_lord_1, time_lord_2, time_lord_3))
