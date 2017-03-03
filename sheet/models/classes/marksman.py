from ..ability import Ability, AbilityPicture, DurationUnit, Time
from ..class_type import Class
from ..equipment import DamageType, Shape


snipe_1 = Ability(
    name='Snipe I', picture=AbilityPicture.hide,
    mp_cost=1, target_area='One enemy', time=Time.std_a,
    duration_unit=DurationUnit.instant,
    effect='Rifle: +2Max Range',
)

snipe_2 = Ability(
    name='Snipe II', picture=AbilityPicture.hide,
    mp_cost=1, target_area='One enemy', time=Time.std_a,
    duration_unit=DurationUnit.instant,
    effect='Rifle: +2Max Range, +1PDAM',
)

snipe_3 = Ability(
    name='Snipe III', picture=AbilityPicture.hide,
    mp_cost=1, target_area='One enemy', time=Time.std_a,
    duration_unit=DurationUnit.instant,
    effect='Rifle: +[[2+WIS]]Max Range, +2PDAM',
)

quick_draw_1 = Ability(
    name='Quick Draw I', picture=AbilityPicture.dancing_edge,
    mp_cost=0, target_area='Self', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: On failed REG check can take normal pistol attack for -4PAC',
)

quick_draw_2 = Ability(
    name='Quick Draw II', picture=AbilityPicture.dancing_edge,
    mp_cost=0, target_area='Self', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: On failed REG check can take normal pistol attack for -2PAC',
)

quick_draw_3 = Ability(
    name='Quick Draw III', picture=AbilityPicture.dancing_edge,
    mp_cost=0, target_area='Self', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: On failed REG check can take normal pistol',
)

mortar_1 = Ability(
    name='Mortar I', picture=AbilityPicture.doton,
    mp_cost=3, attacks=1, mdam='1d10+WIS', damage_type=DamageType.fire,
    targets_mdef=True, max_range='24+4*WIS', time=Time.full_a,
    shape=Shape.circle, target_area='2RAD',
    duration_unit=DurationUnit.instant,
    effect='Setup: 2FullA. Mount/Dismount: 1FullA.  Incendiary Rounds',
)

mortar_2 = Ability(
    name='Mortar II', picture=AbilityPicture.doton,
    mp_cost=0, max_range='24+4*WIS', time=Time.full_a,
    duration_unit=DurationUnit.instant, target_area='Smoke Bomb Ability',
    effect='Allows Smoke Bomb ability use Mortar Range.',
)

mortar_3 = Ability(
    name='Mortar II', picture=AbilityPicture.doton,
    mp_cost=3, attacks=1, mdam='1d20+WIS', damage_type=DamageType.piercing,
    targets_mdef=True, max_range='24+4*WIS', time=Time.full_a,
    shape=Shape.circle, target_area='One enemy',
    duration_unit=DurationUnit.instant,
    effect='Armor Piercing: +4MAC; ignore PRED',
)

smoke_bomb_1 = Ability(
    name='Smoke Bomb I', picture=AbilityPicture.blood_for_blood,
    mp_cost=2, attacks=1, targets_mdef=True,
    shape=Shape.circle, target_area='Up to 2RAD', max_range='6',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Smoke bomb obscures vision',
)

smoke_bomb_2 = Ability(
    name='Smoke Bomb II', picture=AbilityPicture.blood_for_blood,
    mp_cost=2, attacks=1, targets_mdef=True,
    shape=Shape.circle, target_area='Up to [[2+WIS]]RAD', max_range='6',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Smoke causes -4PAC to enemies',
)

smoke_bomb_3 = Ability(
    name='Smoke Bomb III', picture=AbilityPicture.blood_for_blood,
    mp_cost=6, attacks=1, targets_mdef=True,
    shape=Shape.circle, target_area='Up to [[2+WIS]]RAD', max_range='6',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Smoke staggers enemies',
)

combat_enhancements_1 = Ability(
    name='Combat Enhancements I', picture=AbilityPicture.limit_break,
    mp_cost=1,
    shape=Shape.circle, target_area='Allies in [[1+WIS]]RAD',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Passive: Studies 1 enemy type within sight and adds +1PDAM to '
           'allies’ equipment vs that enemy.',
)

combat_enhancements_2 = Ability(
    name='Combat Enhancements II', picture=AbilityPicture.limit_break,
    mp_cost=1,
    shape=Shape.circle, target_area='Allies in [[1+WIS]]RAD',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Passive: Studies 1 enemy type within sight and adds +1PRED to '
           'allies’ equipment vs that enemy.',
)

combat_enhancements_3 = Ability(
    name='Combat Enhancements III', picture=AbilityPicture.limit_break,
    mp_cost=2,
    shape=Shape.circle, target_area='Allies in [[1+WIS]]RAD',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Passive: Studies 1 enemy type within sight and adds +1PDAM, +1PRED to '
           'allies’ equipment vs that enemy.',
)

# Tier 2.

stealth_snipe_1 = Ability(
    name='Stealth Snipe I', picture=AbilityPicture.trick_attack,
    mp_cost=3, target_area='One enemy', time=Time.std_a, min_range='4',
    duration_unit=DurationUnit.instant,
    effect='Rifle: Silenced round; requires 15PER to hear and immobilizes. +2Max Range',
    prerequisites=(snipe_3, combat_enhancements_2,),
)

stealth_snipe_2 = Ability(
    name='Stealth Snipe II', picture=AbilityPicture.trick_attack,
    mp_cost=5, target_area='One enemy', time=Time.std_a, min_range='4',
    duration_unit=DurationUnit.instant,
    effect='Rifle: Silenced round; Requires 20PER to hear and staggers. +2Max Range',
    prerequisites=(stealth_snipe_1,),
)

stealth_snipe_3 = Ability(
    name='Stealth Snipe III', picture=AbilityPicture.trick_attack,
    mp_cost=7, target_area='One enemy', time=Time.std_a, min_range='4',
    duration_unit=DurationUnit.instant,
    effect='Rifle: Silenced round; Requires [[20+WIS]]PER to hear and disables. +2Max Range',
    prerequisites=(stealth_snipe_2,),
)

dual_wield_1 = Ability(
    name='Dual Wield I', picture=AbilityPicture.phlebotomize,
    mp_cost=0, target_area='Self', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: Can equip a one handed firearm in each hand at -6PAC',
    prerequisites=(quick_draw_3, snipe_2,),
)

dual_wield_2 = Ability(
    name='Dual Wield II', picture=AbilityPicture.phlebotomize,
    mp_cost=0, target_area='Self', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: Can equip a one handed firearm in each hand at -4PAC',
    prerequisites=(dual_wield_1,),
)

dual_wield_3 = Ability(
    name='Dual Wield III', picture=AbilityPicture.phlebotomize,
    mp_cost=0, target_area='Self', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: Can equip a one handed firearm in each hand at -2PAC',
    prerequisites=(dual_wield_2,),
)

siege_tech_mark_two_1 = Ability(
    name='Siege Tech Mark Two I', picture=AbilityPicture.doton,
    mp_cost=5, attacks=1, mdam='2d10+WIS', damage_type=DamageType.fire,
    targets_mdef=True, max_range='24+4*WIS', time=Time.full_a,
    shape=Shape.circle, target_area='2RAD',
    duration_unit=DurationUnit.instant,
    effect='Setup: 2FullA. Mount/Dismount: 1FullA.  Incendiary Rounds',
    prerequisites=(mortar_3, smoke_bomb_2,),
)

siege_tech_mark_two_2 = Ability(
    name='Siege Tech Mark Two II', picture=AbilityPicture.doton,
    mp_cost=0, max_range='24+4*WIS', time=Time.full_a,
    duration_unit=DurationUnit.instant, target_area='Slime Bomb Ability',
    effect='Allows Slime Bomb ability use Mortar Range.',
    prerequisites=(siege_tech_mark_two_1,),
)

siege_tech_mark_two_3 = Ability(
    name='Siege Tech Mark Two II', picture=AbilityPicture.doton,
    mp_cost=4, attacks=1, mdam='2d20+WIS', damage_type=DamageType.piercing,
    targets_mdef=True, max_range='24+4*WIS', time=Time.full_a,
    shape=Shape.circle, target_area='One enemy',
    duration_unit=DurationUnit.instant,
    effect='Armor Piercing: +4MAC; ignore PRED',
    prerequisites=(siege_tech_mark_two_2,),
)

slime_bomb_1 = Ability(
    name='Slime Bomb I', picture=AbilityPicture.virus,
    mp_cost=3, attacks=1, targets_mdef=True,
    shape=Shape.circle, target_area='Up to 1RAD', max_range='6',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Effected area becomes slippery; Failing MDEF causes falling. '
           'Creatures that fall are immobilized.',
    prerequisites=(smoke_bomb_3, quick_draw_2,),
)

slime_bomb_2 = Ability(
    name='Slime Bomb II', picture=AbilityPicture.virus,
    mp_cost=4, attacks=1, targets_mdef=True,
    shape=Shape.circle, target_area='Up to 1RAD', max_range='6',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Effected area becomes slippery; Failing MDEF causes falling. '
           'Creatures that fall are immobilized. Creatures moving in the area move at ½SPEED.',
    prerequisites=(slime_bomb_1,),
)

slime_bomb_3 = Ability(
    name='Slime Bomb III', picture=AbilityPicture.virus,
    mp_cost=4, attacks=1, targets_mdef=True,
    shape=Shape.circle, target_area='Up to 1RAD', max_range='6',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Effected area becomes slippery; Failing MDEF causes falling. '
           'Creatures that fall are stunned. Creatures moving in the area move at ½SPEED.',
    prerequisites=(slime_bomb_2,),
)

gatling_1 = Ability(
    name='Gatling I', picture=AbilityPicture.steel_peak,
    mp_cost=3, attacks=3, mdam='3', damage_type=DamageType.piercing,
    targets_mdef=True, max_range='9+WIS', time=Time.std_a,
    shape=Shape.multi_point, target_area='Enemies',
    duration_unit=DurationUnit.instant,
    effect='Reaper: Draw/Stow reaper: FullA.  When drawn, Dwarf moves at -3SPEED. '
           'Standard Rounds',
    prerequisites=(snipe_2, combat_enhancements_2, mortar_2,),
)

gatling_2 = Ability(
    name='Gatling II', picture=AbilityPicture.steel_peak,
    mp_cost=3, attacks=3, mdam='2', damage_type=DamageType.piercing,
    targets_mdef=True, max_range='9+WIS', time=Time.std_a,
    shape=Shape.multi_point, target_area='Enemies',
    duration_unit=DurationUnit.instant,
    effect='Reaper: Wall rounds: -3SPEED on hit',
    prerequisites=(gatling_1,),
)

gatling_3 = Ability(
    name='Gatling III', picture=AbilityPicture.steel_peak,
    mp_cost=5, attacks=3, mdam='3+WIS', damage_type=DamageType.piercing,
    targets_mdef=True, max_range='9+WIS', time=Time.std_a,
    shape=Shape.multi_point, target_area='Enemies',
    duration_unit=DurationUnit.instant,
    effect='Reaper: Punisher rounds',
    prerequisites=(gatling_2,),
)

# Tier 3.

full_luna_jacket_1 = Ability(
    name='Full Luna Jacket I', picture=AbilityPicture.disembowel,
    mp_cost=4, time=Time.std_a,
    shape=Shape.line, target_area='Rifle Range DIS line',
    duration_unit=DurationUnit.instant,
    effect='Rifle: Rounds pierce through Medium size creatures and 1DIS thick objects',
    prerequisites=(dual_wield_2, siege_tech_mark_two_2,),
)

full_luna_jacket_2 = Ability(
    name='Full Luna Jacket II', picture=AbilityPicture.disembowel,
    mp_cost=5, time=Time.std_a,
    shape=Shape.line, target_area='Rifle Range DIS line',
    duration_unit=DurationUnit.instant,
    effect='Rifle: Rounds pierce through Medium size creatures and 1DIS thick objects. '
           '+[[2*WIS]]PAC',
    prerequisites=(full_luna_jacket_1,),
)

full_luna_jacket_3 = Ability(
    name='Full Luna Jacket III', picture=AbilityPicture.disembowel,
    mp_cost=6, time=Time.std_a,
    shape=Shape.line, target_area='Rifle Range DIS line',
    duration_unit=DurationUnit.instant,
    effect='Rifle: Rounds pierce through Medium size creatures and 1DIS thick objects. '
           '+[[2*WIS]]PAC. Ignore PRED.',
    prerequisites=(full_luna_jacket_2,),
)

gds_armor_1 = Ability(
    name='GDS Armor I', picture=AbilityPicture.phlebotomize,
    mp_cost=0, target_area='Self', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: Armor shields Marksman when operating the GDS. +2PRED',
    prerequisites=(stealth_snipe_2, slime_bomb_2,),
)

gds_armor_2 = Ability(
    name='GDS Armor II', picture=AbilityPicture.phlebotomize,
    mp_cost=0, target_area='Self', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: Armor shields Marksman when operating the GDS. +2MRED',
    prerequisites=(gds_armor_1,),
)

gds_armor_3 = Ability(
    name='GDS Armor III', picture=AbilityPicture.phlebotomize,
    mp_cost=0, target_area='Self', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: Armor shields Marksman when operating the GDS. '
           '+[[4+WIS]]PDEF, +[[4+WIS]]MDEF',
    prerequisites=(gds_armor_1,),
)

gds_tech_1 = Ability(
    name='GDS Tech I', picture=AbilityPicture.flaming_arrow,
    mp_cost=0, target_area='Self', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: Gigatonne Defense System. Adds Reaper Gatling I or II ability as FreeA',
    prerequisites=(siege_tech_mark_two_3, gatling_2,),
)

gds_tech_2 = Ability(
    name='GDS Tech II', picture=AbilityPicture.flaming_arrow,
    mp_cost=5, attacks=1, mdam='3d10+WIS', damage_type=DamageType.fire,
    targets_mdef=True, max_range='24+4*WIS', time=Time.full_a,
    shape=Shape.circle, target_area='2RAD',
    duration_unit=DurationUnit.instant,
    effect='Setup: 2FullA. Mount/Dismount: 1FullA.  Incendiary Rounds',
    prerequisites=(gds_tech_1,),
)

gds_tech_3 = Ability(
    name='GDS Tech I', picture=AbilityPicture.flaming_arrow,
    mp_cost=7, attacks=1, mdam='2d20+2*WIS', damage_type=DamageType.fire,
    targets_mdef=True, max_range='24+4*WIS', time=Time.full_a,
    shape=Shape.circle, target_area='3RAD',
    duration_unit=DurationUnit.instant,
    effect='Moonstrike (requires lunacite)',
    prerequisites=(gds_tech_2,),
)

gds_generator_1 = Ability(
    name='GDS Generator I', picture=AbilityPicture.flare,
    mp_cost=0, target_area='Allies in [[3+WIS]]RAD', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: GDS lunacite regenerates allies’ MP (not Marksman). Requires Lunacite. '
           '+1MP per REG',
    prerequisites=(slime_bomb_2, siege_tech_mark_two_2,),
)

gds_generator_2 = Ability(
    name='GDS Generator II', picture=AbilityPicture.flare,
    mp_cost=0, target_area='Allies in [[3+WIS]]RAD', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: GDS lunacite regenerates allies’ MP (not Marksman). Requires Lunacite. '
           '+[[WIS]]MP per REG',
    prerequisites=(gds_generator_1,),
)

gds_generator_3 = Ability(
    name='GDS Generator III', picture=AbilityPicture.flare,
    mp_cost=0, target_area='Allies in [[3+WIS]]RAD', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: GDS lunacite regenerates allies’ MP (not Marksman). Requires Lunacite. '
           '+[[2+WIS]]MP per REG',
    prerequisites=(gds_generator_1,),
)

gatling_mark_two_1 = Ability(
    name='Gatling Mark Two I', picture=AbilityPicture.steel_peak,
    mp_cost=7, attacks=8, mdam='3+WIS', damage_type=DamageType.force,
    targets_mdef=True, max_range='9+WIS', time=Time.std_a,
    shape=Shape.multi_point, target_area='Enemies',
    duration_unit=DurationUnit.instant,
    effect='Reaper: Buzz rounds',
    prerequisites=(gatling_3, dual_wield_2),
)

gatling_mark_two_2 = Ability(
    name='Gatling Mark Two II', picture=AbilityPicture.steel_peak,
    mp_cost=0, target_area='Self', time=Time.free_a,
    duration_unit=DurationUnit.instant,
    effect='Passive: Full speed when Reaper drawn',
    prerequisites=(gatling_mark_two_1,),
)

gatling_mark_two_3 = Ability(
    name='Gatling Mark Two III', picture=AbilityPicture.steel_peak,
    mp_cost=10, attacks=8, mdam='3+WIS', damage_type=DamageType.force,
    targets_mdef=True, max_range='9+WIS', time=Time.std_a,
    shape=Shape.multi_point, target_area='Enemies',
    duration_unit=DurationUnit.instant,
    effect='Reaper: Swarm rounds: -3SPEED on hit',
    prerequisites=(gatling_mark_two_2,),
)


class Marksman(Class):
    def __init__(self) -> None:
        super().__init__(
            name=self.__class__.__name__, hd=8, md=4, sd=4, speed=4, pdef=4, mdef=0.25,
            pred=0, mred=0, reg=1, vis=3, pac=1, mac=0.75, ath=4, ste=2, fort=1, apt=4,
            per=1, spe=2, starting_ap=4,
            use_ranged_light=True, use_ranged_medium=True, use_ranged_heavy=True,
            use_light_armor=True, use_medium_armor=True,
            abilities=(snipe_1, snipe_2, snipe_3,
                       quick_draw_1, quick_draw_2, quick_draw_3,
                       mortar_1, mortar_2, mortar_3,
                       smoke_bomb_1, smoke_bomb_2, smoke_bomb_3,
                       combat_enhancements_1, combat_enhancements_2, combat_enhancements_3,
                       stealth_snipe_1, stealth_snipe_2, stealth_snipe_3,
                       dual_wield_1, dual_wield_2, dual_wield_3,
                       siege_tech_mark_two_1, siege_tech_mark_two_2, siege_tech_mark_two_3,
                       slime_bomb_1, slime_bomb_2, slime_bomb_3,
                       gatling_1, gatling_2, gatling_3,
                       full_luna_jacket_1, full_luna_jacket_2, full_luna_jacket_3,
                       gds_armor_1, gds_armor_2, gds_armor_3,
                       gds_tech_1, gds_tech_2, gds_tech_3,
                       gds_generator_1, gds_generator_2, gds_generator_3,
                       gatling_mark_two_1, gatling_mark_two_2, gatling_mark_two_3,))
