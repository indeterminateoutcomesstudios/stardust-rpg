from django import forms

from .models import character, level_up


class CharacterEquipForm(forms.ModelForm):
    class Meta:
        model = character.Character
        fields = ['utility_enum', 'head_enum', 'neck_enum', 'chest_enum', 'shield_enum',
                  'right_hand_enum', 'left_hand_enum', 'feet_enum', 'weapon_enum']


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
    sync_abilities = forms.BooleanField(label='Sync Abilities', required=False, initial=True)
    sync_combos = forms.BooleanField(label='Sync Combos', required=False, initial=True)
    sync_weapons = forms.BooleanField(label='Sync Weapons', required=False, initial=True)
    sync_utilities = forms.BooleanField(label='Sync Utilities', required=False, initial=True)
    password = forms.CharField(label='Roll20 Password', widget=forms.PasswordInput())
