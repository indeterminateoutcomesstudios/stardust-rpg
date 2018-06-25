from ..ability import Ability, AbilityPicture, DurationUnit, Time
from ..class_type import Class
from ..equipment import DamageType, Shape

jump_1 = Ability(
    name='Jump I', picture=AbilityPicture.spine_shatter_dive,
    mp_cost=2, target_area='One creature in [[2*@{SPEED}]]DIS', time=Time.full_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Jump into air, landing on opponent to ignore PRED on next attack, '
           'not targetable by melee attacks. Spend extra 1FullA in air before attacking.',
)

jump_2 = Ability(
    name='Jump II', picture=AbilityPicture.spine_shatter_dive,
    mp_cost=2, target_area='One creature in [[2*@{SPEED}+2]]DIS', time=Time.full_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Jump into air, landing on opponent to ignore PRED on next attack, '
           'not targetable by melee attacks. Spend extra 1FullA in air before attacking.',
    prerequisites=(jump_1,),
)

jump_3 = Ability(
    name='Jump III', picture=AbilityPicture.spine_shatter_dive,
    mp_cost=2, target_area='One creature in [[2*@{SPEED}+4]]DIS', time=Time.full_a,
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Jump into air, landing on opponent to ignore PRED and +1PDAM on next attack, '
           'not targetable by melee or ranged physical attacks. '
           'Spend extra 1FullA in air before attacking.',
    prerequisites=(jump_2,),
)

telesthesia_1 = Ability(
    name='Telesthesia I', picture=AbilityPicture.miasma,
    mp_cost=1, time=Time.bon_a,
    shape=Shape.circle, target_area='5RAD',
    duration_unit=DurationUnit.instant,
    effect='Detect the presence of living creatures',
)

telesthesia_2 = Ability(
    name='Telesthesia II', picture=AbilityPicture.miasma,
    mp_cost=2, time=Time.bon_a,
    shape=Shape.circle, target_area='[[5+WIS]]RAD',
    duration_unit=DurationUnit.instant,
    effect='Detect the presence, size, and number of living creatures',
    prerequisites=(telesthesia_1,),
)

telesthesia_3 = Ability(
    name='Telesthesia III', picture=AbilityPicture.miasma,
    mp_cost=2, time=Time.bon_a,
    shape=Shape.circle, target_area='[[5+2*WIS]]RAD',
    duration_unit=DurationUnit.instant,
    effect='Detect the number, size, and precise locations of living creatures',
    prerequisites=(telesthesia_2,),
)

confuse_1 = Ability(
    name='Confuse I', picture=AbilityPicture.wide_volley,
    mp_cost=1, attacks=1, mdam='1d4', damage_type=DamageType.psychic,
    targets_mdef=True, max_range='5',
    shape=Shape.point, target_area='1 enemy',
    duration='2', duration_unit=DurationUnit.rnd,
    effect='-4PAC, does not stack',
)

confuse_2 = Ability(
    name='Confuse II', picture=AbilityPicture.wide_volley,
    mp_cost=3, attacks=1, mdam='1d4', damage_type=DamageType.psychic,
    targets_mdef=True, max_range='5+WIS',
    shape=Shape.point, target_area='1 enemy',
    duration='2+WIS', duration_unit=DurationUnit.rnd,
    effect='Stagger, does not stack',
    prerequisites=(confuse_1,),
)

confuse_3 = Ability(
    name='Confuse III', picture=AbilityPicture.wide_volley,
    mp_cost=3, attacks=1, mdam='1d4', damage_type=DamageType.psychic,
    targets_mdef=True, max_range='5+WIS',
    shape=Shape.point, target_area='1 enemy',
    duration='2+WIS', duration_unit=DurationUnit.rnd,
    effect='Silence, does not stack',
    prerequisites=(confuse_2,),
)

parry_1 = Ability(
    name='Parry I', picture=AbilityPicture.feint,
    mp_cost=2, time=Time.re_a,
    shape=Shape.point, target_area='Self',
    duration_unit=DurationUnit.instant,
    effect='Counter: Can move 1DIS if target of melee attack to avoid a single melee attack',
)

parry_2 = Ability(
    name='Parry II', picture=AbilityPicture.feint,
    mp_cost=2, time=Time.re_a,
    shape=Shape.point, target_area='Self',
    duration_unit=DurationUnit.instant,
    effect='Counter: Can move 1DIS if target of ranged attack to avoid a single ranged attack',
    prerequisites=(parry_1,),
)

parry_3 = Ability(
    name='Parry III', picture=AbilityPicture.feint,
    mp_cost=2, time=Time.re_a,
    shape=Shape.point, target_area='Self',
    duration_unit=DurationUnit.instant,
    effect='Counter: Can cast Jump if target of melee or ranged attack to avoid attacks',
    prerequisites=(parry_2,),
)

synergize_1 = Ability(
    name='Synergize I', picture=AbilityPicture.succor,
    mp_cost=2,
    shape=Shape.circle, target_area='Self + Allies in 5RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='+2PAC, +2MAC',
)

synergize_2 = Ability(
    name='Synergize II', picture=AbilityPicture.succor,
    mp_cost=3,
    shape=Shape.circle, target_area='Self + Allies in 5RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='+2PAC, +[[2+WIS]]MAC',
    prerequisites=(synergize_1,),
)

synergize_3 = Ability(
    name='Synergize III', picture=AbilityPicture.succor,
    mp_cost=4,
    shape=Shape.circle, target_area='Self + Allies in 5RAD',
    duration='4', duration_unit=DurationUnit.rnd,
    effect='+[[2+WIS]]PAC, +[[2+WIS]]MAC',
    prerequisites=(synergize_2,),
)

# Tier 2.

hallucinate_1 = Ability(
    name='Hallucinate I', picture=AbilityPicture.rouse,
    mp_cost=3, attacks=1,
    targets_mdef=True, max_range='4',
    shape=Shape.point, target_area='1 enemy',
    duration='3', duration_unit=DurationUnit.rnd,
    effect='Causes target to see object of caster\'s choice',
    prerequisites=(telesthesia_2, confuse_3,),
)

hallucinate_2 = Ability(
    name='Hallucinate II', picture=AbilityPicture.rouse,
    mp_cost=4, attacks=1,
    targets_mdef=True, max_range='4+WIS',
    shape=Shape.point, target_area='1 enemy',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Causes target to see and hear object of caster\'s choice. Can cause Fear status '
           'effect',
    prerequisites=(hallucinate_1,),
)

hallucinate_3 = Ability(
    name='Hallucinate III', picture=AbilityPicture.rouse,
    mp_cost=6, attacks=1,
    targets_mdef=True, max_range='4+WIS',
    shape=Shape.circle, target_area='Enemies in [[WIS]]RAD',
    duration='3+WIS', duration_unit=DurationUnit.rnd,
    effect='Causes target to see, hear, and feel object of caster\'s choice. Can cause Fear '
           'status effect',
    prerequisites=(hallucinate_2,),
)

telepathy_1 = Ability(
    name='Telepathy I', picture=AbilityPicture.miasma_2,
    mp_cost=2, time=Time.bon_a, attacks=1, targets_mdef=True, max_range='5',
    shape=Shape.point, target_area='One person',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Sense emotions of a person',
    prerequisites=(telesthesia_3, synergize_2),
)

telepathy_2 = Ability(
    name='Telepathy II', picture=AbilityPicture.miasma_2,
    mp_cost=4, time=Time.bon_a, attacks=1, targets_mdef=True, max_range='5+WIS',
    shape=Shape.point, target_area='One person',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Sense thoughts of a person',
    prerequisites=(telepathy_1,),
)

telepathy_3 = Ability(
    name='Telepathy III', picture=AbilityPicture.miasma_2,
    mp_cost=4, time=Time.bon_a, attacks=1, targets_mdef=True, max_range='10+WIS',
    shape=Shape.point, target_area='One person',
    duration='5+WIS', duration_unit=DurationUnit.rnd,
    effect='Communicate with a person',
    prerequisites=(telepathy_2,),
)

flashback_1 = Ability(
    name='Flashback I', picture=AbilityPicture.sleep,
    mp_cost=6, time=Time.std_ab_a, attacks=1, targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One enemy',
    duration_unit=DurationUnit.instant,
    effect='Read a recent memory up to [[5+WIS]] minutes old',
    prerequisites=(confuse_2, parry_2),
)

flashback_2 = Ability(
    name='Flashback II', picture=AbilityPicture.sleep,
    mp_cost=8, time=Time.std_ab_a, attacks=1, targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One enemy',
    duration='10*WIS', duration_unit=DurationUnit.min,
    effect='Temporarily wipe a recent memory up to [[5+WIS]] minutes old',
    prerequisites=(flashback_1,),
)

flashback_3 = Ability(
    name='Flashback III', picture=AbilityPicture.sleep,
    mp_cost=12, time=Time.std_ab_a, attacks=1, targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One enemy',
    duration='5*WIS', duration_unit=DurationUnit.min,
    effect='Temporarily inject a recent memory up to [[5+WIS]] minutes old',
    prerequisites=(flashback_2,),
)

synchronize_1 = Ability(
    name='Synchronize I', picture=AbilityPicture.shukuchi,
    mp_cost=2,
    shape=Shape.multi_point, target_area='Allies who hit same target',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Allies who physically attack the same target as caster in same RND gain +[[d8]]PDAM',
    prerequisites=(jump_3, synergize_3,),
)

synchronize_2 = Ability(
    name='Synchronize II', picture=AbilityPicture.shukuchi,
    mp_cost=4,
    shape=Shape.multi_point, target_area='Allies who hit same target',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Allies who physically attack the same target as caster in same RND gain '
           '+[[d12+WIS]]PDAM',
    prerequisites=(synchronize_1,),
)

synchronize_3 = Ability(
    name='Synchronize III', picture=AbilityPicture.shukuchi,
    mp_cost=6,
    shape=Shape.multi_point, target_area='Allies who hit same target',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Allies who physically attack the same target as caster in same RND gain '
           '+[[2d10+2*WIS]]PDAM',
    prerequisites=(synchronize_2,),
)

shoulder_side_1 = Ability(
    name='Shoulder Side I', picture=AbilityPicture.shoulder_tackle,
    mp_cost=0,
    shape=Shape.point, target_area='One ally',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Passive: +1PRED to adjacent ally',
    prerequisites=(parry_3, synergize_2,),
)

shoulder_side_2 = Ability(
    name='Shoulder Side II', picture=AbilityPicture.shoulder_tackle,
    mp_cost=0,
    shape=Shape.multi_point, target_area='Self + One ally',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Passive: +1PRED to self and adjacent ally',
    prerequisites=(shoulder_side_1,),
)

shoulder_side_3 = Ability(
    name='Shoulder Side III', picture=AbilityPicture.shoulder_tackle,
    mp_cost=0,
    shape=Shape.multi_point, target_area='One ally',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Passive: Allows adjacent ally to cast Parry I, II, or III',
    prerequisites=(shoulder_side_1,),
)

# Tier 3.

numb_1 = Ability(
    name='Numb I', picture=AbilityPicture.physick,
    mp_cost=5, max_range='5',
    shape=Shape.point, target_area='One person',
    duration_unit=DurationUnit.instant,
    effect='Heal +[[2d12]]HP, can only be used on creature once every 3RND',
    prerequisites=(hallucinate_2, telepathy_2,),
)

numb_2 = Ability(
    name='Numb II', picture=AbilityPicture.physick,
    mp_cost=10, max_range='5+WIS',
    shape=Shape.point, target_area='One person',
    duration_unit=DurationUnit.instant,
    effect='Heal +[[2d20+WIS]]HP, can only be used on creature once every 3RND',
    prerequisites=(numb_1,),
)

numb_3 = Ability(
    name='Numb III', picture=AbilityPicture.physick,
    mp_cost=16, max_range='6+WIS',
    shape=Shape.point, target_area='One person',
    duration_unit=DurationUnit.instant,
    effect='Heal +[[3d20+2*WIS]]HP, can only be used on creature once every 3RND',
    prerequisites=(numb_2,),
)

dominate_1 = Ability(
    name='Dominate I', picture=AbilityPicture.sleep,
    mp_cost=3, time=Time.std_ab_a, attacks=1, targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.instant,
    effect='Control enemy\'s next MovA',
    prerequisites=(hallucinate_3, telepathy_3,),
)

dominate_2 = Ability(
    name='Dominate II', picture=AbilityPicture.sleep,
    mp_cost=8, time=Time.std_ab_a, attacks=1, targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.instant,
    effect='Control enemy\'s next StdA',
    prerequisites=(dominate_1,),
)

dominate_3 = Ability(
    name='Dominate III', picture=AbilityPicture.sleep,
    mp_cost=12, time=Time.std_ab_a, attacks=1, targets_mdef=True, max_range='1',
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.instant,
    effect='Control enemy\'s next FullA',
    prerequisites=(dominate_2,),
)

mind_cloak_1 = Ability(
    name='Mind Cloak I', picture=AbilityPicture.hide,
    mp_cost=6, time=Time.ab_a,
    shape=Shape.point, target_area='Self',
    duration='6+WIS', duration_unit=DurationUnit.rnd,
    effect='Caster becomes difficult to notice and can blends into a crowd/scene. 16PER to target',
    prerequisites=(hallucinate_2, shoulder_side_2,),
)

mind_cloak_2 = Ability(
    name='Mind Cloak II', picture=AbilityPicture.hide,
    mp_cost=6, time=Time.ab_a,
    shape=Shape.point, target_area='Self',
    duration='6+WIS', duration_unit=DurationUnit.rnd,
    effect='Target must be actively looking for caster to notice. 18PER to target',
    prerequisites=(hallucinate_2, shoulder_side_2,),
)

mind_cloak_3 = Ability(
    name='Mind Cloak III', picture=AbilityPicture.hide,
    mp_cost=10, time=Time.ab_a,
    shape=Shape.circle, target_area='Self + Allies in [[4+WIS]]RAD',
    duration='6+WIS', duration_unit=DurationUnit.rnd,
    effect='Caster and allies become difficult to notice unless target actively looking for them.'
           '18PER to target',
    prerequisites=(hallucinate_2, shoulder_side_2,),
)

psyche_flare_1 = Ability(
    name='Psyche Flare I', picture=AbilityPicture.shadow_flare,
    mp_cost=6, time=Time.full_a, attacks=1, mdam='1d20+WIS', damage_type=DamageType.psychic,
    targets_mdef=True, max_range='6',
    shape=Shape.point, target_area='1 enemy',
    duration='1', duration_unit=DurationUnit.rnd,
    effect='Powerful psychic burst silences creature',
    prerequisites=(telepathy_3, synchronize_3,),
)

psyche_flare_2 = Ability(
    name='Psyche Flare II', picture=AbilityPicture.shadow_flare,
    mp_cost=8, time=Time.full_a, attacks=1, mdam='"1d20+1d10+2*WIS"',
    damage_type=DamageType.psychic,
    targets_mdef=True, max_range='8+WIS',
    shape=Shape.point, target_area='1 enemy',
    duration='2', duration_unit=DurationUnit.rnd,
    effect='Powerful psychic burst silences creature',
    prerequisites=(psyche_flare_1,),
)

psyche_flare_3 = Ability(
    name='Psyche Flare III', picture=AbilityPicture.shadow_flare,
    mp_cost=10, time=Time.full_a, attacks=1, mdam='2d20+4*WIS', damage_type=DamageType.psychic,
    targets_mdef=True, max_range='10+WIS',
    shape=Shape.point, target_area='1 enemy',
    duration='2+WIS', duration_unit=DurationUnit.rnd,
    effect='Powerful psychic burst silences creature',
    prerequisites=(psyche_flare_1,),
)

mimic_1 = Ability(
    name='Mind Cloak I', picture=AbilityPicture.tri_disaster,
    mp_cost=5, max_range='1', time=Time.std_a,
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.instant,
    effect='Repeat a successful physical attack (its PAC, PDAM, Area) of another creature',
    prerequisites=(synchronize_2,),
)

mimic_2 = Ability(
    name='Mind Cloak II', picture=AbilityPicture.tri_disaster,
    mp_cost=5, max_range='3', time=Time.std_a,
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.instant,
    effect='Repeat a successful physical attack (its PAC, PDAM, Area) of another creature',
    prerequisites=(mimic_1,),
)

mimic_3 = Ability(
    name='Mind Cloak III', picture=AbilityPicture.tri_disaster,
    mp_cost=5, max_range='5+WIS', time=Time.std_a,
    shape=Shape.point, target_area='One creature',
    duration_unit=DurationUnit.instant,
    effect='Repeat a successful physical attack (its PAC, PDAM, Area) of another creature',
    prerequisites=(mimic_2,),
)


class Telepath(Class):
    def __init__(self) -> None:
        super().__init__(
            name=self.__class__.__name__, hd=8, md=6, sd=4, speed=5, pdef=4, mdef=1.25,
            pred=0, mred=1, reg=0.75, vis=3, pac=0.75, mac=1, ath=2, ste=4, fort=1, apt=1,
            per=4, spe=4, starting_ap=4, use_melee_light=True,
            use_ranged_light=True, use_ranged_medium=True, use_ranged_heavy=True,
            use_magic_light=True, use_magic_medium=True, use_magic_heavy=True,
            use_light_armor=True,
            abilities=(jump_1, jump_2, jump_3,
                       telesthesia_1, telesthesia_2, telesthesia_3,
                       confuse_1, confuse_2, confuse_3,
                       parry_1, parry_2, parry_3,
                       synergize_1, synergize_2, synergize_3,
                       hallucinate_1, hallucinate_2, hallucinate_3,
                       telepathy_1, telepathy_2, telepathy_3,
                       flashback_1, flashback_2, flashback_3,
                       synchronize_1, synchronize_2, synchronize_3,
                       shoulder_side_1, shoulder_side_2, shoulder_side_3,
                       numb_1, numb_2, numb_3,
                       dominate_1, dominate_2, dominate_3,
                       mind_cloak_1, mind_cloak_2, mind_cloak_3,
                       psyche_flare_1, psyche_flare_2, psyche_flare_3,
                       mimic_1, mimic_2, mimic_3))
