from enum import auto, Enum

from .classes import geomancer, magus, marksman, paladin, spectre, telepath, templar, valkyrie


class Abilities(Enum):
    # Paladin.
    reflect_1 = auto()
    reflect_2 = auto()
    reflect_3 = auto()
    telekinesis_1 = auto()
    telekinesis_2 = auto()
    telekinesis_3 = auto()
    protect_1 = auto()
    protect_2 = auto()
    protect_3 = auto()
    earth_breaker_1 = auto()
    earth_breaker_2 = auto()
    earth_breaker_3 = auto()
    barrier_1 = auto()
    barrier_2 = auto()
    barrier_3 = auto()
    shell_1 = auto()
    shell_2 = auto()
    shell_3 = auto()
    vortex_1 = auto()
    vortex_2 = auto()
    vortex_3 = auto()
    provoke_1 = auto()
    provoke_2 = auto()
    provoke_3 = auto()
    shatter_1 = auto()
    shatter_2 = auto()
    shatter_3 = auto()
    mass_barrier_1 = auto()
    mass_barrier_2 = auto()
    mass_barrier_3 = auto()
    shockwave_1 = auto()
    shockwave_2 = auto()
    shockwave_3 = auto()
    animate_weapon_1 = auto()
    animate_weapon_2 = auto()
    animate_weapon_3 = auto()
    mass_telekinesis_1 = auto()
    mass_telekinesis_2 = auto()
    mass_telekinesis_3 = auto()
    master_telekinetic_1 = auto()
    master_telekinetic_2 = auto()
    master_telekinetic_3 = auto()

    # Magus.
    fireball_1 = auto()
    fireball_2 = auto()
    fireball_3 = auto()
    lightning_shield_1 = auto()
    lightning_shield_2 = auto()
    lightning_shield_3 = auto()
    ice_wall_1 = auto()
    ice_wall_2 = auto()
    ice_wall_3 = auto()
    ice_slick_1 = auto()
    ice_slick_2 = auto()
    ice_slick_3 = auto()
    imbue_weapon_1 = auto()
    imbue_weapon_2 = auto()
    imbue_weapon_3 = auto()
    inferno_1 = auto()
    inferno_2 = auto()
    inferno_3 = auto()
    sunray_1 = auto()
    sunray_2 = auto()
    sunray_3 = auto()
    lightning_strike_1 = auto()
    lightning_strike_2 = auto()
    lightning_strike_3 = auto()
    deep_freeze_1 = auto()
    deep_freeze_2 = auto()
    deep_freeze_3 = auto()
    infuse_1 = auto()
    infuse_2 = auto()
    infuse_3 = auto()
    fire_storm_1 = auto()
    fire_storm_2 = auto()
    fire_storm_3 = auto()
    tempest_1 = auto()
    tempest_2 = auto()
    tempest_3 = auto()
    blizzard_1 = auto()
    blizzard_2 = auto()
    blizzard_3 = auto()
    arcane_master_1 = auto()
    arcane_master_2 = auto()
    arcane_master_3 = auto()
    fury_1 = auto()
    fury_2 = auto()
    fury_3 = auto()

    # Templar.
    time_warp_1 = auto()
    time_warp_2 = auto()
    time_warp_3 = auto()
    slow_1 = auto()
    slow_2 = auto()
    slow_3 = auto()
    rebound_1 = auto()
    rebound_2 = auto()
    rebound_3 = auto()
    rapid_regen_1 = auto()
    rapid_regen_2 = auto()
    rapid_regen_3 = auto()
    cure_1 = auto()
    cure_2 = auto()
    cure_3 = auto()
    mass_time_warp_1 = auto()
    mass_time_warp_2 = auto()
    mass_time_warp_3 = auto()
    stop_1 = auto()
    stop_2 = auto()
    stop_3 = auto()
    phase_out_1 = auto()
    phase_out_2 = auto()
    phase_out_3 = auto()
    healing_wind_1 = auto()
    healing_wind_2 = auto()
    healing_wind_3 = auto()
    esuna_1 = auto()
    esuna_2 = auto()
    esuna_3 = auto()
    reset_1 = auto()
    reset_2 = auto()
    reset_3 = auto()
    decay_1 = auto()
    decay_2 = auto()
    decay_3 = auto()
    time_cloud_1 = auto()
    time_cloud_2 = auto()
    time_cloud_3 = auto()
    curaga_1 = auto()
    curaga_2 = auto()
    curaga_3 = auto()
    time_lord_1 = auto()
    time_lord_2 = auto()
    time_lord_3 = auto()

    # Spectre
    invisibility_1 = auto()
    invisibility_2 = auto()
    invisibility_3 = auto()
    blinding_ray_1 = auto()
    blinding_ray_2 = auto()
    blinding_ray_3 = auto()
    trap_1 = auto()
    trap_2 = auto()
    trap_3 = auto()
    darkness_1 = auto()
    darkness_2 = auto()
    darkness_3 = auto()
    spectre_arts_1 = auto()
    spectre_arts_2 = auto()
    spectre_arts_3 = auto()
    mass_invisibility_1 = auto()
    mass_invisibility_2 = auto()
    mass_invisibility_3 = auto()
    farsight_1 = auto()
    farsight_2 = auto()
    farsight_3 = auto()
    large_trap_1 = auto()
    large_trap_2 = auto()
    large_trap_3 = auto()
    sleep_powder_1 = auto()
    sleep_powder_2 = auto()
    sleep_powder_3 = auto()
    teamwork_1 = auto()
    teamwork_2 = auto()
    teamwork_3 = auto()
    colossal_invisibility_1 = auto()
    colossal_invisibility_2 = auto()
    colossal_invisibility_3 = auto()
    star_fire_1 = auto()
    star_fire_2 = auto()
    star_fire_3 = auto()
    dodge_1 = auto()
    dodge_2 = auto()
    dodge_3 = auto()
    phantom_1 = auto()
    phantom_2 = auto()
    phantom_3 = auto()

    # Marksman
    snipe_1 = auto()
    snipe_2 = auto()
    snipe_3 = auto()
    quick_draw_1 = auto()
    quick_draw_2 = auto()
    quick_draw_3 = auto()
    mortar_1 = auto()
    mortar_2 = auto()
    mortar_3 = auto()
    smoke_bomb_1 = auto()
    smoke_bomb_2 = auto()
    smoke_bomb_3 = auto()
    combat_enhancements_1 = auto()
    combat_enhancements_2 = auto()
    combat_enhancements_3 = auto()
    stealth_snipe_1 = auto()
    stealth_snipe_2 = auto()
    stealth_snipe_3 = auto()
    dual_wield_1 = auto()
    dual_wield_2 = auto()
    dual_wield_3 = auto()
    siege_tech_mark_two_1 = auto()
    siege_tech_mark_two_2 = auto()
    siege_tech_mark_two_3 = auto()
    slime_bomb_1 = auto()
    slime_bomb_2 = auto()
    slime_bomb_3 = auto()
    gatling_1 = auto()
    gatling_2 = auto()
    gatling_3 = auto()
    full_luna_jacket_1 = auto()
    full_luna_jacket_2 = auto()
    full_luna_jacket_3 = auto()
    gds_armor_1 = auto()
    gds_armor_2 = auto()
    gds_armor_3 = auto()
    gds_tech_1 = auto()
    gds_tech_2 = auto()
    gds_tech_3 = auto()
    gds_generator_1 = auto()
    gds_generator_2 = auto()
    gds_generator_3 = auto()
    gatling_mark_two_1 = auto()
    gatling_mark_two_2 = auto()
    gatling_mark_two_3 = auto()

    # Telepath.
    jump_1 = auto()
    jump_2 = auto()
    jump_3 = auto()
    telesthesia_1 = auto()
    telesthesia_2 = auto()
    telesthesia_3 = auto()
    confuse_1 = auto()
    confuse_2 = auto()
    confuse_3 = auto()
    parry_1 = auto()
    parry_2 = auto()
    parry_3 = auto()
    synergize_1 = auto()
    synergize_2 = auto()
    synergize_3 = auto()
    hallucinate_1 = auto()
    hallucinate_2 = auto()
    hallucinate_3 = auto()
    telepathy_1 = auto()
    telepathy_2 = auto()
    telepathy_3 = auto()
    flashback_1 = auto()
    flashback_2 = auto()
    flashback_3 = auto()
    synchronize_1 = auto()
    synchronize_2 = auto()
    synchronize_3 = auto()
    shoulder_side_1 = auto()
    shoulder_side_2 = auto()
    shoulder_side_3 = auto()
    numb_1 = auto()
    numb_2 = auto()
    numb_3 = auto()
    dominate_1 = auto()
    dominate_2 = auto()
    dominate_3 = auto()
    mind_cloak_1 = auto()
    mind_cloak_2 = auto()
    mind_cloak_3 = auto()
    psyche_flare_1 = auto()
    psyche_flare_2 = auto()
    psyche_flare_3 = auto()
    mimic_1 = auto()
    mimic_2 = auto()
    mimic_3 = auto()

    # Geomancer.
    taunt_1 = auto()
    taunt_2 = auto()
    taunt_3 = auto()
    charge_1 = auto()
    charge_2 = auto()
    charge_3 = auto()
    heave_1 = auto()
    heave_2 = auto()
    heave_3 = auto()
    ensnare_1 = auto()
    ensnare_2 = auto()
    ensnare_3 = auto()
    lunacite_veins_1 = auto()
    lunacite_veins_2 = auto()
    lunacite_veins_3 = auto()
    tremor_stomp_1 = auto()
    tremor_stomp_2 = auto()
    tremor_stomp_3 = auto()
    rock_wall_1 = auto()
    rock_wall_2 = auto()
    rock_wall_3 = auto()
    emerald_armor_1 = auto()
    emerald_armor_2 = auto()
    emerald_armor_3 = auto()
    revivify_1 = auto()
    revivify_2 = auto()
    revivify_3 = auto()
    viridian_glow_1 = auto()
    viridian_glow_2 = auto()
    viridian_glow_3 = auto()
    rend_1 = auto()
    rend_2 = auto()
    rend_3 = auto()
    quake_1 = auto()
    quake_2 = auto()
    quake_3 = auto()
    rage_1 = auto()
    rage_2 = auto()
    rage_3 = auto()
    mass_revivify_1 = auto()
    mass_revivify_2 = auto()
    mass_revivify_3 = auto()
    petrify_1 = auto()
    petrify_2 = auto()
    petrify_3 = auto()

    # Valkeryie
    fly_1 = auto()
    fly_2 = auto()
    fly_3 = auto()
    blink_1 = auto()
    blink_2 = auto()
    blink_3 = auto()
    gale_1 = auto()
    gale_2 = auto()
    gale_3 = auto()
    piercing_shot_1 = auto()
    piercing_shot_2 = auto()
    piercing_shot_3 = auto()
    wind_stride_1 = auto()
    wind_stride_2 = auto()
    wind_stride_3 = auto()
    mass_fly_1 = auto()
    mass_fly_2 = auto()
    mass_fly_3 = auto()
    mass_blink_1 = auto()
    mass_blink_2 = auto()
    mass_blink_3 = auto()
    counter_blink_1 = auto()
    counter_blink_2 = auto()
    counter_blink_3 = auto()
    cyclone_1 = auto()
    cyclone_2 = auto()
    cyclone_3 = auto()
    ricochet_1 = auto()
    ricochet_2 = auto()
    ricochet_3 = auto()
    refreshing_breeze_1 = auto()
    refreshing_breeze_2 = auto()
    refreshing_breeze_3 = auto()
    cloud_soar_1 = auto()
    cloud_soar_2 = auto()
    cloud_soar_3 = auto()
    teleport_1 = auto()
    teleport_2 = auto()
    teleport_3 = auto()
    sky_watch_1 = auto()
    sky_watch_2 = auto()
    sky_watch_3 = auto()


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
    Abilities.tempest_1: magus.tempest_1,
    Abilities.tempest_2: magus.tempest_2,
    Abilities.tempest_3: magus.tempest_3,
    Abilities.blizzard_1: magus.blizzard_1,
    Abilities.blizzard_2: magus.blizzard_2,
    Abilities.blizzard_3: magus.blizzard_3,
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

    # Telepath.
    Abilities.jump_1: telepath.jump_1,
    Abilities.jump_2: telepath.jump_2,
    Abilities.jump_3: telepath.jump_3,
    Abilities.telesthesia_1: telepath.telesthesia_1,
    Abilities.telesthesia_2: telepath.telesthesia_2,
    Abilities.telesthesia_3: telepath.telesthesia_3,
    Abilities.confuse_1: telepath.confuse_1,
    Abilities.confuse_2: telepath.confuse_2,
    Abilities.confuse_3: telepath.confuse_3,
    Abilities.parry_1: telepath.parry_1,
    Abilities.parry_2: telepath.parry_2,
    Abilities.parry_3: telepath.parry_3,
    Abilities.synergize_1: telepath.synergize_1,
    Abilities.synergize_2: telepath.synergize_2,
    Abilities.synergize_3: telepath.synergize_3,
    Abilities.hallucinate_1: telepath.hallucinate_1,
    Abilities.hallucinate_2: telepath.hallucinate_2,
    Abilities.hallucinate_3: telepath.hallucinate_3,
    Abilities.telepathy_1: telepath.telepathy_1,
    Abilities.telepathy_2: telepath.telepathy_2,
    Abilities.telepathy_3: telepath.telepathy_3,
    Abilities.flashback_1: telepath.flashback_1,
    Abilities.flashback_2: telepath.flashback_2,
    Abilities.flashback_3: telepath.flashback_3,
    Abilities.synchronize_1: telepath.synchronize_1,
    Abilities.synchronize_2: telepath.synchronize_2,
    Abilities.synchronize_3: telepath.synchronize_3,
    Abilities.shoulder_side_1: telepath.shoulder_side_1,
    Abilities.shoulder_side_2: telepath.shoulder_side_2,
    Abilities.shoulder_side_3: telepath.shoulder_side_3,
    Abilities.numb_1: telepath.numb_1,
    Abilities.numb_2: telepath.numb_2,
    Abilities.numb_3: telepath.numb_3,
    Abilities.dominate_1: telepath.dominate_1,
    Abilities.dominate_2: telepath.dominate_2,
    Abilities.dominate_3: telepath.dominate_3,
    Abilities.mind_cloak_1: telepath.mind_cloak_1,
    Abilities.mind_cloak_2: telepath.mind_cloak_2,
    Abilities.mind_cloak_3: telepath.mind_cloak_3,
    Abilities.psyche_flare_1: telepath.psyche_flare_1,
    Abilities.psyche_flare_2: telepath.psyche_flare_2,
    Abilities.psyche_flare_3: telepath.psyche_flare_3,
    Abilities.mimic_1: telepath.mimic_1,
    Abilities.mimic_2: telepath.mimic_2,
    Abilities.mimic_3: telepath.mimic_3,

    # Geomancer.
    Abilities.taunt_1: geomancer.taunt_1,
    Abilities.taunt_2: geomancer.taunt_2,
    Abilities.taunt_3: geomancer.taunt_3,
    Abilities.charge_1: geomancer.charge_1,
    Abilities.charge_2: geomancer.charge_2,
    Abilities.charge_3: geomancer.charge_3,
    Abilities.heave_1: geomancer.heave_1,
    Abilities.heave_2: geomancer.heave_2,
    Abilities.heave_3: geomancer.heave_3,
    Abilities.ensnare_1: geomancer.ensnare_1,
    Abilities.ensnare_2: geomancer.ensnare_2,
    Abilities.ensnare_3: geomancer.ensnare_3,
    Abilities.lunacite_veins_1: geomancer.lunacite_veins_1,
    Abilities.lunacite_veins_2: geomancer.lunacite_veins_2,
    Abilities.lunacite_veins_3: geomancer.lunacite_veins_3,
    Abilities.tremor_stomp_1: geomancer.tremor_stomp_1,
    Abilities.tremor_stomp_2: geomancer.tremor_stomp_2,
    Abilities.tremor_stomp_3: geomancer.tremor_stomp_3,
    Abilities.rock_wall_1: geomancer.rock_wall_1,
    Abilities.rock_wall_2: geomancer.rock_wall_2,
    Abilities.rock_wall_3: geomancer.rock_wall_3,
    Abilities.emerald_armor_1: geomancer.emerald_armor_1,
    Abilities.emerald_armor_2: geomancer.emerald_armor_2,
    Abilities.emerald_armor_3: geomancer.emerald_armor_3,
    Abilities.revivify_1: geomancer.revivify_1,
    Abilities.revivify_2: geomancer.revivify_2,
    Abilities.revivify_3: geomancer.revivify_3,
    Abilities.viridian_glow_1: geomancer.viridian_glow_1,
    Abilities.viridian_glow_2: geomancer.viridian_glow_2,
    Abilities.viridian_glow_3: geomancer.viridian_glow_3,
    Abilities.rend_1: geomancer.rend_1,
    Abilities.rend_2: geomancer.rend_2,
    Abilities.rend_3: geomancer.rend_3,
    Abilities.quake_1: geomancer.quake_1,
    Abilities.quake_2: geomancer.quake_2,
    Abilities.quake_3: geomancer.quake_3,
    Abilities.rage_1: geomancer.rage_1,
    Abilities.rage_2: geomancer.rage_2,
    Abilities.rage_3: geomancer.rage_3,
    Abilities.mass_revivify_1: geomancer.mass_revivify_1,
    Abilities.mass_revivify_2: geomancer.mass_revivify_2,
    Abilities.mass_revivify_3: geomancer.mass_revivify_3,
    Abilities.petrify_1: geomancer.petrify_1,
    Abilities.petrify_2: geomancer.petrify_2,
    Abilities.petrify_3: geomancer.petrify_3,

    # Valkeryie.
    Abilities.fly_1: valkyrie.fly_1,
    Abilities.fly_2: valkyrie.fly_2,
    Abilities.fly_3: valkyrie.fly_3,
    Abilities.blink_1: valkyrie.blink_1,
    Abilities.blink_2: valkyrie.blink_2,
    Abilities.blink_3: valkyrie.blink_3,
    Abilities.gale_1: valkyrie.gale_1,
    Abilities.gale_2: valkyrie.gale_2,
    Abilities.gale_3: valkyrie.gale_3,
    Abilities.piercing_shot_1: valkyrie.piercing_shot_1,
    Abilities.piercing_shot_2: valkyrie.piercing_shot_2,
    Abilities.piercing_shot_3: valkyrie.piercing_shot_3,
    Abilities.wind_stride_1: valkyrie.wind_stride_1,
    Abilities.wind_stride_2: valkyrie.wind_stride_2,
    Abilities.wind_stride_3: valkyrie.wind_stride_3,
    Abilities.mass_fly_1: valkyrie.mass_fly_1,
    Abilities.mass_fly_2: valkyrie.mass_fly_2,
    Abilities.mass_fly_3: valkyrie.mass_fly_3,
    Abilities.mass_blink_1: valkyrie.mass_blink_1,
    Abilities.mass_blink_2: valkyrie.mass_blink_2,
    Abilities.mass_blink_3: valkyrie.mass_blink_3,
    Abilities.counter_blink_1: valkyrie.counter_blink_1,
    Abilities.counter_blink_2: valkyrie.counter_blink_2,
    Abilities.counter_blink_3: valkyrie.counter_blink_3,
    Abilities.cyclone_1: valkyrie.cyclone_1,
    Abilities.cyclone_2: valkyrie.cyclone_2,
    Abilities.cyclone_3: valkyrie.cyclone_3,
    Abilities.ricochet_1: valkyrie.ricochet_1,
    Abilities.ricochet_2: valkyrie.ricochet_2,
    Abilities.ricochet_3: valkyrie.ricochet_3,
    Abilities.refreshing_breeze_1: valkyrie.refreshing_breeze_1,
    Abilities.refreshing_breeze_2: valkyrie.refreshing_breeze_2,
    Abilities.refreshing_breeze_3: valkyrie.refreshing_breeze_3,
    Abilities.cloud_soar_1: valkyrie.cloud_soar_1,
    Abilities.cloud_soar_2: valkyrie.cloud_soar_2,
    Abilities.cloud_soar_3: valkyrie.cloud_soar_3,
    Abilities.teleport_1: valkyrie.teleport_1,
    Abilities.teleport_2: valkyrie.teleport_2,
    Abilities.teleport_3: valkyrie.teleport_3,
    Abilities.sky_watch_1: valkyrie.sky_watch_1,
    Abilities.sky_watch_2: valkyrie.sky_watch_2,
    Abilities.sky_watch_3: valkyrie.sky_watch_3,
}

inverse_abilities = {ability: enum for enum, ability in abilities.items()}
"""Maps abilities to their corresponding enums."""
