from numbers import Real

import aenum

from .classes import magus, marksman, paladin, spectre, templar


def round_up(num: Real) -> int:
    """Add a small epsilon in order to force .5 values to round up."""
    return round(num + 1e-8)


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

    # Magus.
    fireball_1 = ()
    fireball_2 = ()
    fireball_3 = ()
    lightning_shield_1 = ()
    lightning_shield_2 = ()
    lightning_shield_3 = ()
    ice_wall_1 = ()
    ice_wall_2 = ()
    ice_wall_3 = ()
    ice_slick_1 = ()
    ice_slick_2 = ()
    ice_slick_3 = ()
    imbue_weapon_1 = ()
    imbue_weapon_2 = ()
    imbue_weapon_3 = ()
    inferno_1 = ()
    inferno_2 = ()
    inferno_3 = ()
    sunray_1 = ()
    sunray_2 = ()
    sunray_3 = ()
    lightning_strike_1 = ()
    lightning_strike_2 = ()
    lightning_strike_3 = ()
    deep_freeze_1 = ()
    deep_freeze_2 = ()
    deep_freeze_3 = ()
    infuse_1 = ()
    infuse_2 = ()
    infuse_3 = ()
    fire_storm_1 = ()
    fire_storm_2 = ()
    fire_storm_3 = ()
    thunder_cloud_1 = ()
    thunder_cloud_2 = ()
    thunder_cloud_3 = ()
    ice_wind_1 = ()
    ice_wind_2 = ()
    ice_wind_3 = ()
    arcane_master_1 = ()
    arcane_master_2 = ()
    arcane_master_3 = ()
    fury_1 = ()
    fury_2 = ()
    fury_3 = ()

    # Templar.
    time_warp_1 = ()
    time_warp_2 = ()
    time_warp_3 = ()
    slow_1 = ()
    slow_2 = ()
    slow_3 = ()
    rebound_1 = ()
    rebound_2 = ()
    rebound_3 = ()
    rapid_regen_1 = ()
    rapid_regen_2 = ()
    rapid_regen_3 = ()
    cure_1 = ()
    cure_2 = ()
    cure_3 = ()
    mass_time_warp_1 = ()
    mass_time_warp_2 = ()
    mass_time_warp_3 = ()
    stop_1 = ()
    stop_2 = ()
    stop_3 = ()
    phase_out_1 = ()
    phase_out_2 = ()
    phase_out_3 = ()
    healing_wind_1 = ()
    healing_wind_2 = ()
    healing_wind_3 = ()
    esuna_1 = ()
    esuna_2 = ()
    esuna_3 = ()
    reset_1 = ()
    reset_2 = ()
    reset_3 = ()
    decay_1 = ()
    decay_2 = ()
    decay_3 = ()
    time_cloud_1 = ()
    time_cloud_2 = ()
    time_cloud_3 = ()
    curaga_1 = ()
    curaga_2 = ()
    curaga_3 = ()
    time_lord_1 = ()
    time_lord_2 = ()
    time_lord_3 = ()

    # Spectre
    invisibility_1 = ()
    invisibility_2 = ()
    invisibility_3 = ()
    blinding_ray_1 = ()
    blinding_ray_2 = ()
    blinding_ray_3 = ()
    trap_1 = ()
    trap_2 = ()
    trap_3 = ()
    darkness_1 = ()
    darkness_2 = ()
    darkness_3 = ()
    spectre_arts_1 = ()
    spectre_arts_2 = ()
    spectre_arts_3 = ()
    mass_invisibility_1 = ()
    mass_invisibility_2 = ()
    mass_invisibility_3 = ()
    farsight_1 = ()
    farsight_2 = ()
    farsight_3 = ()
    large_trap_1 = ()
    large_trap_2 = ()
    large_trap_3 = ()
    sleep_powder_1 = ()
    sleep_powder_2 = ()
    sleep_powder_3 = ()
    teamwork_1 = ()
    teamwork_2 = ()
    teamwork_3 = ()
    colossal_invisibility_1 = ()
    colossal_invisibility_2 = ()
    colossal_invisibility_3 = ()
    star_fire_1 = ()
    star_fire_2 = ()
    star_fire_3 = ()
    dodge_1 = ()
    dodge_2 = ()
    dodge_3 = ()
    phantom_1 = ()
    phantom_2 = ()
    phantom_3 = ()

    # Marksman
    snipe_1 = ()
    snipe_2 = ()
    snipe_3 = ()
    quick_draw_1 = ()
    quick_draw_2 = ()
    quick_draw_3 = ()
    mortar_1 = ()
    mortar_2 = ()
    mortar_3 = ()
    smoke_bomb_1 = ()
    smoke_bomb_2 = ()
    smoke_bomb_3 = ()
    combat_enhancements_1 = ()
    combat_enhancements_2 = ()
    combat_enhancements_3 = ()
    stealth_snipe_1 = ()
    stealth_snipe_2 = ()
    stealth_snipe_3 = ()
    dual_wield_1 = ()
    dual_wield_2 = ()
    dual_wield_3 = ()
    siege_tech_mark_two_1 = ()
    siege_tech_mark_two_2 = ()
    siege_tech_mark_two_3 = ()
    slime_bomb_1 = ()
    slime_bomb_2 = ()
    slime_bomb_3 = ()
    gatling_1 = ()
    gatling_2 = ()
    gatling_3 = ()
    full_luna_jacket_1 = ()
    full_luna_jacket_2 = ()
    full_luna_jacket_3 = ()
    gds_armor_1 = ()
    gds_armor_2 = ()
    gds_armor_3 = ()
    gds_tech_1 = ()
    gds_tech_2 = ()
    gds_tech_3 = ()
    gds_generator_1 = ()
    gds_generator_2 = ()
    gds_generator_3 = ()
    gatling_mark_two_1 = ()
    gatling_mark_two_2 = ()
    gatling_mark_two_3 = ()

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
    Abilities.master_telekinetic_3: paladin.master_telekinetic_3,

    # Magus.
    Abilities.fireball_1: magus.fireball_1,
    Abilities.fireball_2: magus.fireball_2,
    Abilities.fireball_3: magus.fireball_3,
    Abilities.lightning_shield_1: magus.lightning_shield_1,
    Abilities.lightning_shield_2: magus.lightning_shield_2,
    Abilities.lightning_shield_3: magus.lightning_shield_3,
    Abilities.ice_wall_1: magus.ice_wall_1,
    Abilities.ice_wall_2: magus.ice_wall_2,
    Abilities.ice_wall_3: magus.ice_wall_3,
    Abilities.ice_slick_1: magus.ice_slick_1,
    Abilities.ice_slick_2: magus.ice_slick_2,
    Abilities.ice_slick_3: magus.ice_slick_3,
    Abilities.imbue_weapon_1: magus.imbue_weapon_1,
    Abilities.imbue_weapon_2: magus.imbue_weapon_2,
    Abilities.imbue_weapon_3: magus.imbue_weapon_3,
    Abilities.inferno_1: magus.inferno_1,
    Abilities.inferno_2: magus.inferno_2,
    Abilities.inferno_3: magus.inferno_3,
    Abilities.sunray_1: magus.sunray_1,
    Abilities.sunray_2: magus.sunray_2,
    Abilities.sunray_3: magus.sunray_3,
    Abilities.lightning_strike_1: magus.lightning_strike_1,
    Abilities.lightning_strike_2: magus.lightning_strike_2,
    Abilities.lightning_strike_3: magus.lightning_strike_3,
    Abilities.deep_freeze_1: magus.deep_freeze_1,
    Abilities.deep_freeze_2: magus.deep_freeze_2,
    Abilities.deep_freeze_3: magus.deep_freeze_3,
    Abilities.infuse_1: magus.infuse_1,
    Abilities.infuse_2: magus.infuse_2,
    Abilities.infuse_3: magus.infuse_3,
    Abilities.fire_storm_1: magus.fire_storm_1,
    Abilities.fire_storm_2: magus.fire_storm_2,
    Abilities.fire_storm_3: magus.fire_storm_3,
    Abilities.thunder_cloud_1: magus.thunder_cloud_1,
    Abilities.thunder_cloud_2: magus.thunder_cloud_2,
    Abilities.thunder_cloud_3: magus.thunder_cloud_3,
    Abilities.ice_wind_1: magus.ice_wind_1,
    Abilities.ice_wind_2: magus.ice_wind_2,
    Abilities.ice_wind_3: magus.ice_wind_3,
    Abilities.arcane_master_1: magus.arcane_master_1,

    # Templar.
    Abilities.time_warp_1: templar.time_warp_1,
    Abilities.time_warp_2: templar.time_warp_2,
    Abilities.time_warp_3: templar.time_warp_3,
    Abilities.slow_1: templar.slow_1,
    Abilities.slow_2: templar.slow_2,
    Abilities.slow_3: templar.slow_3,
    Abilities.rebound_1: templar.rebound_1,
    Abilities.rebound_2: templar.rebound_2,
    Abilities.rebound_3: templar.rebound_3,
    Abilities.rapid_regen_1: templar.rapid_regen_1,
    Abilities.rapid_regen_2: templar.rapid_regen_2,
    Abilities.rapid_regen_3: templar.rapid_regen_3,
    Abilities.cure_1: templar.cure_1,
    Abilities.cure_2: templar.cure_2,
    Abilities.cure_3: templar.cure_3,
    Abilities.mass_time_warp_1: templar.mass_time_warp_1,
    Abilities.mass_time_warp_2: templar.mass_time_warp_2,
    Abilities.mass_time_warp_3: templar.mass_time_warp_3,
    Abilities.stop_1: templar.stop_1,
    Abilities.stop_2: templar.stop_2,
    Abilities.stop_3: templar.stop_3,
    Abilities.phase_out_1: templar.destiny_1,
    Abilities.phase_out_2: templar.destiny_2,
    Abilities.phase_out_3: templar.destiny_3,
    Abilities.healing_wind_1: templar.healing_wind_1,
    Abilities.healing_wind_2: templar.healing_wind_2,
    Abilities.healing_wind_3: templar.healing_wind_3,
    Abilities.esuna_1: templar.esuna_1,
    Abilities.esuna_2: templar.esuna_2,
    Abilities.esuna_3: templar.esuna_3,
    Abilities.reset_1: templar.reset_1,
    Abilities.reset_2: templar.reset_2,
    Abilities.reset_3: templar.reset_3,
    Abilities.decay_1: templar.decay_1,
    Abilities.decay_2: templar.decay_2,
    Abilities.decay_3: templar.decay_3,
    Abilities.time_cloud_1: templar.time_cloud_1,
    Abilities.time_cloud_2: templar.time_cloud_2,
    Abilities.time_cloud_3: templar.time_cloud_3,
    Abilities.curaga_1: templar.curaga_1,
    Abilities.curaga_2: templar.curaga_2,
    Abilities.curaga_3: templar.curaga_3,
    Abilities.time_lord_1: templar.time_lord_1,
    Abilities.time_lord_2: templar.time_lord_2,
    Abilities.time_lord_3: templar.time_lord_3,

    # Spectre.
    Abilities.invisibility_1: spectre.invisibility_1,
    Abilities.invisibility_2: spectre.invisibility_2,
    Abilities.invisibility_3: spectre.invisibility_3,
    Abilities.blinding_ray_1: spectre.blinding_ray_1,
    Abilities.blinding_ray_2: spectre.blinding_ray_2,
    Abilities.blinding_ray_3: spectre.blinding_ray_3,
    Abilities.trap_1: spectre.trap_1,
    Abilities.trap_2: spectre.trap_2,
    Abilities.trap_3: spectre.trap_3,
    Abilities.darkness_1: spectre.darkness_1,
    Abilities.darkness_2: spectre.darkness_2,
    Abilities.darkness_3: spectre.darkness_3,
    Abilities.spectre_arts_1: spectre.spectre_arts_1,
    Abilities.spectre_arts_2: spectre.spectre_arts_2,
    Abilities.spectre_arts_3: spectre.spectre_arts_3,
    Abilities.mass_invisibility_1: spectre.mass_invisibility_1,
    Abilities.mass_invisibility_2: spectre.mass_invisibility_2,
    Abilities.mass_invisibility_3: spectre.mass_invisibility_3,
    Abilities.farsight_1: spectre.farsight_1,
    Abilities.farsight_2: spectre.farsight_2,
    Abilities.farsight_3: spectre.farsight_3,
    Abilities.large_trap_1: spectre.large_trap_1,
    Abilities.large_trap_2: spectre.large_trap_2,
    Abilities.large_trap_3: spectre.large_trap_3,
    Abilities.sleep_powder_1: spectre.sleep_powder_1,
    Abilities.sleep_powder_2: spectre.sleep_powder_2,
    Abilities.sleep_powder_3: spectre.sleep_powder_3,
    Abilities.teamwork_1: spectre.teamwork_1,
    Abilities.teamwork_2: spectre.teamwork_2,
    Abilities.teamwork_3: spectre.teamwork_3,
    Abilities.colossal_invisibility_1: spectre.colossal_invisibility_1,
    Abilities.colossal_invisibility_2: spectre.colossal_invisibility_2,
    Abilities.colossal_invisibility_3: spectre.colossal_invisibility_3,
    Abilities.star_fire_1: spectre.star_fire_1,
    Abilities.star_fire_2: spectre.star_fire_2,
    Abilities.star_fire_3: spectre.star_fire_3,
    Abilities.dodge_1: spectre.dodge_1,
    Abilities.dodge_2: spectre.dodge_2,
    Abilities.dodge_3: spectre.dodge_3,
    Abilities.phantom_1: spectre.phantom_1,
    Abilities.phantom_2: spectre.phantom_2,
    Abilities.phantom_3: spectre.phantom_3,

    # Marksman.
    Abilities.snipe_1: marksman.snipe_1,
    Abilities.snipe_2: marksman.snipe_2,
    Abilities.snipe_3: marksman.snipe_3,
    Abilities.quick_draw_1: marksman.quick_draw_1,
    Abilities.quick_draw_2: marksman.quick_draw_2,
    Abilities.quick_draw_3: marksman.quick_draw_3,
    Abilities.mortar_1: marksman.mortar_1,
    Abilities.mortar_2: marksman.mortar_2,
    Abilities.mortar_3: marksman.mortar_3,
    Abilities.smoke_bomb_1: marksman.smoke_bomb_1,
    Abilities.smoke_bomb_2: marksman.smoke_bomb_2,
    Abilities.smoke_bomb_3: marksman.smoke_bomb_3,
    Abilities.combat_enhancements_1: marksman.combat_enhancements_1,
    Abilities.combat_enhancements_2: marksman.combat_enhancements_2,
    Abilities.combat_enhancements_3: marksman.combat_enhancements_3,
    Abilities.stealth_snipe_1: marksman.stealth_snipe_1,
    Abilities.stealth_snipe_2: marksman.stealth_snipe_2,
    Abilities.stealth_snipe_3: marksman.stealth_snipe_3,
    Abilities.dual_wield_1: marksman.dual_wield_1,
    Abilities.dual_wield_2: marksman.dual_wield_2,
    Abilities.dual_wield_3: marksman.dual_wield_3,
    Abilities.siege_tech_mark_two_1: marksman.siege_tech_mark_two_1,
    Abilities.siege_tech_mark_two_2: marksman.siege_tech_mark_two_2,
    Abilities.siege_tech_mark_two_3: marksman.siege_tech_mark_two_3,
    Abilities.slime_bomb_1: marksman.slime_bomb_1,
    Abilities.slime_bomb_2: marksman.slime_bomb_2,
    Abilities.slime_bomb_3: marksman.slime_bomb_3,
    Abilities.gatling_1: marksman.gatling_1,
    Abilities.gatling_2: marksman.gatling_2,
    Abilities.gatling_3: marksman.gatling_3,
    Abilities.full_luna_jacket_1: marksman.full_luna_jacket_1,
    Abilities.full_luna_jacket_2: marksman.full_luna_jacket_2,
    Abilities.full_luna_jacket_3: marksman.full_luna_jacket_3,
    Abilities.gds_armor_1: marksman.gds_armor_1,
    Abilities.gds_armor_2: marksman.gds_armor_2,
    Abilities.gds_armor_3: marksman.gds_armor_3,
    Abilities.gds_tech_1: marksman.gds_tech_1,
    Abilities.gds_tech_2: marksman.gds_tech_2,
    Abilities.gds_tech_3: marksman.gds_tech_3,
    Abilities.gds_generator_1: marksman.gds_generator_1,
    Abilities.gds_generator_2: marksman.gds_generator_2,
    Abilities.gds_generator_3: marksman.gds_generator_3,
    Abilities.gatling_mark_two_1: marksman.gatling_mark_two_1,
    Abilities.gatling_mark_two_2: marksman.gatling_mark_two_2,
    Abilities.gatling_mark_two_3: marksman.gatling_mark_two_3,
}

inverse_abilities = {ability: enum for enum, ability in abilities.items()}
"""Maps abilities to their corresponding enums."""
