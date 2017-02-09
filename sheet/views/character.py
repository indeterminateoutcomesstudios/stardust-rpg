import re
from typing import Dict, Sequence, Tuple  # noqa: F401

from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from formtools.wizard.views import SessionWizardView

from ..forms import CharacterEquipForm, LevelUpForm, Roll20Form, SkillPointsForm
from ..models import equipment, items, macro  # noqa: F401
from ..models.abilities import inverse_abilities
from ..models.character import Character, UnlockedAbility
from ..models.equipment import Slot
from ..models.inventory_slot import InventorySlot
from ..models.level_up import LevelUp
from ..models.shop import Shop, ShopSlot
from ..roll20 import api, login


def owns_character_or_superuser(request: HttpRequest, character: Character) -> bool:
    if request.user.is_superuser or character.user.username == request.user.username:
        return True
    else:
        messages.error(request, 'User not authorized to edit this character.')
        return False


@login_required
def stats(request: HttpRequest, character_id: str) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'character/stats.html', context={'character': character,
                                                            'Rarity': equipment.Rarity})


@login_required
def cls(request: HttpRequest, character_id: str) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'character/class.html', context={'character': character})


@login_required
def party(request: HttpRequest, character_id: str) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'character/party.html', context={'character': character})


@login_required
def shops(request: HttpRequest, character_id: str, shop_id: str) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    shop = get_object_or_404(Shop, pk=shop_id)
    if not shop.visible:
        messages.error(request, f'{shop.name} shop is not visible')
        return redirect(reverse(party, args=[character.id]))
    if shop.party != character.party:
        messages.error(request, f'Shop is not available for party {shop.party.name}.')
        return redirect(reverse(party, args=[character.id]))
    if request.method == 'POST' and request.user.is_superuser:
        # Check if a delete input button was pressed to remove an ShopSlot.
        for parameter, value in request.POST.items():
            match = re.match(r'^delete\s(?P<shop_slot_id>[0-9]+)$', value)
            if match is not None:
                ShopSlot.objects.get(pk=match.group('shop_slot_id')).delete()

    return render(request, 'character/shop.html',
                  context={'character': character,
                           'shop': shop,
                           'user': request.user,
                           'Rarity': equipment.Rarity,
                           'Slot': Slot})


@login_required
def unlock_abilities(request: HttpRequest, character_id: str) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST' and owns_character_or_superuser(request, character):
        for parameter, value in request.POST.items():
            match = re.match(r'^(?P<action_type>lock|unlock)\s(?P<ability_index>[0-9]+)$', value)
            if match is not None:
                ability_index = int(match.group('ability_index'))
                ability = character.cls.abilities[ability_index]

                action_type = match.group('action_type')
                if action_type == 'lock':
                    for unlocked_ability in character.unlockedability_set.all():
                        if unlocked_ability.ability is ability:
                            # Do not allow the player to re-lock an ability if it is a
                            # prerequisite for another ability they have already unlocked.
                            lock_ability = True
                            for owned_ability in character.unlocked_abilities:
                                if ability in owned_ability.prerequisites:
                                    messages.error(request,
                                                   f'Cannot lock ability {ability.name} because '
                                                   f'it is a prerequisite for '
                                                   f'{owned_ability.name}.')
                                    lock_ability = False
                            if lock_ability:
                                unlocked_ability.delete()
                elif action_type == 'unlock':
                    if character.available_ap > 0:
                        new_unlocked_ability = UnlockedAbility(
                            character=character,
                            ability_enum=inverse_abilities[ability])
                        new_unlocked_ability.save()
                    else:
                        messages.error(request, 'Not enough available AP.')

        return redirect(reverse(unlock_abilities, args=[character.id]))

    return render(request, 'character/abilities.html', context={'character': character})


@login_required
def combos(request: HttpRequest, character_id: str) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'character/combos.html', context={'character': character})


@login_required
def equip(request: HttpRequest, character_id: str) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST' and owns_character_or_superuser(request, character):
        equip_form = CharacterEquipForm(request.POST)
        if equip_form.is_valid():
            character.head_enum = equip_form.cleaned_data['head_enum']
            character.neck_enum = equip_form.cleaned_data['neck_enum']
            character.chest_enum = equip_form.cleaned_data['chest_enum']
            character.shield_enum = equip_form.cleaned_data['shield_enum']
            character.right_hand_enum = equip_form.cleaned_data['right_hand_enum']
            character.left_hand_enum = equip_form.cleaned_data['left_hand_enum']
            character.feet_enum = equip_form.cleaned_data['feet_enum']
            character.weapon_enum = equip_form.cleaned_data['weapon_enum']

            # Validate character meets requirements for equipment.
            if (character.get_attribute(character.head.min_attribute) <
               character.head.min_attribute_value):
                equip_form.add_error('head_enum',
                                     error='Requirements not met for {}.  Need {}{}.'.format(
                                         character.head.name,
                                         character.head.min_attribute_value,
                                         character.head.min_attribute.name.upper()))
            elif (character.get_attribute(character.neck.min_attribute) <
                  character.neck.min_attribute_value):
                equip_form.add_error('neck_enum',
                                     error='Requirements not met for {}.  Need {}{}.'.format(
                                         character.neck.name,
                                         character.neck.min_attribute_value,
                                         character.neck.min_attribute.name.upper()))
            elif (character.get_attribute(character.chest.min_attribute) <
                  character.chest.min_attribute_value):
                equip_form.add_error('chest_enum',
                                     error='Requirements not met for {}.  Need {}{}.'.format(
                                         character.chest.name,
                                         character.chest.min_attribute_value,
                                         character.chest.min_attribute.name.upper()))
            elif (character.get_attribute(character.shield.min_attribute) <
                  character.shield.min_attribute_value):
                equip_form.add_error('shield_enum',
                                     error='Requirements not met for {}.  Need {}{}.'.format(
                                         character.shield.name,
                                         character.shield.min_attribute_value,
                                         character.shield.min_attribute.name.upper()))
            elif (character.get_attribute(character.right_hand.min_attribute) <
                  character.right_hand.min_attribute_value):
                equip_form.add_error('right_hand_enum',
                                     error='Requirements not met for {}.  Need {}{}.'.format(
                                         character.right_hand.name,
                                         character.right_hand.min_attribute_value,
                                         character.right_hand.min_attribute.name.upper()))
            elif (character.get_attribute(character.left_hand.min_attribute) <
                  character.left_hand.min_attribute_value):
                equip_form.add_error('left_hand_enum',
                                     error='Requirements not met for {}.  Need {}{}.'.format(
                                         character.left_hand.name,
                                         character.left_hand.min_attribute_value,
                                         character.left_hand.min_attribute.name.upper()))
            elif (character.get_attribute(character.feet.min_attribute) <
                  character.feet.min_attribute_value):
                equip_form.add_error('feet_enum',
                                     error='Requirements not met for {}.  Need {}{}.'.format(
                                         character.feet.name,
                                         character.feet.min_attribute_value,
                                         character.feet.min_attribute.name.upper()))
            elif (character.get_attribute(character.weapon.min_attribute) <
                  character.weapon.min_attribute_value):
                equip_form.add_error('weapon_enum',
                                     error='Requirements not met for {}.  Need {}{}.'.format(
                                         character.weapon.name,
                                         character.weapon.min_attribute_value,
                                         character.weapon.min_attribute.name.upper()))
            elif (character.weapon.is_two_handed and
                    character.shield_enum is not items.Shields.empty):
                equip_form.add_error('shield_enum',
                                     error='Cannot equip a shield and a two-handed weapon.')
            elif ((character.right_hand.is_two_handed and
                    character.left_hand_enum is not items.Hands.empty) or
                    (character.left_hand.is_two_handed and
                     character.right_hand_enum is not items.Hands.empty)):
                equip_form.add_error('right_hand_enum',
                                     error='Cannot equip two-handed Hand item and an item in '
                                           'other hand.')
            elif not character.can_use_weapon:
                equip_form.add_error('weapon_enum',
                                     error=f'Class {character.cls.name} '
                                           f'cannot use {character.weapon.style.name} '
                                           f'{character.weapon.type.name} weapons')
            else:
                character.save()
                return redirect(reverse(stats, args=[character.id]))
    else:
        equip_form = CharacterEquipForm(
            initial={
                'head_enum': character.head_enum,
                'neck_enum': character.neck_enum,
                'chest_enum': character.chest_enum,
                'shield_enum': character.shield_enum,
                'right_hand_enum': character.right_hand_enum,
                'left_hand_enum': character.left_hand_enum,
                'feet_enum': character.feet_enum,
                'weapon_enum': character.weapon_enum
            })

    return render(request, 'character/equip.html',
                  context={'equip_form': equip_form,
                           'character': character})


def show_item_form_condition(wizard: SessionWizardView) -> bool:
    return inventory_wizard_slot_was_chosen(wizard=wizard, slot=Slot.item)


def show_utility_form_condition(wizard: SessionWizardView) -> bool:
    return inventory_wizard_slot_was_chosen(wizard=wizard, slot=Slot.utility)


def show_weapon_form_condition(wizard: SessionWizardView) -> bool:
    return inventory_wizard_slot_was_chosen(wizard=wizard, slot=Slot.weapon)


def show_head_form_condition(wizard: SessionWizardView) -> bool:
    return inventory_wizard_slot_was_chosen(wizard=wizard, slot=Slot.head)


def show_neck_form_condition(wizard: SessionWizardView) -> bool:
    return inventory_wizard_slot_was_chosen(wizard=wizard, slot=Slot.neck)


def show_chest_form_condition(wizard: SessionWizardView) -> bool:
    return inventory_wizard_slot_was_chosen(wizard=wizard, slot=Slot.chest)


def show_shield_form_condition(wizard: SessionWizardView) -> bool:
    return inventory_wizard_slot_was_chosen(wizard=wizard, slot=Slot.shield)


def show_hand_form_condition(wizard: SessionWizardView) -> bool:
    return inventory_wizard_slot_was_chosen(wizard=wizard, slot=Slot.hand)


def show_feet_form_condition(wizard: SessionWizardView) -> bool:
    return inventory_wizard_slot_was_chosen(wizard=wizard, slot=Slot.feet)


def inventory_wizard_slot_was_chosen(wizard: SessionWizardView, slot: Slot) -> bool:
    slot_cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    return slot is slot_cleaned_data.get('slot')


class ItemSelectionWizard(SessionWizardView):
    @staticmethod
    def get_forms(form_dict: Dict[str, forms.Form]) -> Tuple[forms.Form, forms.Form]:
        inventory_slot_form = form_dict['0']
        # The last item in the OrderedDict (popitem) will be the specific Item Form,
        # whose key is its step (will vary depending on which slot was chosen.
        item_form = form_dict.popitem()[1]
        return inventory_slot_form, item_form

    def done(self, form_list: Sequence[forms.Form], **kwargs) -> None:
        """Call base class done(), effectively making this class abstract."""
        super().done(form_list, **kwargs)


class InventorySlotWizard(ItemSelectionWizard):
    def done(self, form_list: Sequence[forms.Form], form_dict: Dict[str, forms.Form],
             character_id: str, **kwargs) -> HttpResponse:
        character = get_object_or_404(Character, pk=character_id)
        inventory_slot_form, item_form = self.get_forms(form_dict)
        new_inventory_slot = InventorySlot(
            character=character,
            slot=inventory_slot_form.cleaned_data['slot'],
            quantity=inventory_slot_form.cleaned_data['quantity'],
            item_index=item_form.cleaned_data['item_enum'].value)
        new_inventory_slot.save()
        return redirect(reverse(inventory, args=[character.id]))


class ShopSlotWizard(ItemSelectionWizard):
    def done(self, form_list: Sequence[forms.Form], form_dict: Dict[str, forms.Form],
             character_id: str, shop_id: str, **kwargs) -> HttpResponse:
        character = get_object_or_404(Character, pk=character_id)
        shop = get_object_or_404(Shop, pk=shop_id)

        if self.request.user.is_superuser:
            inventory_slot_form, item_form = self.get_forms(form_dict)
            new_shop_slot = ShopSlot(
                shop=shop,
                slot=inventory_slot_form.cleaned_data['slot'],
                quantity=inventory_slot_form.cleaned_data['quantity'],
                item_index=item_form.cleaned_data['item_enum'].value)
            new_shop_slot.save()
        else:
            messages.error(self.request, 'User not authorized to edit this shop.')
        return redirect(reverse(shops, args=[character.id, shop.id]))


def inventory(request: HttpRequest, character_id: str) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST' and owns_character_or_superuser(request, character):
        # Check if a delete input button was pressed to remove an InventorySlot.
        for parameter, value in request.POST.items():
            match = re.match(r'^delete\s(?P<inventory_slot_id>[0-9]+)$', value)
            if match is not None:
                InventorySlot.objects.get(pk=match.group('inventory_slot_id')).delete()

    return render(request, 'character/inventory.html',
                  context={'character': character,
                           'Rarity': equipment.Rarity})


@login_required
def level_up(request: HttpRequest, character_id: str) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST' and owns_character_or_superuser(request, character):
        level_up_form = LevelUpForm(request.POST)

        # Check if a delete input button was pressed to remove an old LevelUp.
        for parameter, value in request.POST.items():
            match = re.match(r'^delete\s(?P<levelup_id>[0-9]+)$', value)
            if match is not None:
                LevelUp.objects.get(pk=match.group('levelup_id')).delete()
                # If a delete button was pushed, clear out the new level form.
                level_up_form = LevelUpForm()

        # Otherwise, user is creating a new LevelUp.
        if level_up_form.is_valid():
            hd_roll = level_up_form.cleaned_data['hd_roll']
            md_roll = level_up_form.cleaned_data['md_roll']
            sd_roll = level_up_form.cleaned_data['sd_roll']
            if hd_roll > character.cls.hd:
                level_up_form.add_error('hd_roll',
                                        error=f'HD roll higher than HD: '
                                              f'{hd_roll}>{character.cls.hd}')
            elif md_roll > character.cls.md:
                level_up_form.add_error('md_roll',
                                        error=f'MD roll higher than MD: '
                                              f'{md_roll}>{character.cls.md}')
            elif sd_roll > character.cls.sd:
                level_up_form.add_error('sd_roll',
                                        error=f'SD roll higher than SD: '
                                              f'{sd_roll}>{character.cls.sd}')
            elif (character.lvl == 0 and
                  (hd_roll != character.cls.hd or
                   md_roll != character.cls.md or
                   sd_roll != character.cls.sd)):
                level_up_form.add_error('hd_roll',
                                        error='For LVL 1: HD, MD, and SD are assigned maximum '
                                              'roll values.')
            else:
                new_level_up = level_up_form.save(commit=False)
                new_level_up.character = character
                new_level_up.save()
                level_up_form = LevelUpForm()
    else:
        if character.lvl == 0:
            level_up_form = LevelUpForm(
                initial={'hd_roll': character.cls.hd,
                         'md_roll': character.cls.md,
                         'sd_roll': character.cls.sd})
        else:
            level_up_form = LevelUpForm()

    return render(request, 'character/level_up.html',
                  context={'level_up_form': level_up_form,
                           'character': character})


@login_required
def skill_points(request: HttpRequest, character_id: str) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST' and owns_character_or_superuser(request, character):
        skill_points_form = SkillPointsForm(request.POST)
        if skill_points_form.is_valid():
            assigned_ath = skill_points_form.cleaned_data['assigned_ath']
            assigned_ste = skill_points_form.cleaned_data['assigned_ste']
            assigned_for = skill_points_form.cleaned_data['assigned_for']
            assigned_apt = skill_points_form.cleaned_data['assigned_apt']
            assigned_per = skill_points_form.cleaned_data['assigned_per']
            assigned_spe = skill_points_form.cleaned_data['assigned_spe']
            if (assigned_ath + assigned_ste + assigned_for + assigned_apt + assigned_per +
                    assigned_spe > character.sp):
                messages.error(request, f'Too many SP assigned. Max: {character.sp}')
            elif assigned_ath > character.max_sp_per_skill:
                skill_points_form.add_error('assigned_ath',
                                            error=f'Assigned ATH too high. '
                                                  f'Max: {character.max_sp_per_skill}')
            elif assigned_ste > character.max_sp_per_skill:
                skill_points_form.add_error('assigned_ste',
                                            error=f'Assigned STE too high. '
                                                  f'Max: {character.max_sp_per_skill}')
            elif assigned_for > character.max_sp_per_skill:
                skill_points_form.add_error('assigned_for',
                                            error=f'Assigned FOR too high. '
                                                  f'Max: {character.max_sp_per_skill}')
            elif assigned_apt > character.max_sp_per_skill:
                skill_points_form.add_error('assigned_apt',
                                            error=f'Assigned APT too high. '
                                                  f'Max: {character.max_sp_per_skill}')
            elif assigned_per > character.max_sp_per_skill:
                skill_points_form.add_error('assigned_per',
                                            error=f'Assigned PER too high. '
                                                  f'Max: {character.max_sp_per_skill}')
            elif assigned_spe > character.max_sp_per_skill:
                skill_points_form.add_error('assigned_spe',
                                            error=f'Assigned SPE too high. '
                                                  f'Max: {character.max_sp_per_skill}')
            else:
                character.assigned_ath = assigned_ath
                character.assigned_ste = assigned_ste
                character.assigned_for = assigned_for
                character.assigned_apt = assigned_apt
                character.assigned_per = assigned_per
                character.assigned_spe = assigned_spe
                character.save()
                messages.info(request, 'Skill points successfully assigned.')
    else:
        skill_points_form = SkillPointsForm(
            initial={'assigned_ath': character.assigned_ath,
                     'assigned_ste': character.assigned_ste,
                     'assigned_for': character.assigned_for,
                     'assigned_apt': character.assigned_apt,
                     'assigned_per': character.assigned_per,
                     'assigned_spe': character.assigned_spe}
        )

    return render(request, 'character/skill_points.html',
                  context={'skill_points_form': skill_points_form,
                           'character': character})


@login_required
def roll20(request: HttpRequest, character_id: str) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST' and owns_character_or_superuser(request, character):
        roll20_form = Roll20Form(request.POST)
        if roll20_form.is_valid():
            password = roll20_form.cleaned_data['password']
            sync_attributes = roll20_form.cleaned_data['sync_attributes']
            sync_current_hp_mp = roll20_form.cleaned_data['sync_current_hp_mp']
            sync_abilities = roll20_form.cleaned_data['sync_abilities']
            sync_combos = roll20_form.cleaned_data['sync_combos']
            sync_weapons = roll20_form.cleaned_data['sync_weapons']
            sync_utilities = roll20_form.cleaned_data['sync_utilities']

            if sync_current_hp_mp and not sync_attributes:
                roll20_form.add_error('sync_current_hp_mp',
                                      error='Cannot sync current HP and MP without attributes.')
            else:
                try:
                    roll20_login = login.login(email=request.user.email, password=password,
                                               campaign_id=character.party.roll20_campaign_id)
                    character_id = api.get_character_id(login=roll20_login,
                                                        character_name=character.name)
                    attributes_to_sync_both = {
                        'Name': character.name,
                        'LVL': character.lvl,
                        'SPEED': character.speed,
                        'PDEF': character.pdef,
                        'MDEF': character.mdef,
                        'PRED': character.pred,
                        'MRED': character.mred,
                        'REG': character.reg,
                        'RD': character.rd,
                        'VIS': character.vis,
                        'BPAC': character.bpac,
                        'BMAC': character.bmac,
                        'ATH': character.ath,
                        'STE': character.ste,
                        'FOR': character.fort,
                        'APT': character.apt,
                        'PER': character.per,
                        'SPE': character.spe,
                        'STR': character.stren,
                        'DEX': character.dex,
                        'CON': character.con,
                        'INT': character.intel,
                        'WIS': character.wis,
                        'CHA': character.cha,
                        'HD': 'd' + str(character.cls.hd),
                        'MD': 'd' + str(character.cls.md),
                        'SD': 'd' + str(character.cls.sd),

                        'SlashingVUL': int(character.vul_set.vul.slashing),
                        'PiercingVUL': int(character.vul_set.vul.piercing),
                        'BludgeoningVUL': int(character.vul_set.vul.bludgeoning),
                        'FireVUL': int(character.vul_set.vul.fire),
                        'ColdVUL': int(character.vul_set.vul.cold),
                        'LightningVUL': int(character.vul_set.vul.lightning),
                        'AcidVUL': int(character.vul_set.vul.acid),
                        'PoisonVUL': int(character.vul_set.vul.poison),
                        'ForceVUL': int(character.vul_set.vul.force),
                        'PsychicVUL': int(character.vul_set.vul.psychic),

                        'SlashingRES': int(character.vul_set.res.slashing),
                        'PiercingRES': int(character.vul_set.res.piercing),
                        'BludgeoningRES': int(character.vul_set.res.bludgeoning),
                        'FireRES': int(character.vul_set.res.fire),
                        'ColdRES': int(character.vul_set.res.cold),
                        'LightningRES': int(character.vul_set.res.lightning),
                        'AcidRES': int(character.vul_set.res.acid),
                        'PoisonRES': int(character.vul_set.res.poison),
                        'ForceRES': int(character.vul_set.res.force),
                        'PsychicRES': int(character.vul_set.res.psychic),

                        'SlashingIMU': int(character.vul_set.imu.slashing),
                        'PiercingIMU': int(character.vul_set.imu.piercing),
                        'BludgeoningIMU': int(character.vul_set.imu.bludgeoning),
                        'FireIMU': int(character.vul_set.imu.fire),
                        'ColdIMU': int(character.vul_set.imu.cold),
                        'LightningIMU': int(character.vul_set.imu.lightning),
                        'AcidIMU': int(character.vul_set.imu.acid),
                        'PoisonIMU': int(character.vul_set.imu.poison),
                        'ForceIMU': int(character.vul_set.imu.force),
                        'PsychicIMU': int(character.vul_set.imu.psychic),
                    }

                    hp_mp_attributes = {'HP': character.hp, 'MP': character.mp}
                    if sync_current_hp_mp:
                        attributes_to_sync_current = {**attributes_to_sync_both,
                                                      **hp_mp_attributes}
                    else:
                        attributes_to_sync_current = attributes_to_sync_both

                    attributes_to_sync_max = {**attributes_to_sync_both, **hp_mp_attributes}

                    if sync_attributes:
                        api.set_attributes(login=roll20_login, character_id=character_id,
                                           attributes=attributes_to_sync_current,
                                           attribute_position=api.AttributePosition.current)
                        api.set_attributes(login=roll20_login, character_id=character_id,
                                           attributes=attributes_to_sync_max,
                                           attribute_position=api.AttributePosition.max)

                    abilities_to_sync: Tuple[macro.Macroable, ...] = ()
                    if sync_abilities:
                        abilities_to_sync += character.unlocked_abilities
                    if sync_combos:
                        abilities_to_sync += character.unlocked_combos
                    if sync_weapons:
                        abilities_to_sync += (character.weapon,)
                    if sync_utilities:
                        abilities_to_sync += character.utilities
                    for ability in abilities_to_sync:
                        if not api.ability_exists(login=roll20_login, character_id=character_id,
                                                  ability_name=ability.name):
                            api.create_ability(login=roll20_login, character_id=character_id,
                                               ability_name=ability.name,
                                               ability_action=ability.macro)
                        else:
                            api.update_ability(login=roll20_login, character_id=character_id,
                                               ability_name=ability.name,
                                               ability_action=ability.macro)
                    messages.info(request, f'Macros synced successfully to '
                                           f'{roll20_login.campaign_name}.')

                except (login.Roll20AuthenticationError, RuntimeError,
                        api.Roll20CharacterNotFoundError) as ex:
                    messages.error(request, str(ex))
                    return redirect(reverse(roll20, args=[character.id]))

    else:
        roll20_form = Roll20Form()

    return render(request, 'character/roll20.html',
                  context={'roll20_form': roll20_form,
                           'character': character,
                           'user': request.user})
