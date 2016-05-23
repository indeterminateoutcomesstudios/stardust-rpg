import enum
import re

template_tag = '&{template:5eDefault}'

template_terminator = '@{classactionmeleeweapon}'


@enum.unique
class MacroColorTag(enum.Enum):
    """Correspond to DnD5e character sheet macros"""
    grey = ''
    green = '{{weapon=1}}'
    purple = '{{spell=1}}'
    teal = '{{ability=1}}'
    red = '{{save=1}}'
    dark_red = '{{deathsave=1}}'


def escape_attributes(macro_string: str) -> str:
    return re.sub(pattern=r'(?P<attribute>ATH|DEX|CON|INT|WIS|CHA)',
                  repl='@{\g<attribute>}',
                  string=macro_string)
