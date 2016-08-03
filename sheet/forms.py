from django import forms

import enumfields

from .models import character, inventory_slot, items, level_up


class CharacterEquipForm(forms.ModelForm):
    class Meta:
        model = character.Character
        fields = ['head_enum', 'neck_enum', 'chest_enum', 'shield_enum',
                  'right_hand_enum', 'left_hand_enum', 'feet_enum', 'weapon_enum']


class InventorySlotForm(forms.ModelForm):
    class Meta:
        model = inventory_slot.InventorySlot
        fields = ['slot', 'quantity']


class ItemForm(forms.Form):
    item_enum = enumfields.EnumIntegerField(items.Items, verbose_name='Item').formfield()


class UtilityForm(forms.Form):
    item_enum = enumfields.EnumIntegerField(items.Utilities, verbose_name='Utility').formfield()


class WeaponForm(forms.Form):
    item_enum = enumfields.EnumIntegerField(items.Weapons, verbose_name='Weapon').formfield()


class HeadForm(forms.Form):
    item_enum = enumfields.EnumIntegerField(items.Heads, verbose_name='Head').formfield()


class NeckForm(forms.Form):
    item_enum = enumfields.EnumIntegerField(items.Necks, verbose_name='Neck').formfield()


class ChestForm(forms.Form):
    item_enum = enumfields.EnumIntegerField(items.Chests, verbose_name='Chest').formfield()


class ShieldForm(forms.Form):
    item_enum = enumfields.EnumIntegerField(items.Shields, verbose_name='Shield').formfield()


class HandForm(forms.Form):
    item_enum = enumfields.EnumIntegerField(items.Hands, verbose_name='Hand').formfield()


class FeetForm(forms.Form):
    item_enum = enumfields.EnumIntegerField(items.Feets, verbose_name='Feet').formfield()


class LevelUpForm(forms.ModelForm):
    class Meta:
        model = level_up.LevelUp
        fields = ['hd_roll', 'md_roll', 'sd_roll', 'ad_roll', 'selected_attribute']


class SkillPointsForm(forms.ModelForm):
    class Meta:
        model = character.Character
        fields = ['assigned_ath', 'assigned_ste', 'assigned_for', 'assigned_apt',
                  'assigned_per', 'assigned_spe']


class Roll20Form(forms.Form):
    sync_attributes = forms.BooleanField(label='Sync Attributes', required=False, initial=True)
    sync_current_hp_mp = forms.BooleanField(label='Sync Current HP/MP', required=False)
    sync_abilities = forms.BooleanField(label='Sync Abilities', required=False, initial=True)
    sync_combos = forms.BooleanField(label='Sync Combos', required=False, initial=True)
    sync_weapons = forms.BooleanField(label='Sync Weapons', required=False, initial=True)
    sync_utilities = forms.BooleanField(label='Sync Utilities', required=False, initial=True)
    password = forms.CharField(label='Roll20 Password', widget=forms.PasswordInput())
