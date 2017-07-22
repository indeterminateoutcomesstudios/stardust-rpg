from enum import Enum


class NamedEnum(Enum):
    """Enum that overrides the name property to replace underscores with spaces."""

    @property
    def name(self) -> str:
        return super().name.replace('_', ' ')
