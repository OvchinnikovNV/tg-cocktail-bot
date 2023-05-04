from json import load
from typing import Union, Dict
from os import getenv


def json_loader(filename: str) -> Union[dict, None]:
    try:
        with open(filename) as json_file:
            return load(json_file)
    except Exception as e:
        print(e)

    return None


class GuestState:
    def __init__(self, username: str, first_name: str, last_name: str):
        self.username: str = username
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.cocktail: Union[str, None] = None
        self.selfie: bool = False

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def clear(self):
        self.cocktail = None
        self.selfie = False


DATA = json_loader('data.json')
STATE: Dict[int, GuestState] = {}


def get_cocktail_name(callback: str) -> str:
    for cocktail in DATA['cocktails']:
        if callback == cocktail['callback']:
            return cocktail['name']

    return ""
