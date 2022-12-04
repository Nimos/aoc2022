
from os import path
from typing import List
import requests

SESSION_FILE = "session.txt"


def get_input(day, small=False):

    if small:
        file_name = f"inputs/{day:02}.small.txt"
    else:
        file_name = f"inputs/{day:02}.txt"

    if path.exists(file_name) or small:
        file = open(file_name, "r")
        data = file.read()
        file.close()
    else:
        file = open(SESSION_FILE, "r")
        session = file.read()
        file.close()
        cookies = {"session": session}

        url = f"https://adventofcode.com/2022/day/{day}/input"

        data = requests.get(url, cookies=cookies, headers={"User-Agent": "Nimos"}).text

        file = open(file_name, "w")
        file.write(data)
        file.close()

    return data

class AocData:
    _data = None
    _data_small = None
    def __init__(self, day) -> None:
        self._day = day

    def _get_data_small(self):
        if not self._data_small:
            self._data_small = get_input(self._day, small=True)
        return self._data_small
    
    def _get_data(self):
        if not self._data:
            self._data = get_input(self._day)
        return self._data
    

    
    def get_raw(self, small=False) -> str:
        if small:
            return self._get_data_small()
        else:
            return self._get_data()

    def lines(self, small: bool=False) -> List[str]:
        return [x for x in self.get_raw(small=small).split("\n") if x]
        
        
    def text(self, small: bool =False) -> str:
        return self.get_raw(small=small)