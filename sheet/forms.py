from django import forms

from .models import level_up


class LevelUpForm(forms.ModelForm):
    class Meta:
        model = level_up.LevelUp
        fields = ['hd_roll', 'md_roll', 'sd_roll', 'ad_roll', 'selected_attribute']
