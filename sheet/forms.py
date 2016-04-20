from django import forms

from .models.character import LevelUp


class LevelUpForm(forms.ModelForm):
    class Meta:
        model = LevelUp
        fields = ['hd_roll', 'md_roll', 'sd_roll', 'ad_roll', 'selected_attribute']
