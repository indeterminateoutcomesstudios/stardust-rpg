from django import forms

from .models import character, level_up


class CharacterEquipForm(forms.ModelForm):
    class Meta:
        model = character.Character
        fields = ['utility_enum', 'head_enum', 'neck_enum', 'chest_enum', 'shield_enum',
                  'hand_enum', 'feet_enum', 'weapon_enum']


class LevelUpForm(forms.ModelForm):
    class Meta:
        model = level_up.LevelUp
        fields = ['hd_roll', 'md_roll', 'sd_roll', 'ad_roll', 'selected_attribute']
