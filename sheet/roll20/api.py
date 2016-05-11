"""URLS:
    /jukeboxplaylist/
    /players/
    /pages/
    /macros/player/-JoQ7XOdNq1qd1qz-jjs/
    /paths/page/-JoQ8N4X4kuBVHB7bHYP/
    /texts/page/-Jot0iSLWfpewBY_ZfFD/
    /graphics/page/-JjXbDyhiQ5BIfsKUIAF/
    /characters/
    /handouts/
    /decks/
    /rollabletables/
    /hands/
    /custfxs/
    /char-attribs/char/-JnxHiSp18UmTHuHLG54/
    /char-abils/char/-JnxHiSp18UmTHuHLG54/
    /decks/-JjksiRpAGV6DM1ZdjVY/cards/
    /cardtrades/
"""

import enum
import json
from typing import Tuple

import requests

from .login import Roll20Login


def get_character_id(login: Roll20Login, character_name: str) -> str:
    """
    Notes:
        Used for debugging:
            characters = json.loads(requests.get(url).text)
            json.dumps(characters, indent=4) for debugging.
    """
    url = '{}{}/characters.json?auth={}'.format(login.firebase_root, login.campaign_path,
                                                login.auth_token)
    characters = json.loads(requests.get(url).text)
    characters_data = {c['name']: c['id'] for c in characters.values()}
    print('Found characters: {}'.format(characters_data.keys()))
    character_id = characters_data[character_name]
    print('Found character: {}'.format(character_id))
    return character_id


@enum.unique
class AttributePosition(enum.Enum):
    current = 'current'
    max = 'max'


def get_attribute_id(login: Roll20Login, character_id: str, attribute_name: str) -> str:
    url = '{}{}/char-attribs/char/{}.json?auth={}'.format(login.firebase_root, login.campaign_path,
                                                          character_id, login.auth_token)
    attributes = json.loads(requests.get(url).text)
    attribs_data = {c['name']: c['id'] for c in attributes.values()}
    print('Found attributes: {}'.format(attribs_data.keys()))
    attribute_id = attribs_data[attribute_name]
    attribute_current = attributes[attribute_id][AttributePosition.current.value]
    attribute_max = attributes[attribute_id][AttributePosition.max.value]
    print('{}: {}/{}'.format(attribute_name, attribute_current, attribute_max))
    return attribute_id


def set_attribute(login: Roll20Login, character_id: str, attribute_name: str,
                  attribute_value: str, attribute_position:
                  AttributePosition=AttributePosition.current) -> None:
    attribute_id = get_attribute_id(login=login, character_id=character_id,
                                    attribute_name=attribute_name)
    url = '{}{}/char-attribs/char/{}/{}/.json?auth={}'.format(
        login.firebase_root, login.campaign_path, character_id, attribute_id, login.auth_token)
    response = requests.patch(url, data=json.dumps({attribute_position.value: attribute_value}))
    updated_mp = json.loads(response.text)[attribute_position.value]
    print('New MP: {}'.format(updated_mp))


def get_player_id(login: Roll20Login, d20_user_id: int) -> str:
    url = '{}{}/players/.json?auth={}'.format(login.firebase_root, login.campaign_path,
                                              login.auth_token)
    players = json.loads(requests.get(url).text)
    correct_player_id = None
    for player_id, player_info in players.items():
        if player_info['d20userid'] == str(d20_user_id):
            correct_player_id = player_id

    correct_player_info = players[correct_player_id]
    print(correct_player_info)
    return correct_player_id


def get_macros(login: Roll20Login, player_id: str) -> Tuple[str, ...]:
    url = '{}{}/macros/.json?auth={}'.format(login.firebase_root, login.campaign_path,
                                             login.auth_token)
    all_players_macros = json.loads(requests.get(url).text)
    print(json.dumps(all_players_macros, indent=4))
    try:
        player_macros = all_players_macros['player'][player_id]
        print(json.dumps(player_macros, indent=4))
        return player_macros
    except KeyError:
        print('No macros found for Player ID: {}'.format(player_id))
        return None


def update_ability(login: Roll20Login, character_id: str, ability_name: str,
                   ability_action: str) -> None:
    url = '{}{}/char-abils/char.json?auth={}'.format(login.firebase_root, login.campaign_path,
                                                     login.auth_token)
    abilities = json.loads(requests.get(url).text)
    print('Abilities')
    print(json.dumps(abilities[character_id], indent=4))
    for ability in abilities[character_id].values():
        if ability['name'] == ability_name:
            print('Found {name} Ability: {id}'.format(name=ability_name, id=ability['id']))
            url = '{}{}/char-abils/char/{}/{}/.json?auth={}'.format(
                login.firebase_root, login.campaign_path, character_id, ability['id'],
                login.auth_token)
            response = requests.patch(url, data=json.dumps({'action': ability_action}))
            updated_action = json.loads(response.text)['action']
            print('New Action: {}'.format(updated_action))


def create_ability(login: Roll20Login, character_id: str, ability_name: str,
                   ability_action: str) -> None:
    pass
