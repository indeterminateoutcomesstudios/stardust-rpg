import aenum

from .classes import paladin


class Abilities(aenum.AutoNumberEnum):
    # Paladin.
    reflect_1 = ()
    reflect_2 = ()
    reflect_3 = ()
    telekinesis_1 = ()
    telekinesis_2 = ()
    telekinesis_3 = ()
    protect_1 = ()
    protect_2 = ()
    protect_3 = ()
    earth_breaker_1 = ()
    earth_breaker_2 = ()
    earth_breaker_3 = ()
    barrier_1 = ()
    barrier_2 = ()
    barrier_3 = ()
    shell_1 = ()
    shell_2 = ()
    shell_3 = ()
    vortex_1 = ()
    vortex_2 = ()
    vortex_3 = ()
    provoke_1 = ()
    provoke_2 = ()
    provoke_3 = ()
    shatter_1 = ()
    shatter_2 = ()
    shatter_3 = ()
    mass_barrier_1 = ()
    mass_barrier_2 = ()
    mass_barrier_3 = ()
    shockwave_1 = ()
    shockwave_2 = ()
    shockwave_3 = ()
    animate_weapon_1 = ()
    animate_weapon_2 = ()
    animate_weapon_3 = ()
    mass_telekinesis_1 = ()
    mass_telekinesis_2 = ()
    mass_telekinesis_3 = ()
    master_telekinetic_1 = ()
    master_telekinetic_2 = ()
    master_telekinetic_3 = ()


abilities = {
    # Paladin.
    Abilities.reflect_1: paladin.reflect_1,
    Abilities.reflect_2: paladin.reflect_2,
    Abilities.reflect_3: paladin.reflect_3,
    Abilities.telekinesis_1: paladin.telekinesis_1,
    Abilities.telekinesis_2: paladin.telekinesis_2,
    Abilities.telekinesis_3: paladin.telekinesis_3,
    Abilities.protect_1: paladin.protect_1,
    Abilities.protect_2: paladin.protect_2,
    Abilities.protect_3: paladin.protect_3,
    Abilities.earth_breaker_1: paladin.earth_breaker_1,
    Abilities.earth_breaker_2: paladin.earth_breaker_2,
    Abilities.earth_breaker_3: paladin.earth_breaker_3,
    Abilities.barrier_1: paladin.barrier_1,
    Abilities.barrier_2: paladin.barrier_2,
    Abilities.barrier_3: paladin.barrier_3,
    Abilities.shell_1: paladin.shell_1,
    Abilities.shell_2: paladin.shell_2,
    Abilities.shell_3: paladin.shell_3,
    Abilities.vortex_1: paladin.vortex_1,
    Abilities.vortex_2: paladin.vortex_2,
    Abilities.vortex_3: paladin.vortex_3,
    Abilities.provoke_1: paladin.provoke_1,
    Abilities.provoke_2: paladin.provoke_2,
    Abilities.provoke_3: paladin.provoke_3,
    Abilities.shatter_1: paladin.shatter_1,
    Abilities.shatter_2: paladin.shatter_2,
    Abilities.shatter_3: paladin.shatter_3,
    Abilities.mass_barrier_1: paladin.mass_barrier_1,
    Abilities.mass_barrier_2: paladin.mass_barrier_2,
    Abilities.mass_barrier_3: paladin.mass_barrier_3,
    Abilities.shockwave_1: paladin.shockwave_1,
    Abilities.shockwave_2: paladin.shockwave_2,
    Abilities.shockwave_3: paladin.shockwave_3,
    Abilities.animate_weapon_1: paladin.animate_weapon_1,
    Abilities.animate_weapon_2: paladin.animate_weapon_2,
    Abilities.animate_weapon_3: paladin.animate_weapon_3,
    Abilities.mass_telekinesis_1: paladin.mass_telekinesis_1,
    Abilities.mass_telekinesis_2: paladin.mass_telekinesis_2,
    Abilities.mass_telekinesis_3: paladin.mass_telekinesis_3,
    Abilities.master_telekinetic_1: paladin.master_telekinetic_1,
    Abilities.master_telekinetic_2: paladin.master_telekinetic_2,
    Abilities.master_telekinetic_3: paladin.master_telekinetic_3
}


inverse_abilities = {ability: enum for enum, ability in abilities.items()}
"""Maps abilities to their corresponding enums."""
