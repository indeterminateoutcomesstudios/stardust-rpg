import enumfields
from django.core import validators
from django.db import models

from .character import Attribute, Character


class LevelUp(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    hd_roll = models.IntegerField(verbose_name='HD Roll',
                                  validators=[validators.MinValueValidator(1)])
    md_roll = models.IntegerField(verbose_name='MD Roll',
                                  validators=[validators.MinValueValidator(1)])
    sd_roll = models.IntegerField(verbose_name='SD Roll',
                                  validators=[validators.MinValueValidator(1)])
    ad_roll = enumfields.EnumIntegerField(verbose_name='AD Roll',
                                          enum=Attribute, default=Attribute.stren)
    selected_attribute = enumfields.EnumIntegerField(verbose_name='Selected Attribute',
                                                     enum=Attribute, default=Attribute.stren)
