from dataclasses import dataclass
from Options import (
    PerGameCommonOptions,
    DeathLink,
)


@dataclass
class CentoOptions(PerGameCommonOptions):
    death_link: DeathLink
