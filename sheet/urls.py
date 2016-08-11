from django.conf.urls import url

from . import forms
from . import views
from .models import ability, equipment, items

item_selection_form_list = [forms.InventorySlotForm,
                            forms.ItemForm,
                            forms.UtilityForm,
                            forms.WeaponForm,
                            forms.HeadForm,
                            forms.NeckForm,
                            forms.ChestForm,
                            forms.ShieldForm,
                            forms.HandForm,
                            forms.FeetForm]
"""Forms associated with the ItemSelectionWizard."""

item_selection_condition_dict = {'1': views.character.show_item_form_condition,
                                 '2': views.character.show_utility_form_condition,
                                 '3': views.character.show_weapon_form_condition,
                                 '4': views.character.show_head_form_condition,
                                 '5': views.character.show_neck_form_condition,
                                 '6': views.character.show_chest_form_condition,
                                 '7': views.character.show_shield_form_condition,
                                 '8': views.character.show_hand_form_condition,
                                 '9': views.character.show_feet_form_condition}
"""Conditions associated with the ItemSelectionWizard."""

urlpatterns = [
    # Browser
    url(r'^parties/$', views.browser.parties, name='sheet-views-parties'),
    url(r'^classes/$', views.browser.all_classes, name='sheet-views-classes'),
    url(r'^classes/(?P<class_name>[A-Za-z]+)/abilities/$', views.browser.class_abilities,
        name='sheet-views-class-abilities'),
    url(r'^combos/$', views.browser.all_combos, name='sheet-views-all-combos'),
    url(r'^heads/$', views.browser.all_equipment, {'wearables': items.heads.values()},
        name='sheet-views-heads'),
    url(r'^necks/$', views.browser.all_equipment, {'wearables': items.necks.values()},
        name='sheet-views-necks'),
    url(r'^chests/$', views.browser.all_equipment, {'wearables': items.chests.values()},
        name='sheet-views-chests'),
    url(r'^shields/$', views.browser.all_equipment, {'wearables': items.shields.values()},
        name='sheet-views-shields'),
    url(r'^hands/$', views.browser.all_equipment, {'wearables': items.hands.values()},
        name='sheet-views-hands'),
    url(r'^feets/$', views.browser.all_equipment, {'wearables': items.feets.values()},
        name='sheet-views-feets'),
    url(r'^utilities/$', views.browser.all_equipment, {'wearables': items.utilities.values()},
        name='sheet-views-utilities'),
    url(r'^weapons/$', views.browser.all_weapons, {'weapons': items.weapons.values()},
        name='sheet-views-weapons'),
    url(r'^items/$', views.browser.all_items, {'item_set': items.items.values()},
        name='sheet-views-items'),
    url(r'^shape_pictures/$', views.browser.pictures, {'picture_enum': equipment.Shape},
        name='sheet-views-shape-pictures'),
    url(r'^weapon_pictures/$', views.browser.pictures, {'picture_enum': equipment.WeaponPicture},
        name='sheet-views-weapon-pictures'),
    url(r'^ability_pictures/$', views.browser.pictures, {'picture_enum': ability.AbilityPicture},
        name='sheet-views-ability-pictures'),

    # Character
    url(r'^(?P<character_id>[0-9]+)/stats/$', views.character.stats, name='sheet-views-stats'),
    url(r'^(?P<character_id>[0-9]+)/class/$', views.character.cls, name='sheet-views-class'),
    url(r'^(?P<character_id>[0-9]+)/abilities/$', views.character.unlock_abilities,
        name='sheet-views-abilities'),
    url(r'^(?P<character_id>[0-9]+)/combos/$', views.character.combos, name='sheet-views-combos'),
    url(r'^(?P<character_id>[0-9]+)/equip/$', views.character.equip, name='sheet-views-equip'),
    url(r'^(?P<character_id>[0-9]+)/inventory/$', views.character.inventory,
        name='sheet-views-inventory'),
    url(r'^(?P<character_id>[0-9]+)/inventory/add/$',
        views.character.InventorySlotWizard.as_view(form_list=item_selection_form_list,
                                                    condition_dict=item_selection_condition_dict),
        name='sheet-views-inventory-add'),
    url(r'^(?P<character_id>[0-9]+)/level_up/$', views.character.level_up,
        name='sheet-views-level-up'),
    url(r'^(?P<character_id>[0-9]+)/skill_points/$', views.character.skill_points,
        name='sheet-views-skill-points'),
    url(r'^(?P<character_id>[0-9]+)/party/$', views.character.party, name='sheet-views-party'),
    url(r'^(?P<character_id>[0-9]+)/party/shops/(?P<shop_id>[0-9]+)/$',
        views.character.shops, name='sheet-views-shops'),
    url(r'^(?P<character_id>[0-9]+)/party/shops/(?P<shop_id>[0-9]+)/add/$',
        views.character.ShopSlotWizard.as_view(form_list=item_selection_form_list,
                                               condition_dict=item_selection_condition_dict),
        name='sheet-views-shops-add'),
    url(r'^(?P<character_id>[0-9]+)/roll20/$', views.character.roll20, name='sheet-views-roll20'),
]
