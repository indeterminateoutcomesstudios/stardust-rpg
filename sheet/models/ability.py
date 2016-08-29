import enum
from typing import Tuple

from . import macro
from .equipment import DamageType, Shape


@enum.unique
class AbilityPicture(enum.Enum):
    adloquium = ('http://img1.wikia.nocookie.net/__cb20140918073139/finalfantasy/images/f/f0/'
                 'FFXIV_Adloquium_Icon.png')
    aeolian_edge = ('http://img2.wikia.nocookie.net/__cb20141208222247/finalfantasy/images/d/d0/'
                    'FFXIV_Aeolian_Edge_Icon.png')
    aero = ('http://img1.wikia.nocookie.net/__cb20140918232722/finalfantasy/images/f/f4/'
            'FFXIV_Aero_Icon.png')
    aero_2 = ('http://img1.wikia.nocookie.net/__cb20141208210816/finalfantasy/images/d/de/'
              'FFXIV_Aetherflow_Icon.png')
    aetherial_manipulation = ('http://img3.wikia.nocookie.net/__cb20141208212454/finalfantasy/'
                              'images/1/14/FFXIV_Aetherial_Manipulation_Icon.png')
    apocatastasis = ('http://img2.wikia.nocookie.net/__cb20141208212450/finalfantasy/images/b/b2/'
                     'FFXIV_Apocatastasis_Icon.png')
    arm_of_the_destroyer = ('http://img3.wikia.nocookie.net/__cb20141208215622/finalfantasy/'
                            'images/9/99/FFXIV_Arm_of_the_Destroyer_Icon.png')
    armys_paeon = ('http://img1.wikia.nocookie.net/__cb20141208212010/finalfantasy/images/0/04/'
                   'FFXIV_Army%27s_Paeon_Icon.png')
    arr_freeze = ('http://img4.wikia.nocookie.net/__cb20140918071701/finalfantasy/images/a/ae/'
                  'FFXIV_ARR_Freeze_Icon.png')
    assassinate = ('http://img3.wikia.nocookie.net/__cb20141208222247/finalfantasy/images/3/36/'
                   'FFXIV_Assassinate_Icon.png')
    awareness = ('http://img2.wikia.nocookie.net/__cb20141208214709/finalfantasy/images/9/9d/'
                 'FFXIV_Awareness_Icon.png')
    bane = ('http://img2.wikia.nocookie.net/__cb20141208211334/finalfantasy/images/2/2f/'
            'FFXIV_Bane_Icon.png')
    barrage = ('http://img2.wikia.nocookie.net/__cb20141208212006/finalfantasy/images/d/dd/'
               'FFXIV_Barrage_Icon.png')
    battle_voice = ('http://img4.wikia.nocookie.net/__cb20141208212010/finalfantasy/images/6/60/'
                    'FFXIV_Battle_Voice_Icon.png')
    berserk = ('http://img3.wikia.nocookie.net/__cb20141208213947/finalfantasy/images/9/98/'
               'FFXIV_Berserk_Icon.png')
    benediction = ('http://vignette3.wikia.nocookie.net/finalfantasy/images/9/9a/'
                   'FFXIV_Benediction_Icon.png')
    bio = ('http://img4.wikia.nocookie.net/__cb20140918234700/finalfantasy/images/c/ce/'
           'FFXIV_Bio_Icon.png')
    bio_2 = ('http://img3.wikia.nocookie.net/__cb20140918072432/finalfantasy/images/f/fd/'
             'Bio_II_Icon.png')
    blizzard = ('http://img4.wikia.nocookie.net/__cb20140918072426/finalfantasy/images/d/dd/'
                'FFXIV_Blizzard_Icon.png')
    blizzard_2 = ('http://img1.wikia.nocookie.net/__cb20140918071702/finalfantasy/images/0/01/'
                  'FFXIVARR_Blizzard_II_Icon.png')
    blizzard_3 = ('http://img4.wikia.nocookie.net/__cb20140918071702/finalfantasy/images/7/7d/'
                  'FFXIVARR_Blizzard_III_Icon.png')
    blood_for_blood = ('http://img3.wikia.nocookie.net/__cb20141208213309/finalfantasy/images/'
                       'a/a9/FFXIV_Blood_for_Blood_Icon.png')
    blood_bath = ('http://img2.wikia.nocookie.net/__cb20141208213544/finalfantasy/images/0/0a/'
                  'FFXIV_Bloodbath_Icon.png')
    blood_letter = ('http://img1.wikia.nocookie.net/__cb20141208211707/finalfantasy/images/1/1a/'
                    'FFXIV_Bloodletter_Icon.png')
    blunt_arrow = ('http://img3.wikia.nocookie.net/__cb20141208212007/finalfantasy/images/3/37/'
                   'FFXIV_Blunt_Arrow_Icon.png')
    boot_shine = ('http://img2.wikia.nocookie.net/__cb20141208215347/finalfantasy/images/9/93/'
                  'FFXIV_Bootshine_Icon.png')
    brutal_swing = ('http://img2.wikia.nocookie.net/__cb20141208213545/finalfantasy/images/a/a7/'
                    'FFXIV_Brutal_Swing_Icon.png')
    bulwark = ('http://img4.wikia.nocookie.net/__cb20141208214712/finalfantasy/images/e/e8/'
               'FFXIV_Bulwark_Icon.png')
    butchers_block = ('http://img1.wikia.nocookie.net/__cb20141208213948/finalfantasy/images/2/22/'
                      'FFXIV_Butcher%27s_Block_Icon.png')
    chaos_thrust = ('http://img2.wikia.nocookie.net/__cb20141208213542/finalfantasy/images/7/72/'
                    'FFXIV_Chaos_Thrust_Icon.png')
    chi = ('http://img3.wikia.nocookie.net/__cb20141208222248/finalfantasy/images/2/2e/'
           'FFXIV_Chi_Icon.png')
    circle_of_scorn = ('http://img2.wikia.nocookie.net/__cb20141208214712/finalfantasy/images/'
                       '8/8b/FFXIV_Circle_of_Scorn_Icon.png')
    cleric_stance = ('http://img3.wikia.nocookie.net/__cb20140920071554/finalfantasy/images/2/2f/'
                     'FFXIV_Cleric_Stance_Icon.png')
    convalescence = ('http://img3.wikia.nocookie.net/__cb20141208214253/finalfantasy/images/f/fc/'
                     'FFXIV_Convalescence_Icon.png')
    convert = ('http://img2.wikia.nocookie.net/__cb20141208212450/finalfantasy/images/5/54/'
               'FFXIV_Convert_Icon.png')
    cover = ('http://img1.wikia.nocookie.net/__cb20141208214836/finalfantasy/images/8/81/'
             'FFXIV_Cover_Icon.png')
    cure = ('http://img4.wikia.nocookie.net/__cb20140920071554/finalfantasy/images/f/f0/'
            'FFXIVARR_Cure_Icon.png')
    cure_2 = ('http://img2.wikia.nocookie.net/__cb20140918070722/finalfantasy/images/c/c2/'
              'FFXIV_Cure_II_Icon.png')
    cure_3 = ('http://img2.wikia.nocookie.net/__cb20140918070721/finalfantasy/images/6/6a/'
              'Cure_III_Icon.png')
    dancing_edge = ('http://img1.wikia.nocookie.net/__cb20141208222248/finalfantasy/images/a/a3/'
                    'FFXIV_Dancing_Edge_Icon.png')
    death_blossom = ('http://img1.wikia.nocookie.net/__cb20141208222248/finalfantasy/images/a/aa/'
                     'FFXIV_Death_Blossom_Icon.png')
    defiance = ('http://img4.wikia.nocookie.net/__cb20141208213951/finalfantasy/images/1/1a/'
                'FFXIV_Defiance_Icon.png')
    demolish = ('http://img4.wikia.nocookie.net/__cb20141208215622/finalfantasy/images/e/e9/'
                'FFXIV_Demolish_Icon.png')
    disembowel = ('http://img3.wikia.nocookie.net/__cb20141208213310/finalfantasy/images/d/d1/'
                  'FFXIV_Disembowel_Icon.png')
    divine_seal = ('http://img2.wikia.nocookie.net/__cb20141208212948/finalfantasy/images/1/1c/'
                   'FFXIV_Divine_Seal_Icon.png')
    doom_spike = ('http://img1.wikia.nocookie.net/__cb20141208213310/finalfantasy/images/6/6f/'
                  'FFXIV_Doom_Spike_Icon.png')
    doton = ('http://img4.wikia.nocookie.net/__cb20141208222249/finalfantasy/images/6/63/'
             'FFXIV_Doton_Icon.png')
    dragon_kick = ('http://img4.wikia.nocookie.net/__cb20141008060613/finalfantasy/images/f/f6/'
                   'FFXIV_Dragon_Kick_Icon.png')
    dragon_fire_dive = ('http://img1.wikia.nocookie.net/__cb20141006231908/finalfantasy/images/'
                        'e/ea/FFXIV_Dragonfire_Dive_Icon.png')
    elusive_jump = ('http://img3.wikia.nocookie.net/__cb20141208212951/finalfantasy/images/d/d3/'
                    'FFXIV_Elusive_Jump_Icon.png')
    energy_drain = ('http://img3.wikia.nocookie.net/__cb20141208210817/finalfantasy/images/5/59/'
                    'FFXIV_Energy_Drain_Icon.png')
    enkindle = ('http://img4.wikia.nocookie.net/__cb20141208210815/finalfantasy/images/d/d6/'
                'FFXIV_Enkindle_Icon.png')
    esuna = ('http://img4.wikia.nocookie.net/__cb20140920071556/finalfantasy/images/3/31/'
             'FFXIVARR_Esuna_icon.png')
    eye_for_an_eye = ('http://img2.wikia.nocookie.net/__cb20141018051706/finalfantasy/images/f/fd/'
                      'FFXIV_Eye_for_an_Eye_Icon.png')
    fast_blade = ('http://img1.wikia.nocookie.net/__cb20141208214251/finalfantasy/images/9/9b/'
                  'FFXIV_Fast_Blade_Icon.png')
    feather_foot = ('http://img3.wikia.nocookie.net/__cb20141208215348/finalfantasy/images/1/1e/'
                    'FFXIV_Featherfoot_Icon.png')
    feint = ('http://img1.wikia.nocookie.net/__cb20141208212954/finalfantasy/images/5/56/'
             'FFXIV_Feint_Icon.png')
    fester = ('http://img2.wikia.nocookie.net/__cb20141208210814/finalfantasy/images/6/64/'
              'FFXIV_Fester_Icon.png')
    fight_or_flight = ('http://img4.wikia.nocookie.net/__cb20141208214252/finalfantasy/images/'
                       '4/45/FFXIV_Fight_or_Flight_Icon.png')
    fire = ('http://img3.wikia.nocookie.net/__cb20140918072425/finalfantasy/images/7/7f/'
            'FFXIV_Fire_Icon.png')
    fire_2 = ('http://img3.wikia.nocookie.net/__cb20140918071702/finalfantasy/images/e/ed/'
              'FFXIV_FireII_Icon.png')
    fire_3 = ('http://img4.wikia.nocookie.net/__cb20140918071702/finalfantasy/images/4/40/'
              'FFXIV_FireIII_Icon.png')
    fists_of_earth = ('http://img3.wikia.nocookie.net/__cb20141208215352/finalfantasy/images/e/ea/'
                      'FFXIV_Fists_of_Earth_Icon.png')
    fists_of_fire = ('http://img3.wikia.nocookie.net/__cb20141208215625/finalfantasy/images/1/15/'
                     'FFXIV_Fists_of_Fire_Icon.png')
    fists_of_wind = ('http://img2.wikia.nocookie.net/__cb20141208215623/finalfantasy/images/0/00/'
                     'FFXIV_Fists_of_Wind_Icon.png')
    flaming_arrow = ('http://img4.wikia.nocookie.net/__cb20141208212007/finalfantasy/images/2/28/'
                     'FFXIV_Flaming_Arrow_Icon.png')
    flare = ('http://img4.wikia.nocookie.net/__cb20140918071701/finalfantasy/images/4/4b/'
             'FFXIV_Flare_Icon.png')
    flash = ('http://img2.wikia.nocookie.net/__cb20141208214253/finalfantasy/images/c/cf/'
             'FFXIV_Flash_Icon.png')
    fluid_aura = ('http://img3.wikia.nocookie.net/__cb20140920071555/finalfantasy/images/3/35/'
                  'FFXIV_Fluid_Aura_Icon.png')
    foe_requiem = ('http://img1.wikia.nocookie.net/__cb20141208212009/finalfantasy/images/6/6b/'
                   'FFXIV_Foe_Requiem_Icon.png')
    foresight = ('http://img3.wikia.nocookie.net/__cb20141208213543/finalfantasy/images/c/c4/'
                 'FFXIV_Foresight_Icon.png')
    fracture = ('http://img4.wikia.nocookie.net/__cb20141208213544/finalfantasy/images/d/da/'
                'FFXIV_Fracture_Icon.png')
    full_thrust = ('http://img3.wikia.nocookie.net/__cb20141208213308/finalfantasy/images/2/2c/'
                   'FFXIV_Full_Thrust_Icon.png')
    fuma_shuriken = ('http://img2.wikia.nocookie.net/__cb20141208222249/finalfantasy/images/7/7c/'
                     'FFXIV_Fuma_Shuriken_Icon.png')
    goad = ('http://img3.wikia.nocookie.net/__cb20141213124746/finalfantasy/images/8/8a/'
            'FFXIV_Goad_Icon.png')
    gust_slash = ('http://img3.wikia.nocookie.net/__cb20141208222250/finalfantasy/images/5/58/'
                  'FFXIV_Gust_Slash_Icon.png')
    hallowed_ground = ('http://img4.wikia.nocookie.net/__cb20140926191049/finalfantasy/images/'
                       '5/58/FFXIV_Hallowed_Ground_Icon.png')
    hawks_eye = ('http://img1.wikia.nocookie.net/__cb20141208211708/finalfantasy/images/3/34/'
                 'FFXIV_Hawk%27s_Eye_Icon.png')
    haymaker = ('http://img3.wikia.nocookie.net/__cb20141208215351/finalfantasy/images/a/a0/'
                'FFXIV_Haymaker_Icon.png')
    heavy_shot = ('http://img2.wikia.nocookie.net/__cb20141208211337/finalfantasy/images/0/02/'
                  'FFXIV_Heavy_Shot_Icon.png')
    heavy_swing = ('http://img2.wikia.nocookie.net/__cb20141208213542/finalfantasy/images/1/1b/'
                   'FFXIV_Heavy_Swing_Icon.png')
    heavy_thrust = ('http://img1.wikia.nocookie.net/__cb20141208213306/finalfantasy/images/d/da/'
                    'FFXIV_Heavy_Thrust_Icon.png')
    hide = ('http://img3.wikia.nocookie.net/__cb20141208222250/finalfantasy/images/e/ed/'
            'FFXIV_Hide_Icon.png')
    holmgang = ('http://img3.wikia.nocookie.net/__cb20141208213949/finalfantasy/images/5/57/'
                'FFXIV_Holmgang_Icon.png')
    holy = 'http://vignette4.wikia.nocookie.net/finalfantasy/images/f/fc/FFXIV_Holy_Icon.png'
    howling_fist = ('http://img1.wikia.nocookie.net/__cb20141208215624/finalfantasy/images/a/ab/'
                    'FFXIV_Howling_Fist_Icon.png')
    huton = ('http://img4.wikia.nocookie.net/__cb20141208222251/finalfantasy/images/f/f8/'
             'FFXIV_Huton_Icon.png')
    hyoton = ('http://img4.wikia.nocookie.net/__cb20141208222448/finalfantasy/images/0/05/'
              'FFXIV_Hyoton_Icon.png')
    impulse_drive = ('http://img1.wikia.nocookie.net/__cb20141208212955/finalfantasy/images/f/f5/'
                     'FFXIV_Impulse_Drive_Icon.png')
    infuriate = ('http://img1.wikia.nocookie.net/__cb20141208214251/finalfantasy/images/0/06/'
                 'FFXIV_Infuriate_Icon.png')
    inner_beast = ('http://img3.wikia.nocookie.net/__cb20141208213952/finalfantasy/images/e/eb/'
                   'FFXIV_Inner_Beast_Icon.png')
    internal_release = ('http://img1.wikia.nocookie.net/__cb20141208215351/finalfantasy/images/'
                        'a/af/FFXIV_Internal_Release_Icon.png')
    invigorate = ('http://img3.wikia.nocookie.net/__cb20141208213308/finalfantasy/images/3/3b/'
                  'FFXIV_Invigorate_Icon.png')
    jin = ('http://img1.wikia.nocookie.net/__cb20141208222449/finalfantasy/images/4/40/'
           'FFXIV_Jin_Icon.png')
    jugulate = ('http://img2.wikia.nocookie.net/__cb20141208222450/finalfantasy/images/4/42/'
                'FFXIV_Jugulate_Icon.png')
    jump = ('http://img2.wikia.nocookie.net/__cb20141208212950/finalfantasy/images/1/1b/'
            'FFXIV_Jump_Icon.png')
    kassatsu = ('http://img1.wikia.nocookie.net/__cb20141208222450/finalfantasy/images/8/8f/'
                'FFXIV_Kassatsu_Icon.png')
    katon = ('http://img3.wikia.nocookie.net/__cb20141208222450/finalfantasy/images/1/15/'
             'FFXIV_Katon_Icon.png')
    keen_flurry = ('http://img1.wikia.nocookie.net/__cb20141208212954/finalfantasy/images/1/1c/'
                   'FFXIV_Keen_Flurry_Icon.png')
    kiss_of_the_viper = ('http://img4.wikia.nocookie.net/__cb20141208222451/finalfantasy/images/'
                         '7/72/FFXIV_Kiss_of_the_Viper_Icon.png')
    kiss_of_the_wasp = ('http://img2.wikia.nocookie.net/__cb20141208222451/finalfantasy/images/'
                        '6/68/FFXIV_Kiss_of_the_Wasp_Icon.png')
    leeches = ('http://img2.wikia.nocookie.net/__cb20141208211336/finalfantasy/images/4/42/'
               'FFXIV_Leeches_Icon.png')
    leg_sweep = ('http://img3.wikia.nocookie.net/__cb20141208213305/finalfantasy/images/8/80/'
                 'FFXIV_Leg_Sweep_Icon.png')
    lethargy = ('http://img2.wikia.nocookie.net/__cb20141208212454/finalfantasy/images/b/b5/'
                'FFXIV_Lethargy_Icon.png')
    life_surge = ('http://img1.wikia.nocookie.net/__cb20141208213307/finalfantasy/images/a/a2/'
                  'FFXIV_Life_Surge_Icon.png')
    limit_break = ('http://img2.wikia.nocookie.net/__cb20141219010443/finalfantasy/images/0/02/'
                   'FFXIV_Limit_Break_Icon.png')
    lustrate = ('http://img3.wikia.nocookie.net/__cb20141208211337/finalfantasy/images/a/a0/'
                'FFXIV_Lustrate_Icon.png')
    mages_ballad = ('http://img3.wikia.nocookie.net/__cb20141208212009/finalfantasy/images/7/7c/'
                    'FFXIV_Mage%27s_Ballad_Icon.png')
    maim = ('http://img1.wikia.nocookie.net/__cb20141208213545/finalfantasy/images/c/c5/'
            'FFXIV_Maim_Icon.png')
    mana_wall = ('http://img2.wikia.nocookie.net/__cb20141208212451/finalfantasy/images/c/c0/'
                 'FFXIV_Manawall_Icon.png')
    mana_ward = ('http://img4.wikia.nocookie.net/__cb20141208212453/finalfantasy/images/f/f1/'
                 'FFXIV_Manaward_Icon.png')
    mantra = ('http://img1.wikia.nocookie.net/__cb20141208215624/finalfantasy/images/1/1a/'
              'FFXIV_Mantra_Icon.png')
    medica = ('http://img2.wikia.nocookie.net/__cb20140918065859/finalfantasy/images/a/aa/'
              'Medica_Icon.png')
    medica_2 = ('http://img4.wikia.nocookie.net/__cb20140918070722/finalfantasy/images/1/19/'
                'Medica_II_Icon.png')
    mercy_stroke = ('http://img1.wikia.nocookie.net/__cb20141208213948/finalfantasy/images/5/58/'
                    'FFXIV_Mercy_Stroke_Icon.png')
    miasma = ('http://img4.wikia.nocookie.net/__cb20140918072432/finalfantasy/images/7/7a/'
              'Miasma.png')
    miasma_2 = ('http://img2.wikia.nocookie.net/__cb20140919132749/finalfantasy/images/c/c0/'
                'FFXIVARR_Miasma_II_Icon.png')
    miserys_end = ('http://img1.wikia.nocookie.net/__cb20141208211706/finalfantasy/images/d/d3/'
                   'FFXIV_Misery%27s_End_Icon.png')
    mug = ('http://img1.wikia.nocookie.net/__cb20141208222452/finalfantasy/images/9/9f/'
           'FFXIV_Mug_Icon.png')
    mutilate = ('http://img1.wikia.nocookie.net/__cb20141208222452/finalfantasy/images/b/b3/'
                'FFXIV_Mutilate_Icon.png')
    ninjutsu = ('http://img4.wikia.nocookie.net/__cb20141208222453/finalfantasy/images/4/49/'
                'FFXIV_Ninjutsu_Icon.png')
    one_arm_punch = ('http://img1.wikia.nocookie.net/__cb20141005214708/finalfantasy/images/d/dd/'
                     'FFXIV_One_Ilm_Punch_Icon.png')
    overpower = ('http://img2.wikia.nocookie.net/__cb20141208213545/finalfantasy/images/5/5d/'
                 'FFXIV_Overpower_Icon.png')
    perfect_balance = ('http://img2.wikia.nocookie.net/__cb20141208215625/finalfantasy/images/'
                       'c/c2/FFXIV_Perfect_Balance_Icon.png')
    perfect_dodge = ('http://img2.wikia.nocookie.net/__cb20141208222620/finalfantasy/images/d/dd/'
                     'FFXIV_Perfect_Dodge_Icon.png')
    phlebotomize = ('http://img3.wikia.nocookie.net/__cb20141208213309/finalfantasy/images/3/31/'
                    'FFXIV_Phlebotomize_Icon.png')
    physick = ('http://img2.wikia.nocookie.net/__cb20141208210815/finalfantasy/images/b/ba/'
               'FFXIV_Physick_Icon.png')
    piercing_talon = ('http://img2.wikia.nocookie.net/__cb20141208213307/finalfantasy/images/f/f7/'
                      'FFXIV_Piercing_Talon_Icon.png')
    power_surge = ('http://img2.wikia.nocookie.net/__cb20141208212952/finalfantasy/images/d/dd/'
                   'FFXIV_Power_Surge_Icon.png')
    presence_of_mind = ('http://img2.wikia.nocookie.net/__cb20141208212454/finalfantasy/images/'
                        '6/65/FFXIV_Presence_of_Mind_Icon.png')
    protect = ('http://img3.wikia.nocookie.net/__cb20140920071554/finalfantasy/images/9/92/'
               'FFXIVARR_Protect_Icon.png')
    provoke = ('http://img3.wikia.nocookie.net/__cb20141208214708/finalfantasy/images/d/d2/'
               'FFXIV_Provoke_Icon.png')
    quelling_strikes = ('http://img1.wikia.nocookie.net/__cb20141208211709/finalfantasy/images/'
                        '4/46/FFXIV_Quelling_Strikes_Icon.png')
    quick_nock = ('http://img1.wikia.nocookie.net/__cb20141208211708/finalfantasy/images/3/3e/'
                  'FFXIV_Quick_Nock_Icon.png')
    rabbit_medium = ('http://img2.wikia.nocookie.net/__cb20141208222621/finalfantasy/images/7/7d/'
                     'FFXIV_Rabbit_Medium_Icon.png')
    rage_of_halone = ('http://img1.wikia.nocookie.net/__cb20141208214708/finalfantasy/images/5/5d/'
                      'FFXIV_Rage_of_Halone_Icon.png')
    raging_strikes = ('http://img3.wikia.nocookie.net/__cb20141208211338/finalfantasy/images/5/51/'
                      'FFXIV_Raging_Strikes_Icon.png')
    rain_of_death = ('http://img2.wikia.nocookie.net/__cb20141208212010/finalfantasy/images/1/1a/'
                     'FFXIV_Rain_of_Death_Icon.png')
    raise_ability = ('http://img2.wikia.nocookie.net/__cb20140920071555/finalfantasy/images/7/7d/'
                     'FFXIVARR_Raise_Icon.png')
    raiton = ('http://img1.wikia.nocookie.net/__cb20141208222621/finalfantasy/images/0/08/'
              'FFXIV_Raiton_Icon.png')
    rampart = ('http://img3.wikia.nocookie.net/__cb20141208214252/finalfantasy/images/2/29/'
               'FFXIV_Rampart_Icon.png')
    regen = ('http://img4.wikia.nocookie.net/__cb20141208212455/finalfantasy/images/0/05/'
             'FFXIV_Regen_Icon.png')
    repelling_shot = ('http://img4.wikia.nocookie.net/__cb20141208211707/finalfantasy/images/3/3b/'
                      'FFXIV_Repelling_Shot_Icon.png')
    repose = ('http://img3.wikia.nocookie.net/__cb20140920071556/finalfantasy/images/b/bc/'
              'FFXIV_Repose_Icon.png')
    resurrection = ('http://img4.wikia.nocookie.net/__cb20141009232507/finalfantasy/images/3/31/'
                    'FFXIV_Resurrection_Icon.png')
    return_ability = ('http://img3.wikia.nocookie.net/__cb20141001015216/finalfantasy/images/4/4c/'
                      'FFXIV_Return_Icon.png')
    ring_of_thorns = ('http://img4.wikia.nocookie.net/__cb20141208213542/finalfantasy/images/7/7b/'
                      'FFXIV_Ring_of_Thorns_Icon.png')
    riot_blade = ('http://img3.wikia.nocookie.net/__cb20140918073139/finalfantasy/images/2/25/'
                  'FFXIVARR_Riot_Blade_Icon.png')
    rock_breaker = ('http://img4.wikia.nocookie.net/__cb20141001010950/finalfantasy/images/a/a0/'
                    'FFXIV_Rockbreaker_Icon.png')
    rouse = ('http://img2.wikia.nocookie.net/__cb20141208211335/finalfantasy/images/c/c1/'
             'FFXIV_Rouse_Icon.png')
    ruin = ('http://img1.wikia.nocookie.net/__cb20140918072426/finalfantasy/images/d/da/'
            'FFXIVARR_Ruin_Icon.png')
    ruin_2 = ('http://img4.wikia.nocookie.net/__cb20140918074535/finalfantasy/images/d/d4/'
              'FFXIVARR_Ruin_II_Icon.png')
    sacred_soil = ('http://img2.wikia.nocookie.net/__cb20141208211336/finalfantasy/images/6/64/'
                   'FFXIV_Sacred_Soil_Icon.png')
    savage_blade = ('http://img2.wikia.nocookie.net/__cb20141208214252/finalfantasy/images/b/b7/'
                    'FFXIV_Savage_Blade_Icon.png')
    scathe = ('http://img3.wikia.nocookie.net/__cb20140918071703/finalfantasy/images/a/ac/'
              'FFXIVARR_Scathe_Icon.png')
    second_wind = ('http://img4.wikia.nocookie.net/__cb20141208215350/finalfantasy/images/1/13/'
                   'FFXIV_Second_Wind_Icon.png')
    sentinel = ('http://img4.wikia.nocookie.net/__cb20141208214711/finalfantasy/images/0/0f/'
                'FFXIV_Sentinel_Icon.png')
    shadow_fang = ('http://img2.wikia.nocookie.net/__cb20141208222622/finalfantasy/images/0/06/'
                   'FFXIV_Shadow_Fang_Icon.png')
    shadow_flare = ('http://img1.wikia.nocookie.net/__cb20140918072432/finalfantasy/images/9/9b/'
                    'FFXIVARR_Shadow_Flare_Icon.png')
    shadow_bind = ('http://img3.wikia.nocookie.net/__cb20141208211706/finalfantasy/images/6/6f/'
                   'FFXIV_Shadowbind_Icon.png')
    shield_bash = ('http://img1.wikia.nocookie.net/__cb20141208214707/finalfantasy/images/4/45/'
                   'FFXIV_Shield_Bash_Icon.png')
    shield_lob = ('http://img3.wikia.nocookie.net/__cb20141208214254/finalfantasy/images/a/a4/'
                  'FFXIV_Shield_Lob_Icon.png')
    shield_oath = ('http://img2.wikia.nocookie.net/__cb20141208214837/finalfantasy/images/6/66/'
                   'FFXIV_Shield_Oath_Icon.png')
    shield_swipe = ('http://img1.wikia.nocookie.net/__cb20141208214709/finalfantasy/images/7/71/'
                    'FFXIV_Shield_Swipe_Icon.png')
    shoulder_tackle = ('http://img2.wikia.nocookie.net/__cb20141011031940/finalfantasy/images/'
                       'd/d9/FFXIV_Shoulder_Tackle_Icon.png')
    shroud_of_saints = ('http://img2.wikia.nocookie.net/__cb20140920071556/finalfantasy/images/'
                        '0/0a/FFXIV_Shroud_of_Saints_Icon.png')
    shukuchi = ('http://img2.wikia.nocookie.net/__cb20141208222622/finalfantasy/images/c/cc/'
                'FFXIV_Shukuchi_Icon.png')
    skull_sunder = ('http://img2.wikia.nocookie.net/__cb20141208213543/finalfantasy/images/b/bf/'
                    'FFXIV_Skull_Sunder_Icon.png')
    sleep = ('http://img3.wikia.nocookie.net/__cb20140918071703/finalfantasy/images/e/e2/'
             'FFXIARR_Sleep_Icon.png')
    snap_punch = ('http://img4.wikia.nocookie.net/__cb20141208215350/finalfantasy/images/6/66/'
                  'FFXIV_Snap_Punch_Icon.png')
    sneak_attack = ('http://img3.wikia.nocookie.net/__cb20141208222623/finalfantasy/images/d/d4/'
                    'FFXIV_Sneak_Attack_Icon.png')
    spine_shatter_dive = ('http://img2.wikia.nocookie.net/__cb20141208212953/finalfantasy/images/'
                          'd/d3/FFXIV_Spineshatter_Dive_Icon.png')
    spinning_edge = ('http://img4.wikia.nocookie.net/__cb20141208222623/finalfantasy/images/5/5f/'
                     'FFXIV_Spinning_Edge_Icon.png')
    spirits_within = ('http://img3.wikia.nocookie.net/__cb20141208214837/finalfantasy/images/3/35/'
                      'FFXIV_Spirits_Within_Icon.png')
    spur = ('http://img4.wikia.nocookie.net/__cb20141208210815/finalfantasy/images/c/c7/'
            'FFXIV_Spur_Icon.png')
    steel_cyclone = ('http://img4.wikia.nocookie.net/__cb20141208214250/finalfantasy/images/2/29/'
                     'FFXIV_Steel_Cyclone_Icon.png')
    steel_peak = ('http://img2.wikia.nocookie.net/__cb20141208215623/finalfantasy/images/2/27/'
                  'FFXIV_Steel_Peak_Icon.png')
    stone = ('http://img2.wikia.nocookie.net/__cb20140918075748/finalfantasy/images/c/c0/'
             'FFXIV_Stone_Icon.png')
    stone_2 = ('http://img2.wikia.nocookie.net/__cb20140918072425/finalfantasy/images/e/e5/'
               'Stone_II_Icon.png')
    stone_skin = ('http://img2.wikia.nocookie.net/__cb20140918070721/finalfantasy/images/2/21/'
                  'FFXIVARR_Stoneskin_Icon.png')
    stone_skin_2 = ('http://img1.wikia.nocookie.net/__cb20141209203022/finalfantasy/images/3/36/'
                    'FFXIV_Stoneskin_II_Icon.png')
    storms_eye = ('http://img4.wikia.nocookie.net/__cb20141208213951/finalfantasy/images/0/0d/'
                  'FFXIV_Storm%27s_Eye_Icon.png')
    storms_path = ('http://img2.wikia.nocookie.net/__cb20141208213949/finalfantasy/images/6/6b/'
                   'FFXIV_Storm%27s_Path_Icon.png')
    straight_shot = ('http://img2.wikia.nocookie.net/__cb20141208211338/finalfantasy/images/8/85/'
                     'FFXIV_Straight_Shot_Icon.png')
    succor = ('http://img2.wikia.nocookie.net/__cb20141208211335/finalfantasy/images/c/cb/'
              'FFXIV_Succor_Icon.png')
    suiton = ('http://img4.wikia.nocookie.net/__cb20141208222623/finalfantasy/images/8/8a/'
              'FFXIV_Suiton_Icon.png')
    summon = ('http://img3.wikia.nocookie.net/__cb20141208210816/finalfantasy/images/f/f5/'
              'FFXIV_Summon_Icon.png')
    summon_2 = ('http://img2.wikia.nocookie.net/__cb20141208210818/finalfantasy/images/4/47/'
                'FFXIV_Summon_II_Icon.png')
    summon_3 = ('http://img3.wikia.nocookie.net/__cb20141208210813/finalfantasy/images/f/ff/'
                'FFXIV_Summon_III_Icon.png')
    sure_cast = ('http://img3.wikia.nocookie.net/__cb20141208212453/finalfantasy/images/a/af/'
                 'FFXIV_Surecast_Icon.png')
    sustain = ('http://img1.wikia.nocookie.net/__cb20141208211333/finalfantasy/images/d/d5/'
               'FFXIV_Sustain_Icon.png')
    swift_cast = ('http://img2.wikia.nocookie.net/__cb20140918072425/finalfantasy/images/d/d5/'
                  'FFXIV_Swiftcast_Icon.png')
    swift_song = ('http://img1.wikia.nocookie.net/__cb20141208211708/finalfantasy/images/e/e0/'
                  'FFXIV_Swiftsong_Icon.png')
    sword_oath = ('http://img4.wikia.nocookie.net/__cb20141208214713/finalfantasy/images/0/04/'
                  'FFXIV_Sword_Oath_Icon.png')
    teleport = ('http://img4.wikia.nocookie.net/__cb20141001015217/finalfantasy/images/c/cb/'
                'FFXIV_Teleport_Icon.png')
    tempered_will = ('http://img4.wikia.nocookie.net/__cb20141208214711/finalfantasy/images/f/fc/'
                     'FFXIV_Tempered_Will_Icon.png')
    ten = ('http://img4.wikia.nocookie.net/__cb20141208222624/finalfantasy/images/d/d5/'
           'FFXIV_Ten_Icon.png')
    thrill_of_battle = ('http://img3.wikia.nocookie.net/__cb20141208213949/finalfantasy/images/'
                        '7/71/FFXIV_Thrill_of_Battle_Icon.png')
    throwing_dagger = ('http://img2.wikia.nocookie.net/__cb20141208222625/finalfantasy/images/'
                       'b/bb/FFXIV_Throwing_Dagger_Icon.png')
    thunder = ('http://img3.wikia.nocookie.net/__cb20140918072425/finalfantasy/images/d/de/'
               'FFXIV_Thunder_Icon.png')
    thunder_2 = ('http://img1.wikia.nocookie.net/__cb20140918071703/finalfantasy/images/5/58/'
                 'FFXIV_Thunder_II_Icon.png')
    thunder_3 = ('http://img2.wikia.nocookie.net/__cb20140918071702/finalfantasy/images/0/03/'
                 'FFXIVARR_Thunder_III_Icon.png')
    tomahawk = ('http://img2.wikia.nocookie.net/__cb20140918073139/finalfantasy/images/e/ee/'
                'FFXIVARR_Tomahawk_Icon.png')
    touch_of_death = ('http://img2.wikia.nocookie.net/__cb20141208215352/finalfantasy/images/b/b5/'
                      'FFXIV_Touch_of_Death_Icon.png')
    transpose = ('http://img4.wikia.nocookie.net/__cb20141208212452/finalfantasy/images/c/c5/'
                 'FFXIV_Transpose_Icon.png')
    tri_disaster = ('http://img4.wikia.nocookie.net/__cb20140918072432/finalfantasy/images/0/01/'
                    'FFXIVARR_Tri-disaster_Icon.png')
    trick_attack = ('http://img1.wikia.nocookie.net/__cb20141208222728/finalfantasy/images/c/c2/'
                    'FFXIV_Trick_Attack_Icon.png')
    true_strike = ('http://img2.wikia.nocookie.net/__cb20141208215348/finalfantasy/images/0/0c/'
                   'FFXIV_True_Strike_Icon.png')
    true_thrust = ('http://img1.wikia.nocookie.net/__cb20141208212953/finalfantasy/images/e/e4/'
                   'FFXIV_True_Thrust_Icon.png')
    twin_snakes = ('http://img2.wikia.nocookie.net/__cb20141208215352/finalfantasy/images/a/a0/'
                   'FFXIV_Twin_Snakes_Icon.png')
    unchained = ('http://img3.wikia.nocookie.net/__cb20141208214358/finalfantasy/images/d/d4/'
                 'FFXIV_Unchained_Icon.png')
    vengeance = ('http://img2.wikia.nocookie.net/__cb20141208213950/finalfantasy/images/d/dd/'
                 'FFXIV_Vengeance_Icon.png')
    venomous_bite = ('http://img2.wikia.nocookie.net/__cb20141208211705/finalfantasy/images/5/5b/'
                     'FFXIV_Venomous_Bite_Icon.png')
    virus = ('http://img1.wikia.nocookie.net/__cb20141208210817/finalfantasy/images/8/8e/'
             'FFXIV_Virus_Icon.png')
    vorpal_thrust = ('http://img4.wikia.nocookie.net/__cb20141208212954/finalfantasy/images/1/13/'
                     'FFXIV_Vorpal_Thrust_Icon.png')
    wide_volley = ('http://img1.wikia.nocookie.net/__cb20141208212007/finalfantasy/images/a/af/'
                   'FFXIV_Wide_Volley_Icon.png')
    wind_bite = ('http://img3.wikia.nocookie.net/__cb20141208211709/finalfantasy/images/0/0d/'
                 'FFXIV_Windbite_Icon.png')


class DurationUnit(enum.Enum):
    instant = object()
    rnd = object()
    min = object()
    hour = object()
    day = object()
    forever = object()


class Time(enum.Enum):
    free_a = object()
    ab_a = object()
    std_a = object()
    full_a = object()
    std_ab_a = object()


class Ability(macro.Macroable):
    mp_mac_modifier = 0.25

    def __init__(self, name: str, picture: AbilityPicture, mp_cost: int, target_area: str,
                 duration: str = None, duration_unit: DurationUnit = DurationUnit.instant,
                 prerequisites: Tuple['Ability', ...]=(), damage_type: DamageType = None,
                 effect='',
                 attacks: int = 0, pdam: str = None, mdam: str = None,
                 targets_mdef: bool = False, time: Time = Time.ab_a, min_range: str = '0',
                 max_range: str = '0', shape: Shape = Shape.point) -> None:
        self.name = name
        self.picture = picture
        self.damage_type = damage_type
        self.mp_cost = mp_cost
        self.prerequisites = prerequisites
        self.target_area = target_area
        self.duration = duration
        self.duration_unit = duration_unit
        self.effect = effect
        self.attacks = attacks
        # TODO: Validate pdam/mdam formulas?
        self.pdam = pdam
        self.mdam = mdam
        self.targets_mdef = targets_mdef
        self.time = time
        self.min_range = min_range
        self.max_range = max_range
        self.shape = shape

    def mac(self) -> int:
        return round(self.mp_cost * self.mp_mac_modifier)

    @property
    def macro(self) -> str:
        common_template = ('{template_tag}'
                           '{color}'
                           '{{{{title=**{ability_name}** [p]({picture})}}}}'
                           '{{{{subheader=Ability}}}}'
                           '{{{{subheaderright={time}}}}}'
                           '{{{{subheader2={mp_cost}MP}}}}'
                           '{attacks}'
                           '{{{{emote=@{{Name}} casts{target_name}}}}}'
                           '{{{{Range=[[{min_range}]]-[[{max_range}]]}}}}'
                           '{{{{Shape=[p]({shape_picture}) ({shape})}}}}'
                           '{{{{Area={area}}}}}'
                           '{{{{Duration={duration}}}}}'
                           '{{{{Effect=*{effect}*}}}}'
                           '{template_terminator}')

        if self.attacks > 1:
            attacks = ('{{{{Attacks=[[?{{Attacks (max={attacks})|'
                       '{attacks}}}]]/{attacks}}}}}').format(attacks=self.attacks)
        else:
            attacks = ''

        if self.targets_mdef:
            target_name = ' at @{target|Name}'
        else:
            target_name = ''

        if (self.duration_unit is DurationUnit.instant or
                self.duration_unit is DurationUnit.forever):
            duration_str = self.duration_unit.name
        else:
            duration_str = '[[{duration_value}]]{duration_unit}'.format(
                duration_value=self.duration, duration_unit=self.duration_unit.name.upper())

            if self.duration_unit is DurationUnit.rnd:
                duration_str += '(ends [[{duration_rnd}+@{{tracker|RND}}]])'.format(
                    duration_rnd=self.duration)

        macro_str = common_template.format(template_tag=macro.template_tag,
                                           color=macro.MacroColorTag.purple.value,
                                           ability_name=self.name,
                                           picture=self.picture.value,
                                           time=self.time.name,
                                           attacks=attacks,
                                           mp_cost=self.mp_cost,
                                           target_name=target_name,
                                           min_range=self.min_range,
                                           max_range=self.max_range,
                                           template_terminator=macro.template_terminator,
                                           shape_picture=self.shape.value,
                                           shape=self.shape.name,
                                           area=self.target_area,
                                           duration=duration_str,
                                           effect=self.effect)
        for i in range(self.attacks):
            attack_template = ('{template_tag}'
                               '{{{{title=Attack}}}}'
                               '{color}'
                               '{hit}'
                               '{pdam}'
                               '{mdam}'
                               '{template_terminator}')

            hit = ''
            if self.targets_mdef:
                hit = ('{{{{Hit=[[{{d20+@{{BMAC}}+{mp_mac_modifier}*{mp_cost}}}>'
                       '@{{target|MDEF}}]] vs MDEF}}}}'.format(
                            mp_mac_modifier=self.mp_mac_modifier,
                            mp_cost=self.mp_cost))

            damage_template = ('{{{{{damage_category}='
                               '[[round({dam}-@{{target|{reduction_type}}})'
                               '*(1+@{{target|{damage_type}VUL}})'
                               '/(1+@{{target|{damage_type}RES}})'
                               '*(1-@{{target|{damage_type}IMU}})'
                               ']]{damage_category} [{damage_type}]}}}}'
                               '{{{{{damage_type}='
                               'VUL:@{{target|{damage_type}VUL}} '
                               'RES:@{{target|{damage_type}RES}} '
                               'IMU:@{{target|{damage_type}IMU}}'
                               '}}}}')

            pdam = ''
            if self.pdam is not None:
                pdam = damage_template.format(damage_category='PDAM',
                                              dam=self.pdam,
                                              reduction_type='PRED',
                                              damage_type=self.damage_type.cap_name)

            mdam = ''
            if self.mdam is not None:
                mdam = damage_template.format(damage_category='MDAM',
                                              dam=self.mdam,
                                              reduction_type='MRED',
                                              damage_type=self.damage_type.cap_name)

            macro_str += '\n' + attack_template.format(
                template_tag=macro.template_tag,
                color=macro.MacroColorTag.purple.value,
                template_terminator=macro.template_terminator,
                hit=hit,
                pdam=pdam,
                mdam=mdam)

        return macro.escape_attributes(macro_str)
