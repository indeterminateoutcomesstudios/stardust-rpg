import abc
import enum
import re

template_tag = '&{template:5eDefault}'

template_terminator = '@{classactionmeleeweapon}'


@enum.unique
class MacroColorTag(enum.Enum):
    """Correspond to DnD5e character sheet macros.

    See Also:
        https://wiki.roll20.net/Roll20:DnD5e_Character_Sheet
    """
    grey = ''
    green = '{{weapon=1}}'
    purple = '{{spell=1}}'
    teal = '{{ability=1}}'
    red = '{{save=1}}'
    dark_red = '{{deathsave=1}}'


def escape_attributes(macro_string: str) -> str:
    return re.sub(pattern=r'(?P<attribute>STR|DEX|CON|INT|WIS|CHA)',
                  repl=r'@{\g<attribute>}',
                  string=macro_string)


class Macroable(abc.ABC):
    name: str = NotImplemented
    """Not exactly an approved 'abstract attribute' but makes PyCharm static analysis happy."""

    @property
    @abc.abstractmethod
    def macro(self) -> str:
        pass
