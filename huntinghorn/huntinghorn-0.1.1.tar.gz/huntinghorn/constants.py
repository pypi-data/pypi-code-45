"""Constants and Enums for use in the main program."""

from colorama import Fore, Back, Style
from dataclasses import dataclass
from enum import Enum, auto
from typing import List


class Note(Enum):
    """Hunting Horn notes."""

    AQUA = auto()
    BLUE = auto()
    GREEN = auto()
    MAGENTA = auto()
    RED = auto()
    WHITE = auto()
    YELLOW = auto()

    def __str__(self):
        note_colours = {
            self.AQUA: Fore.LIGHTBLUE_EX,
            self.BLUE: Fore.BLUE,
            self.GREEN: Fore.GREEN,
            self.MAGENTA: Fore.MAGENTA,
            self.RED: Fore.RED,
            self.WHITE: Fore.LIGHTWHITE_EX,
            self.YELLOW: Fore.YELLOW
        }
        name = super().__str__().partition('.')[2]
        colour = note_colours[self]
        return f'{Fore.BLACK}{colour}♪{Style.RESET_ALL}'


@dataclass
class Melody:
    """Represents a Hunting Horn melody."""

    name: str
    notes: List[Note]

    def __str__(self):
        return self.name

    def as_str(self, padding: int):
        return self.name.ljust(padding) + ' '.join(map(str, self.notes))


# flake8: noqa: E501
melodies = [
    Melody('Clairvoyance', [Note.BLUE, Note.BLUE, Note.AQUA]),
    Melody('Supersonic Waves', [Note.YELLOW, Note.YELLOW, Note.YELLOW]),
    Melody('Attack Up [Lo]', [Note.WHITE, Note.RED]),
    Melody('Attack Up [Hi]', [Note.MAGENTA, Note.RED, Note.RED]),
    Melody('Defense Up [Lo]', [Note.RED, Note.YELLOW]),
    Melody('Defense Up [Hi]', [Note.RED, Note.GREEN, Note.RED]),
    Melody('Defense Up [Hi]', [Note.RED, Note.AQUA, Note.AQUA, Note.MAGENTA]),
    Melody('Health Inc [Lo]', [Note.RED, Note.BLUE, Note.WHITE]),
    Melody('Health Inc [Mid]', [Note.RED, Note.RED, Note.AQUA]),
    Melody('Health Inc [Hi]', [Note.RED, Note.BLUE, Note.RED, Note.MAGENTA]),
    Melody('Wind Reduce', [Note.BLUE, Note.BLUE, Note.RED]),
    Melody('Wind Cancel', [Note.BLUE, Note.BLUE, Note.GREEN]),
    Melody('Wind Cancel', [Note.BLUE, Note.AQUA, Note.BLUE]),
    Melody('Wind All Cancel', [Note.BLUE, Note.BLUE, Note.YELLOW, Note.MAGENTA]),
    Melody('Marathon [Lo]', [Note.WHITE, Note.BLUE]),
    Melody('Marathon [Hi]', [Note.MAGENTA, Note.BLUE, Note.BLUE]),
    Melody('Health Rec [Lo]', [Note.MAGENTA, Note.GREEN]),
    Melody('Health Rec [Mid]', [Note.GREEN, Note.MAGENTA, Note.YELLOW]),
    Melody('Health Rec [Hi]', [Note.GREEN, Note.GREEN, Note.MAGENTA, Note.AQUA]),
    Melody('Health Rec [Lo] & Antidote', [Note.WHITE, Note.GREEN]),
    Melody('Health Rec [Mid] & Antidote', [Note.GREEN, Note.BLUE, Note.MAGENTA, Note.BLUE]),
    Melody('Health Rec [Mid] & Deodorant', [Note.GREEN, Note.WHITE, Note.AQUA]),
    Melody('Recover Spd Up [Lo]', [Note.GREEN, Note.GREEN, Note.YELLOW]),
    Melody('Recover Spd Up [Hi]', [Note.GREEN, Note.RED, Note.GREEN, Note.MAGENTA]),
    Melody('Heavenly Protection', [Note.GREEN, Note.YELLOW, Note.MAGENTA, Note.YELLOW]),
    Melody('Hear Protect [Lo]', [Note.AQUA, Note.AQUA, Note.RED]),
    Melody('Hear Protect [Hi]', [Note.AQUA, Note.AQUA, Note.GREEN, Note.MAGENTA]),
    Melody('No Cold & Snow Res', [Note.AQUA, Note.AQUA, Note.YELLOW]),
    Melody('No Heat', [Note.AQUA, Note.GREEN, Note.AQUA]),
    Melody('No Faint', [Note.AQUA, Note.BLUE, Note.MAGENTA]),
    Melody('No Paralysis', [Note.AQUA, Note.YELLOW, Note.YELLOW]),
    Melody('No Quakes', [Note.AQUA, Note.YELLOW, Note.AQUA]),
    Melody('Element Attack Up', [Note.YELLOW, Note.BLUE, Note.YELLOW, Note.WHITE]),
    Melody('Fire Res Up [Lo]', [Note.YELLOW, Note.RED]),
    Melody('Fire Res Up [Hi]', [Note.YELLOW, Note.BLUE, Note.WHITE]),
    Melody('Water Res Up [Lo]', [Note.YELLOW, Note.BLUE, Note.MAGENTA]),
    Melody('Water Res Up [Hi]', [Note.YELLOW, Note.BLUE, Note.BLUE, Note.WHITE]),
    Melody('Thunder Res Up [Lo]', [Note.YELLOW, Note.AQUA, Note.MAGENTA]),
    Melody('Thunder Res Up [Hi]', [Note.YELLOW, Note.YELLOW, Note.BLUE]),
    Melody('Ice Res Up [Lo]', [Note.YELLOW, Note.WHITE, Note.AQUA]),
    Melody('Ice Res Up [Lo]', [Note.YELLOW, Note.GREEN, Note.WHITE]),
    Melody('Ice Res Up [Hi]', [Note.YELLOW, Note.MAGENTA, Note.AQUA]),
    Melody('Ice Res Up [Hi]', [Note.YELLOW, Note.GREEN, Note.MAGENTA]),
    Melody('Dragon Res Up [Lo]', [Note.WHITE, Note.YELLOW]),
    Melody('Dragon Res Up [Hi]', [Note.MAGENTA, Note.YELLOW, Note.YELLOW])
]
