from typing import Tuple

from .ability import Ability, AbilityPicture, DurationUnit, Time
from .class_type import Class
from .classes.geomancer import Geomancer
from .classes.magus import Magus
from .classes.marksman import Marksman
from .classes.paladin import Paladin
from .classes.spectre import Spectre
from .classes.telepath import Telepath
from .classes.templar import Templar
from .classes.valkyrie import Valkyrie
from .equipment import DamageType, Shape


class Combo(Ability):
    def __init__(self, classes: Tuple[Class, Class], prerequisite_lvl: int,
                 name: str, picture: AbilityPicture, mp_cost: int, target_area: str,
                 duration: str = None, duration_unit: DurationUnit = DurationUnit.instant,
                 damage_type: DamageType = None,
                 effect='',
                 attacks: int = 0, pdam: str = None, mdam: str = None,
                 targets_mdef: bool = False, time: Time = Time.ab_a, min_range: str = '0',
                 max_range: str = '0', shape: Shape = Shape.point) -> None:
        self.classes = classes
        self.prerequisite_lvl = prerequisite_lvl
        super().__init__(name=name, picture=picture, mp_cost=mp_cost, target_area=target_area,
                         duration=duration, duration_unit=duration_unit, prerequisites=(),
                         damage_type=damage_type, effect=effect, attacks=attacks, pdam=pdam,
                         mdam=mdam, targets_mdef=targets_mdef, time=time, min_range=min_range,
                         max_range=max_range, shape=shape)


combos = (
    Combo(
        classes=(Paladin, Templar), prerequisite_lvl=2,
        name='Temporal Shock Wave I', picture=AbilityPicture.benediction,
        mp_cost=4, attacks=1, mdam='d10 + WIS',
        damage_type=DamageType.force, targets_mdef=True, time=Time.full_a, min_range='1',
        max_range='1', shape=Shape.circle, target_area='[[1+WIS]]RAD',
        duration_unit=DurationUnit.instant,
        effect='Removes status effects from allies and heals [[d4+WIS]]HP. '
               'Knockback enemies [[WIS]]DIS.'
    ),
    Combo(
        classes=(Paladin, Templar), prerequisite_lvl=5,
        name='Temporal Shock Wave II', picture=AbilityPicture.benediction,
        mp_cost=7, attacks=1, mdam='2d12 + WIS',
        damage_type=DamageType.force, targets_mdef=True, time=Time.full_a, min_range='1',
        max_range='1', shape=Shape.circle, target_area='[[2+WIS]]RAD',
        duration_unit=DurationUnit.instant,
        effect='Removes status effects from allies and heals [[2d10+WIS]]HP. '
               'Knockback enemies [[1+WIS]]DIS.'
    ),
    Combo(
        classes=(Paladin, Templar), prerequisite_lvl=8,
        name='Temporal Shock Wave III', picture=AbilityPicture.benediction,
        mp_cost=12, attacks=1, mdam='4d12 + 2*WIS',
        damage_type=DamageType.force, targets_mdef=True, time=Time.full_a, min_range='1',
        max_range='1', shape=Shape.circle, target_area='[[4+WIS]]RAD',
        duration_unit=DurationUnit.instant,
        effect='Removes status effects from allies and heals [[3d10+2*WIS]]HP. '
               'Knockback enemies  [[3+WIS]]DIS.'
    ),
    Combo(
        classes=(Paladin, Magus), prerequisite_lvl=2,
        name='Prism I', picture=AbilityPicture.presence_of_mind,
        mp_cost=6, attacks=1,
        time=Time.free_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='Self and 1 ally', duration='4', duration_unit=DurationUnit.rnd,
        effect='Magus loses weapon attack & control of movement, moving to any adjacent space '
               'next to the Paladin.  Paladin takes 50% DAM for Magus.  When Magus or Paladin '
               'hit, Magus counters with weapon attack as FreeA.  All Paladin weapon attacks slow '
               '[[-WIS]]SPEED.  -2SPEED'
    ),
    Combo(
        classes=(Paladin, Magus), prerequisite_lvl=5,
        name='Prism II', picture=AbilityPicture.presence_of_mind,
        mp_cost=8, attacks=1, mdam='2d10', damage_type=DamageType.fire,
        time=Time.free_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='Self and 1 ally', duration='4+WIS', duration_unit=DurationUnit.rnd,
        effect='Magus loses weapon attack & control of movement, moving to any adjacent space '
               'next to the Paladin.  Paladin takes 50% DAM for Magus.  When Magus or Paladin '
               'hit, Magus counters with weapon attack as FreeA.  All Paladin weapon attacks '
               'deal extra MDAM. -1SPEED'
    ),
    Combo(
        classes=(Paladin, Magus), prerequisite_lvl=8,
        name='Prism III', picture=AbilityPicture.presence_of_mind,
        mp_cost=12, attacks=1, mdam='3d12+WIS', damage_type=DamageType.lightning,
        time=Time.free_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='Self and 1 ally', duration='6+WIS', duration_unit=DurationUnit.rnd,
        effect='Magus loses weapon attack & control of movement, moving to any adjacent space '
               'next to the Paladin.  Paladin takes 50% DAM for Magus.  When Magus or Paladin '
               'hit, Magus counters with weapon attack as FreeA.  All Paladin weapon attacks deal '
               'extra MDAM. -1SPEED'
    ),
    Combo(
        classes=(Paladin, Spectre), prerequisite_lvl=2,
        name='Mirage I', picture=AbilityPicture.eye_for_an_eye,
        mp_cost=5, time=Time.ab_a, min_range='1', max_range='1', shape=Shape.circle,
        target_area='Up to 5RAD', duration='6', duration_unit=DurationUnit.rnd,
        effect='Can create a mirage on the outside of a telekinetic shell.'
    ),
    Combo(
        classes=(Paladin, Spectre), prerequisite_lvl=5,
        name='Mirage II', picture=AbilityPicture.eye_for_an_eye,
        mp_cost=8, time=Time.ab_a, min_range='1', max_range='1', shape=Shape.circle,
        target_area='Up to [[7+WIS]]RAD', duration='7+WIS', duration_unit=DurationUnit.rnd,
        effect='Can create a mirage on the outside of a telekinetic shell.  Objects within the '
               'shell feel as if they are real.'
    ),
    Combo(
        classes=(Paladin, Spectre), prerequisite_lvl=8,
        name='Mirage III', picture=AbilityPicture.eye_for_an_eye,
        mp_cost=12, time=Time.ab_a, min_range='1', max_range='1', shape=Shape.circle,
        target_area='Up to [[12+2*WIS]]RAD', duration='10+WIS', duration_unit=DurationUnit.rnd,
        effect='Can create a mirage on the outside of a telekinetic shell.  Objects within and '
               'outside the shell feel as if they are real.'
    ),
    Combo(
        classes=(Paladin, Valkyrie), prerequisite_lvl=2,
        name='Rift I', picture=AbilityPicture.miasma,
        mp_cost=8, targets_mdef=True, mdam='1d8+WIS', damage_type=DamageType.force,
        time=Time.full_a, min_range='1', max_range='8', shape=Shape.circle,
        target_area='[[4+WIS]]RAD', duration='4', duration_unit=DurationUnit.rnd,
        effect='Rips a hole in space.  Pulls creatures within area 3DIS towards it.  Deals '
               'double damage if creatures are adjacent to the rift.  Requires FullA per RND to '
               'keep open.'
    ),
    Combo(
        classes=(Paladin, Valkyrie), prerequisite_lvl=2,
        name='Rift II', picture=AbilityPicture.miasma,
        mp_cost=12, targets_mdef=True, mdam='2d10+2*WIS', damage_type=DamageType.force,
        time=Time.full_a, min_range='1', max_range='10+WIS', shape=Shape.circle,
        target_area='[[4+WIS]]RAD', duration='4+WIS', duration_unit=DurationUnit.rnd,
        effect='Rips a hole in space.  Pulls creatures within area 3DIS towards it.  Deals '
               'double damage if creatures are adjacent to the rift.  Requires FullA per RND to '
               'keep open.'
    ),
    Combo(
        classes=(Paladin, Valkyrie), prerequisite_lvl=2,
        name='Rift III', picture=AbilityPicture.miasma,
        mp_cost=16, targets_mdef=True, mdam='4d10+4*WIS', damage_type=DamageType.force,
        time=Time.ab_a, min_range='1', max_range='10+WIS', shape=Shape.circle,
        target_area='[[12+WIS]]RAD', duration='6+WIS', duration_unit=DurationUnit.rnd,
        effect='Rips a hole in space.  Pulls creatures within area [[3+WIS]]DIS towards it. '
               'Deals double damage if creatures are adjacent to the rift.'
    ),
    # Paladin Geomancer: Rocket
    #   Paladin is thrown, taking StdA against all targets in Range along path, leaving a tremor.
    Combo(
        classes=(Paladin, Marksman), prerequisite_lvl=2,
        name='Shaped Round I', picture=AbilityPicture.steel_peak,
        mp_cost=4, attacks=1, targets_mdef=True, mdam='1d6', damage_type=DamageType.force,
        time=Time.ab_a, min_range='1', max_range='5+WIS', shape=Shape.point,
        target_area='Marksman attack',
        effect='Trajectory of marksman weapon or ability attack bends up to 45 degrees and deals '
               'extra Force damage.'
    ),
    Combo(
        classes=(Paladin, Marksman), prerequisite_lvl=5,
        name='Shaped Round II', picture=AbilityPicture.steel_peak,
        mp_cost=6, attacks=1, targets_mdef=True, mdam='1d8+WIS', damage_type=DamageType.force,
        time=Time.ab_a, min_range='1', max_range='7+WIS', shape=Shape.point,
        target_area='Marksman attack',
        effect='Trajectory of marksman weapon or ability attack bends up to 90 degrees and deals '
               'extra Force damage.'
    ),
    Combo(
        classes=(Paladin, Marksman), prerequisite_lvl=8,
        name='Shaped Round III', picture=AbilityPicture.steel_peak,
        mp_cost=8, attacks=1, targets_mdef=True, mdam='1d12+2*WIS', damage_type=DamageType.force,
        time=Time.ab_a, min_range='1', max_range='9+WIS', shape=Shape.point,
        target_area='Marksman attack',
        effect='Trajectory of marksman weapon or ability attack bends up to 180 degrees and deals '
               'extra Force damage.'
    ),
    Combo(
        classes=(Templar, Magus), prerequisite_lvl=2,
        name='Alternating Current I', picture=AbilityPicture.aetherial_manipulation,
        mp_cost=6, attacks=1, targets_mdef=True, mdam='d4+WIS', damage_type=DamageType.lightning,
        time=Time.full_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='All adjacent enemies along path',
        effect='Casters zip through the air up to the sum of their SPEED, taking an ability '
               'attack against each enemy they move adjacent to.  Each successful attack adds '
               '+1SPEED.  Immobilizes for 1RND.'
    ),
    Combo(
        classes=(Templar, Magus), prerequisite_lvl=5,
        name='Alternating Current II', picture=AbilityPicture.aetherial_manipulation,
        mp_cost=8, attacks=1, targets_mdef=True, mdam='2d10+WIS', damage_type=DamageType.lightning,
        time=Time.full_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='All adjacent enemies along path',
        effect='Casters zip through the air up to the sum of their SPEED, taking an ability '
               'attack against each enemy they move adjacent to.  Each successful attack adds '
               '+1SPEED.  Disables for 1RND.'
    ),
    Combo(
        classes=(Templar, Magus), prerequisite_lvl=8,
        name='Alternating Current III', picture=AbilityPicture.aetherial_manipulation,
        mp_cost=10, attacks=1, targets_mdef=True, mdam='3d12+2*WIS',
        damage_type=DamageType.lightning,
        time=Time.full_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='All adjacent enemies along path',
        effect='Casters zip through the air up to the sum of their SPEED, taking an ability '
               'attack against each enemy they move adjacent to.  Each successful attack adds '
               '+2SPEED.  Stuns for 1RND.'
    ),
    Combo(
        classes=(Templar, Spectre), prerequisite_lvl=2,
        name='Temporal Echo I', picture=AbilityPicture.cleric_stance,
        mp_cost=4, time=Time.ab_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='Self + 1 ally', duration='4', duration_unit=DurationUnit.rnd,
        effect='Casters exist in two places at once and can perform basic actions.'
    ),
    Combo(
        classes=(Templar, Spectre), prerequisite_lvl=5,
        name='Temporal Echo II', picture=AbilityPicture.cleric_stance,
        mp_cost=8, time=Time.ab_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='Self + 1 ally', duration='4+WIS', duration_unit=DurationUnit.rnd,
        effect='Casters exist in two places at once and can perform basic actions, or physical '
               'attacks.'
    ),
    Combo(
        classes=(Templar, Spectre), prerequisite_lvl=8,
        name='Temporal Echo III', picture=AbilityPicture.cleric_stance,
        mp_cost=12, time=Time.ab_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='Self + 1 ally', duration='6+WIS', duration_unit=DurationUnit.rnd,
        effect='Casters exist in two places at once and can perform basic actions, physical '
               'attacks, or abilities.'
    ),
    Combo(
        classes=(Templar, Valkyrie), prerequisite_lvl=2,
        name='Hyper Jump I', picture=AbilityPicture.impulse_drive,
        mp_cost=6, time=Time.full_a, min_range='1', max_range='1', shape=Shape.circle,
        target_area='[[WIS]]RAD', duration='1', duration_unit=DurationUnit.rnd,
        effect='Split space and time to teleport a great distance at once ([[14+WIS]]DIS).  On '
               'arrival, stun surrounding enemies. Physical and magical attacks interrupt. '
               'Additional FullA of charge up needed.'
    ),
    Combo(
        classes=(Templar, Valkyrie), prerequisite_lvl=5,
        name='Hyper Jump II', picture=AbilityPicture.impulse_drive,
        mp_cost=8, time=Time.full_a, min_range='1', max_range='1', shape=Shape.circle,
        target_area='[[2+WIS]]RAD', duration='1', duration_unit=DurationUnit.rnd,
        effect='Split space and time to teleport a great distance at once ([[16+2*WIS]]DIS). '
               'On arrival, stun surrounding enemies. Physical attacks interrupt. Additional '
               'FullA of charge up needed.'
    ),
    Combo(
        classes=(Templar, Valkyrie), prerequisite_lvl=8,
        name='Hyper Jump III', picture=AbilityPicture.impulse_drive,
        mp_cost=10, time=Time.full_a, min_range='1', max_range='1', shape=Shape.circle,
        target_area='[[4+WIS]]RAD', duration='1', duration_unit=DurationUnit.rnd,
        effect='Split space and time to teleport a great distance at once ([[24+3*WIS]]DIS). '
               'On arrival, stun surrounding enemies. Additional FullA of charge up needed.'
    ),
    Combo(
        classes=(Templar, Telepath), prerequisite_lvl=2,
        name='Mind Travel I', picture=AbilityPicture.convert,
        mp_cost=8, attacks=1, targets_mdef=True,
        time=Time.full_a, min_range='1', max_range='1',
        target_area='One creature', duration='5+WIS', duration_unit=DurationUnit.min,
        effect='Experience an event in the target\'s past up to 3 months earlier.  Can only hear. '
               'Target is aware of the ability.'
    ),
    Combo(
        classes=(Templar, Telepath), prerequisite_lvl=5,
        name='Mind Travel II', picture=AbilityPicture.convert,
        mp_cost=15, attacks=1, targets_mdef=True,
        time=Time.full_a, min_range='1', max_range='1',
        target_area='One creature', duration='10+WIS', duration_unit=DurationUnit.min,
        effect='Experience an event in the target\'s past up to 1 year earlier.  Can see and '
               'hear. '
               'Target is aware of the ability.'
    ),
    Combo(
        classes=(Templar, Telepath), prerequisite_lvl=8,
        name='Mind Travel III', picture=AbilityPicture.convert,
        mp_cost=30, attacks=1, targets_mdef=True,
        time=Time.full_a, min_range='1', max_range='1',
        target_area='One creature', duration='1+WIS', duration_unit=DurationUnit.hour,
        effect='Experience an event any time in the target\'s past.  Can see and hear.  Target is'
               ' un-aware of the ability.'
    ),
    Combo(
        classes=(Templar, Geomancer), prerequisite_lvl=2,
        name='Biome I', picture=AbilityPicture.aero,
        mp_cost=6, time=Time.ab_a, min_range='1', max_range='1', shape=Shape.circle,
        target_area='Allies in 3RAD', duration='5', duration_unit=DurationUnit.rnd,
        effect='Lush jungle sprouts up and heals party [[d4]]HP per RND.'
    ),
    Combo(
        classes=(Templar, Geomancer), prerequisite_lvl=5,
        name='Biome II', picture=AbilityPicture.aero,
        mp_cost=8, time=Time.ab_a, min_range='1', max_range='1', shape=Shape.circle,
        target_area='Allies in [[3+WIS]]RAD', duration='5+WIS', duration_unit=DurationUnit.rnd,
        effect='Lush jungle sprouts up and heals party [[d10+WIS]]HP per RND. '
               'Removes status effects.'
    ),
    Combo(
        classes=(Templar, Geomancer), prerequisite_lvl=8,
        name='Biome III', picture=AbilityPicture.aero,
        mp_cost=12, time=Time.ab_a, min_range='1', max_range='1', shape=Shape.circle,
        attacks=2, targets_mdef=True, mdam='d4', damage_type=DamageType.poison,
        target_area='Allies in [[3+WIS]]RAD', duration='5+WIS', duration_unit=DurationUnit.rnd,
        effect='Lush jungle sprouts up and heals party [[d10+WIS]]HP per RND. '
               'Removes status effects.'
    ),
    # Templar Marksman
    Combo(
        classes=(Magus, Spectre), prerequisite_lvl=2,
        name='Flashbang I', picture=AbilityPicture.wide_volley,
        mp_cost=4, attacks=1, targets_mdef=True,
        time=Time.ab_a, min_range='1', max_range='5', shape=Shape.circle,
        target_area='Enemies in 5RAD', duration='2', duration_unit=DurationUnit.rnd,
        effect='Blinds enemies and removes RES.'
    ),
    Combo(
        classes=(Magus, Spectre), prerequisite_lvl=5,
        name='Flashbang II', picture=AbilityPicture.wide_volley,
        mp_cost=12, attacks=1, targets_mdef=True,
        time=Time.ab_a, min_range='1', max_range='5+WIS', shape=Shape.circle,
        target_area='Enemies in [[5+WIS]]RAD', duration='2+WIS', duration_unit=DurationUnit.rnd,
        effect='Blinds, disables enemies, and removes RES.'
    ),
    Combo(
        classes=(Magus, Spectre), prerequisite_lvl=8,
        name='Flashbang III', picture=AbilityPicture.wide_volley,
        mp_cost=20, attacks=1, targets_mdef=True,
        time=Time.ab_a, min_range='1', max_range='7+WIS', shape=Shape.circle,
        target_area='Enemies in [[7+WIS]]RAD', duration='2+WIS', duration_unit=DurationUnit.rnd,
        effect='Blinds, stuns enemies, and removes RES and IMU.'
    ),
    Combo(
        classes=(Magus, Valkyrie), prerequisite_lvl=2,
        name='Lightning Jump I', picture=AbilityPicture.fists_of_wind,
        mp_cost=6, attacks=1, targets_mdef=True, mdam='d4+WIS', damage_type=DamageType.lightning,
        time=Time.full_a, min_range='1', max_range='3', shape=Shape.multi_point,
        target_area='All enemies jumped to',
        effect='Casters teleport between enemies that are within Range of each other, returning '
               'to original location. Immobilizes 1RND.'
    ),
    Combo(
        classes=(Magus, Valkyrie), prerequisite_lvl=5,
        name='Lightning Jump II', picture=AbilityPicture.fists_of_wind,
        mp_cost=8, attacks=1, targets_mdef=True, mdam='2d10+WIS', damage_type=DamageType.lightning,
        time=Time.full_a, min_range='1', max_range='3+WIS', shape=Shape.multi_point,
        target_area='All enemies jumped to',
        effect='Casters teleport between enemies that are within Range of each other, returning '
               'to original location. Disables 1RND.'
    ),
    Combo(
        classes=(Magus, Valkyrie), prerequisite_lvl=8,
        name='Lightning Jump III', picture=AbilityPicture.fists_of_wind,
        mp_cost=10, attacks=1, targets_mdef=True, mdam='3d12+2*WIS',
        damage_type=DamageType.lightning,
        time=Time.full_a, min_range='1', max_range='5+WIS', shape=Shape.multi_point,
        target_area='All enemies jumped to',
        effect='Casters teleport between enemies that are within Range of each other, returning '
               'to original location. Stuns 1RND.'
    ),
    Combo(
        classes=(Magus, Telepath), prerequisite_lvl=2,
        name='Shock Therapy', picture=AbilityPicture.enkindle,
        mp_cost=8,
        time=Time.full_a, min_range='1', max_range='1', shape=Shape.point,
        duration='1', duration_unit=DurationUnit.hour, target_area='One creature',
        effect='Jolt a creature\'s cognitive abilities, granting ADV on APT and SPE checks.'
    ),
    Combo(
        classes=(Magus, Telepath), prerequisite_lvl=5,
        name='Cryostasis', picture=AbilityPicture.raise_ability,
        mp_cost=20,
        time=Time.full_a, min_range='1', max_range='1', shape=Shape.point,
        duration='1+WIS', duration_unit=DurationUnit.day, target_area='One creature',
        effect='Shuts down willing or KO\'d creature\'s, mental and physical systems, simulating '
               'death but preserving the life of the creature.  Casting again can reanimate early.'
    ),
    Combo(
        classes=(Magus, Telepath), prerequisite_lvl=7,
        name='Heat Wave', picture=AbilityPicture.rock_breaker,
        mp_cost=12, attacks=1, targets_mdef=True,
        time=Time.full_a, min_range='1', max_range='10+WIS', shape=Shape.circle,
        duration='5+WIS', duration_unit=DurationUnit.rnd, target_area='[[5+WIS]]RAD',
        effect='Causes creatures to feel uncomfortably hot, causing them to generally want to '
               'leave the immediate area quietly.  Effect severity can be tuned.'
    ),
    # Magus Geomancer: Meteor, Fire, Ice, Lightning.
    Combo(
        classes=(Spectre, Valkyrie), prerequisite_lvl=2,
        name='Twilight I', picture=AbilityPicture.ninjutsu,
        mp_cost=6, time=Time.full_a, min_range='1', max_range='1', shape=Shape.line,
        target_area='1RAD portal', duration='1', duration_unit=DurationUnit.rnd,
        effect='Look through a 1DIS wall/surface and create a portal beyond it.'
    ),
    Combo(
        classes=(Spectre, Valkyrie), prerequisite_lvl=5,
        name='Twilight II', picture=AbilityPicture.ninjutsu,
        mp_cost=10, time=Time.full_a, min_range='1', max_range='2+WIS', shape=Shape.line,
        target_area='1RAD portal', duration='1+WIS', duration_unit=DurationUnit.rnd,
        effect='Look through a 2DIS wall/surface and create a portal beyond it.'
    ),
    Combo(
        classes=(Spectre, Valkyrie), prerequisite_lvl=8,
        name='Twilight III', picture=AbilityPicture.ninjutsu,
        mp_cost=14, time=Time.full_a, min_range='1', max_range='4+WIS', shape=Shape.line,
        target_area='[[1+WIS]]RAD portal', duration='3+WIS', duration_unit=DurationUnit.rnd,
        effect='Look through a [[2+WIS]]DIS wall/surface and create a portal beyond it.'
    ),
    # Spectre Marksman
    Combo(
        classes=(Spectre, Telepath), prerequisite_lvl=2,
        name='Mirror I', picture=AbilityPicture.perfect_dodge,
        mp_cost=7, time=Time.full_a, min_range='1', max_range='1', shape=Shape.multi_point,
        duration='1+WIS', duration_unit=DurationUnit.min,
        target_area='Casters',
        effect='Casters appear to others as the same shape, size, and voice as two other small '
               'or medium creatures that have been seen. Casters must remain within '
               '[[5+WIS]]DIS or the ability ends. Cooldown of 1 minute. Physical or magical '
               'attacks taken or received end the ability.'
    ),
    Combo(
        classes=(Spectre, Telepath), prerequisite_lvl=5,
        name='Mirror II', picture=AbilityPicture.perfect_dodge,
        mp_cost=10, time=Time.full_a, min_range='1', max_range='1', shape=Shape.multi_point,
        duration='5+WIS', duration_unit=DurationUnit.min,
        target_area='Casters + 1 ally',
        effect='Casters appear to others as the same shape, size, and voice as three other small '
               'or medium creatures that have been seen. Casters must remain within '
               '[[8+2*WIS]]DIS or the ability ends. Cooldown of 1 minute. Physical or magical '
               'attacks taken or received end the ability.'
    ),
    Combo(
        classes=(Spectre, Telepath), prerequisite_lvl=8,
        name='Mirror III', picture=AbilityPicture.perfect_dodge,
        mp_cost=18, time=Time.full_a, min_range='1', max_range='1', shape=Shape.multi_point,
        duration='1+WIS', duration_unit=DurationUnit.hour,
        target_area='Casters + 2 ally',
        effect='Casters appear to others as the same shape, size, and voice as four other small, '
               'medium, or large creatures that have been seen. Physical or magical '
               'attacks taken or received end the ability.'
    ),
    Combo(
        classes=(Valkyrie, Telepath), prerequisite_lvl=2,
        name='Recall I', picture=AbilityPicture.aetherial_manipulation,
        mp_cost=14, time=Time.full_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='Casters',
        effect='Teleport to some place you have been before, up to 1km. Physical or magical '
               'attacks interrupt. Requires 2FullA additional charge up rounds.'
    ),
    Combo(
        classes=(Valkyrie, Telepath), prerequisite_lvl=5,
        name='Recall II', picture=AbilityPicture.aetherial_manipulation,
        mp_cost=20, time=Time.full_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='Casters + 1 ally',
        effect='Teleport to some place you have been before, up to 2km. Physical attacks '
               'interrupt. Requires 2FullA additional charge up rounds.'
    ),
    Combo(
        classes=(Valkyrie, Telepath), prerequisite_lvl=8,
        name='Recall III', picture=AbilityPicture.aetherial_manipulation,
        mp_cost=26, time=Time.full_a, min_range='1', max_range='1', shape=Shape.multi_point,
        target_area='Casters + 2 allies',
        effect='Teleport to some place you have been before, up to 10km. Requires 2FullA '
               'additional charge up rounds.'
    ),
    # Valkyrie, Geomancer: Titanfall
    # Valkyrie, Marksman: Pavelow
    # Telepath, Geomancer
    # Telepath, Marksman
    # Geomancer, Marksman: Rodeo
)
