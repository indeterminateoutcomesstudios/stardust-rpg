from ..ability import Ability, AbilityPicture, DurationUnit, Time
from ..class_type import Class
from ..equipment import DamageType, Shape

taunt_1 = Ability(
    name='Taunt I', picture=AbilityPicture.provoke,
    mp_cost=1, time=Time.bon_a, attacks=1,
    targets_mdef=True, max_range='4',
    shape=Shape.point, target_area='1 creature',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Compels creature to attack caster',
)

taunt_2 = Ability(
    name='Taunt II', picture=AbilityPicture.provoke,
    mp_cost=2, time=Time.bon_a, attacks=1,
    targets_mdef=True, max_range='4+WIS',
    shape=Shape.multi_point, target_area='Up to [[1+WIS]] creatures',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Compels creature to attack caster',
    prerequisites=(taunt_1,),
)

taunt_3 = Ability(
    name='Taunt III', picture=AbilityPicture.provoke,
    mp_cost=2, time=Time.bon_a, attacks=1,
    targets_mdef=True, max_range='4+WIS',
    shape=Shape.multi_point, target_area='Up to [[2+WIS]] creatures',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Compels creature to attack caster',
    prerequisites=(taunt_2,),
)

charge_1 = Ability(
    name='Charge I', picture=AbilityPicture.swift_song,
    mp_cost=1, attacks=1, mdam='1d4', damage_type=DamageType.force,
    targets_mdef=True,
    shape=Shape.point, target_area='Self',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='+1SPEED, hit creatures damaged and knocked back 1DIS in direction of movement',
)

charge_2 = Ability(
    name='Charge II', picture=AbilityPicture.swift_song,
    mp_cost=2, attacks=1, mdam='1d6', damage_type=DamageType.force,
    targets_mdef=True,
    shape=Shape.point, target_area='Self',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='+1SPEED, hit creatures damaged and knocked back 1DIS in direction of movement',
    prerequisites=(charge_1,),
)

charge_3 = Ability(
    name='Charge III', picture=AbilityPicture.swift_song,
    mp_cost=3, attacks=1, mdam='1d8+WIS', damage_type=DamageType.force,
    targets_mdef=True,
    shape=Shape.point, target_area='Self',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='+[[3+0.5*WIS]]SPEED, hit creatures damaged and knocked back [[3+2*WIS]]DIS in '
           'direction of movement',
    prerequisites=(charge_2,),
)

heave_1 = Ability(
    name='Heave I', picture=AbilityPicture.snap_punch,
    mp_cost=1, attacks=1, mdam='1d4', damage_type=DamageType.force,
    targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.instant,
    effect='Throws medium creature 3DIS',
)

heave_2 = Ability(
    name='Heave II', picture=AbilityPicture.snap_punch,
    mp_cost=3, attacks=1, mdam='1d8+2*WIS', damage_type=DamageType.force,
    targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.instant,
    effect='Throws 1 huge, 1 large, or 3 medium creatures [[3+2*WIS]]DIS',
    prerequisites=(heave_1,),
)

heave_3 = Ability(
    name='Heave III', picture=AbilityPicture.snap_punch,
    mp_cost=3, attacks=1, mdam='1d4+WIS', damage_type=DamageType.force,
    targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.instant,
    effect='Throws 1 large or 2 medium creature [[3+WIS]]DIS',
    prerequisites=(heave_2,),
)

ensnare_1 = Ability(
    name='Ensare I', picture=AbilityPicture.bio,
    mp_cost=3, attacks=1, mdam='1d4', damage_type=DamageType.poison,
    targets_mdef=True, max_range='6',
    shape=Shape.point, target_area='One creature',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Vines roots sprout from ground immobilizing and causing poison damage per RND',
)

ensnare_2 = Ability(
    name='Ensare II', picture=AbilityPicture.bio,
    mp_cost=5, attacks=1, mdam='1d6', damage_type=DamageType.poison,
    targets_mdef=True, max_range='8',
    shape=Shape.point, target_area='One creature',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Vines roots sprout from ground immobilizing and causing poison damage per RND',
    prerequisites=(ensnare_1,),
)

ensnare_3 = Ability(
    name='Ensare III', picture=AbilityPicture.bio,
    mp_cost=5, attacks=1, mdam='1d6+WIS', damage_type=DamageType.poison,
    targets_mdef=True, max_range='8',
    shape=Shape.circle, target_area='1RAD',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Vines roots sprout from ground immobilizing and causing poison damage per RND',
    prerequisites=(ensnare_2,),
)

lunacite_veins_1 = Ability(
    name='Lunacite Veins I', picture=AbilityPicture.adloquium,
    mp_cost=0, time=Time.free_a,
    shape=Shape.point, target_area='Self',
    duration_unit=DurationUnit.instant,
    effect='Passive: On successful REG, +1HP or RD to MP, does not stack.',
)

lunacite_veins_2 = Ability(
    name='Lunacite Veins II', picture=AbilityPicture.adloquium,
    mp_cost=0, time=Time.free_a,
    shape=Shape.point, target_area='Self',
    duration_unit=DurationUnit.instant,
    effect='Passive: On successful REG, add RD to HP or MP, does not stack.',
    prerequisites=(lunacite_veins_1,),
)

lunacite_veins_3 = Ability(
    name='Lunacite Veins III', picture=AbilityPicture.adloquium,
    mp_cost=0, time=Time.free_a,
    shape=Shape.point, target_area='Self',
    duration_unit=DurationUnit.instant,
    effect='Passive: On successful REG, add RD to HP and MP, does not stack.',
    prerequisites=(lunacite_veins_2,),
)

# Tier 2.

tremor_stomp_1 = Ability(
    name='Tremor Stomp I', picture=AbilityPicture.stone,
    mp_cost=4, time=Time.std_ab_a, attacks=1, mdam='1d6', damage_type=DamageType.force,
    targets_mdef=True,
    shape=Shape.circle, target_area='2RAD',
    duration_unit=DurationUnit.instant,
    effect='Stomping the ground knocks creatures back and immobilizes',
    prerequisites=(taunt_3, charge_3,),
)

tremor_stomp_2 = Ability(
    name='Tremor Stomp II', picture=AbilityPicture.stone,
    mp_cost=6, time=Time.std_ab_a, attacks=1, mdam='1d8+WIS', damage_type=DamageType.force,
    targets_mdef=True,
    shape=Shape.circle, target_area='2RAD',
    duration_unit=DurationUnit.instant,
    effect='Stomping the ground knocks creatures back and immobilizes',
    prerequisites=(tremor_stomp_1,),
)

tremor_stomp_3 = Ability(
    name='Tremor Stomp III', picture=AbilityPicture.stone,
    mp_cost=8, time=Time.std_ab_a, attacks=1, mdam='1d12+2*WIS', damage_type=DamageType.force,
    targets_mdef=True,
    shape=Shape.circle, target_area='[[2+WIS]]RAD',
    duration_unit=DurationUnit.instant,
    effect='Stomping the ground knocks creatures back and immobilizes',
    prerequisites=(tremor_stomp_2,),
)

rock_wall_1 = Ability(
    name='Rock Wall I', picture=AbilityPicture.stone_skin_2,
    mp_cost=2, max_range='10',
    shape=Shape.line, target_area='6 Long x 3 High x 1 Wide DIS',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Rock wall shoots out from ground. Each section has 20HP',
    prerequisites=(charge_2, ensnare_3,),
)

rock_wall_2 = Ability(
    name='Rock Wall II', picture=AbilityPicture.stone_skin_2,
    mp_cost=4, max_range='12',
    shape=Shape.line, target_area='[[7+WIS]] Long x 4 High x 1 Wide DIS',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Rock wall shoots out from ground. Each section has [[25+2*WIS]]HP',
    prerequisites=(rock_wall_1,),
)

rock_wall_3 = Ability(
    name='Rock Wall III', picture=AbilityPicture.convalescence,
    mp_cost=4, max_range='12+WIS',
    shape=Shape.line, target_area='[[9+WIS]] Long x 5 High x 1 Wide DIS',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Rock wall shoots out from ground. Each section has [[30+5*WIS]]HP',
    prerequisites=(rock_wall_2,),
)

emerald_armor_1 = Ability(
    name='Emerald Armor I', picture=AbilityPicture.stone_skin_2,
    mp_cost=3,
    shape=Shape.circle, target_area='Self + Allies in 4RAD',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='+3MDEF',
    prerequisites=(heave_3, lunacite_veins_2,),
)

emerald_armor_2 = Ability(
    name='Emerald Armor II', picture=AbilityPicture.stone_skin_2,
    mp_cost=6,
    shape=Shape.circle, target_area='Self + Allies in [[4+WIS]]RAD',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='+[[3+WIS]]MDEF, +1MRED',
    prerequisites=(emerald_armor_1,),
)

emerald_armor_3 = Ability(
    name='Emerald Armor III', picture=AbilityPicture.stone_skin_2,
    mp_cost=8,
    shape=Shape.circle, target_area='Self + Allies in [[4+(2*WIS)]]RAD',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='+[[3+WIS]]MDEF, +1 MRED, Absorb 1MP when hit by attacks dealing MDAM',
    prerequisites=(emerald_armor_2,),
)

revivify_1 = Ability(
    name='Revivify I', picture=AbilityPicture.leeches,
    mp_cost=5, time=Time.full_a,
    shape=Shape.point, target_area='Self',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='+[[d4]]HP per RND, +2PDEF, +2MDEF; Must continue to cast for Duration',
    prerequisites=(ensnare_2, lunacite_veins_2,),
)

revivify_2 = Ability(
    name='Revivify II', picture=AbilityPicture.leeches,
    mp_cost=8, time=Time.full_a,
    shape=Shape.point, target_area='Self',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='+[[d8+WIS]]HP per RND, +[[2+WIS]]PDEF, +2MDEF; Must continue to cast for Duration',
    prerequisites=(revivify_1,),
)

revivify_3 = Ability(
    name='Revivify III', picture=AbilityPicture.leeches,
    mp_cost=12, time=Time.full_a,
    shape=Shape.point, target_area='Self',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='+[[d12+2*WIS]]HP per RND, +[[3+WIS]]PDEF, +[[3+WIS]]MDEF; '
           'Must continue to cast for Duration',
    prerequisites=(revivify_1,),
)

viridian_glow_1 = Ability(
    name='Viridian Glow I', picture=AbilityPicture.lustrate,
    mp_cost=0, time=Time.free_a,
    shape=Shape.circle, target_area='Allies in 6RAD',
    duration_unit=DurationUnit.instant,
    effect='Passive: On successful REG, allies gain +1HP, does not stack.',
    prerequisites=(ensnare_2, lunacite_veins_3,),
)

viridian_glow_2 = Ability(
    name='Viridian Glow II', picture=AbilityPicture.lustrate,
    mp_cost=0, time=Time.free_a,
    shape=Shape.circle, target_area='Allies in [[6+WIS]]RAD',
    duration_unit=DurationUnit.instant,
    effect='Passive: On successful REG, add RD to allies HP, does not stack.',
    prerequisites=(viridian_glow_1,),
)

viridian_glow_3 = Ability(
    name='Viridian Glow III', picture=AbilityPicture.lustrate,
    mp_cost=0, time=Time.free_a,
    shape=Shape.circle, target_area='Allies in [[6+WIS]]RAD',
    duration_unit=DurationUnit.instant,
    effect='Passive: On successful REG, add RD to allies MP, does not stack.',
    prerequisites=(viridian_glow_2,),
)

# Tier 3.

rend_1 = Ability(
    name='Rend I', picture=AbilityPicture.phlebotomize,
    mp_cost=5, time=Time.full_a, attacks=1, mdam='1d20+WIS', damage_type=DamageType.force,
    targets_mdef=True, max_range='1',
    target_area='Weapon AOE',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster channels power into single power attack that adds to a single normal physical '
           'attack. Immobilizes.',
    prerequisites=(tremor_stomp_3, emerald_armor_2,),
)

rend_2 = Ability(
    name='Rend II', picture=AbilityPicture.phlebotomize,
    mp_cost=8, time=Time.full_a, attacks=1, mdam='1d20+1d10 +2*WIS', damage_type=DamageType.force,
    targets_mdef=True, max_range='1',
    target_area='Weapon AOE',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster channels power into single power attack that adds to a single normal physical '
           'attack. Disables.',
    prerequisites=(rend_1,),
)

rend_3 = Ability(
    name='Rend III', picture=AbilityPicture.phlebotomize,
    mp_cost=12, time=Time.full_a, attacks=1, mdam='2d20+3*WIS', damage_type=DamageType.force,
    targets_mdef=True, max_range='1',
    target_area='Weapon AOE',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Caster channels power into single power attack that adds to a single normal physical '
           'attack. Stuns.',
    prerequisites=(rend_2,),
)

quake_1 = Ability(
    name='Quake I', picture=AbilityPicture.stone_2,
    mp_cost=8, attacks=1, mdam='2d10', damage_type=DamageType.force,
    targets_mdef=True, max_range='1',
    shape=Shape.line, target_area='7 Long x 2 Deep x 2 Wide DIS',
    duration_unit=DurationUnit.instant,
    effect='Tears chasm into ground, causing enemies to fall into it.',
    prerequisites=(tremor_stomp_2, rock_wall_3,),
)

quake_2 = Ability(
    name='Quake II', picture=AbilityPicture.stone_2,
    mp_cost=10, attacks=1, mdam='2d12+WIS', damage_type=DamageType.force,
    targets_mdef=True, max_range='1',
    shape=Shape.line, target_area='[[9+WIS]] Long x 2 Deep x 3 Wide DIS',
    duration_unit=DurationUnit.instant,
    effect='Tears chasm into ground, causing enemies to fall into it.',
    prerequisites=(quake_1,),
)

quake_3 = Ability(
    name='Quake III', picture=AbilityPicture.stone_2,
    mp_cost=12, attacks=1, mdam='3d12+2*WIS', damage_type=DamageType.force,
    targets_mdef=True, max_range='1',
    shape=Shape.line, target_area='[[11+WIS]] Long x 2 Deep x 4 Wide DIS',
    duration_unit=DurationUnit.instant,
    effect='Tears chasm into ground, causing enemies to fall into it.',
    prerequisites=(quake_2,),
)

rage_1 = Ability(
    name='Rage I', picture=AbilityPicture.inner_beast,
    mp_cost=6, time=Time.bon_a,
    target_area='Self',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='+4PDAM to weapon, -2PAC, -1HP per RND, All creatures appear as enemies. '
           'Uncontrollable, attack closest creature',
    prerequisites=(tremor_stomp_2, rock_wall_2, emerald_armor_2,),
)

rage_2 = Ability(
    name='Rage II', picture=AbilityPicture.inner_beast,
    mp_cost=8, time=Time.bon_a,
    target_area='Self',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='+[[6+WIS]]PDAM to weapon, -2PAC, -2HP per RND, All creatures appear as enemies. '
           'Uncontrollable, attack closest creature',
    prerequisites=(rage_1,),
)

rage_3 = Ability(
    name='Rage III', picture=AbilityPicture.inner_beast,
    mp_cost=16, time=Time.bon_a,
    target_area='Self',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='+[[6+2*WIS]]PDAM to weapon. +1 Attack. -3PAC, -3HP per RND, All creatures appear as '
           'enemies. Uncontrollable, attack closest creature',
    prerequisites=(rage_2,),
)

mass_revivify_1 = Ability(
    name='Mass Revivify I', picture=AbilityPicture.leeches,
    mp_cost=10, time=Time.full_a,
    shape=Shape.point, target_area='Self + Allies in 5RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Heals self and allies +[[d4]]HP per RND. Self: +2PDEF, +2MDEF. '
           'Must continue to cast for Duration',
    prerequisites=(revivify_3, viridian_glow_2,),
)

mass_revivify_2 = Ability(
    name='Mass Revivify II', picture=AbilityPicture.leeches,
    mp_cost=16, time=Time.full_a,
    shape=Shape.point, target_area='Self + Allies in 6RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Heals self and allies +[[d8+WIS]]HP per RND. Self: +[[2+WIS]]PDEF, +2MDEF. '
           'Must continue to cast for Duration',
    prerequisites=(mass_revivify_1,),
)

mass_revivify_3 = Ability(
    name='Mass Revivify III', picture=AbilityPicture.leeches,
    mp_cost=24, time=Time.full_a,
    shape=Shape.point, target_area='Self + Allies in [[6+WIS]]RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='Heals self and allies +[[d12+2*WIS]]HP per RND. Self: +[[3+WIS]]PDEF, +[[3+WIS]]MDEF. '
           'Must continue to cast for Duration',
    prerequisites=(mass_revivify_2,),
)

petrify_1 = Ability(
    name='Petrify I', picture=AbilityPicture.stone_skin,
    mp_cost=15, time=Time.full_a, attacks=1,
    targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.forever,
    effect='Turns 20lb object or [small] creature to stone. '
           'Caster spends 3FullA and target must fail MDEF 3 times.',
    prerequisites=(rock_wall_3, emerald_armor_3, viridian_glow_3,),
)

petrify_2 = Ability(
    name='Petrify II', picture=AbilityPicture.stone_skin,
    mp_cost=30, time=Time.full_a, attacks=1,
    targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.forever,
    effect='Turns 200lb object or [medium] creature to stone. '
           'Caster spends 3FullA and target must fail MDEF 3 times.',
    prerequisites=(petrify_1,),
)

petrify_3 = Ability(
    name='Petrify III', picture=AbilityPicture.stone_skin,
    mp_cost=45, time=Time.full_a, attacks=1,
    targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.forever,
    effect='Turns 800lb object or [large] creature to stone. '
           'Caster spends 3FullA and target must fail MDEF 3 times.',
    prerequisites=(petrify_2,),
)


class Geomancer(Class):
    def __init__(self) -> None:
        super().__init__(
            name=self.__class__.__name__, hd=20, md=4, sd=2, speed=3, pdef=3, mdef=0.5,
            pred=0.5, mred=0.5, reg=0.75, vis=4, pac=1, mac=0.5, ath=4, ste=1, fort=5, apt=1,
            per=2, spe=2, starting_ap=4,
            use_melee_heavy=True,
            use_light_armor=True, use_medium_armor=True, use_heavy_armor=True,
            abilities=(taunt_1, taunt_2, taunt_3,
                       charge_1, charge_2, charge_3,
                       heave_1, heave_2, heave_3,
                       ensnare_1, ensnare_2, ensnare_3,
                       lunacite_veins_1, lunacite_veins_2, lunacite_veins_3,
                       tremor_stomp_1, tremor_stomp_2, tremor_stomp_3,
                       rock_wall_1, rock_wall_2, rock_wall_3,
                       emerald_armor_1, emerald_armor_2, emerald_armor_3,
                       revivify_1, revivify_2, revivify_3,
                       viridian_glow_1, viridian_glow_2, viridian_glow_3,
                       rend_1, rend_2, rend_3,
                       quake_1, quake_2, quake_3,
                       rage_1, rage_2, rage_3,
                       mass_revivify_1, mass_revivify_2, mass_revivify_3,
                       petrify_1, petrify_2, petrify_3,))
