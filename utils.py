import pyautogui as pg
import time

class Keyset:

    def __init__(self, *instructions: tuple[str, float]) -> None:
        self.instructions = instructions
    
    def __str__(self) -> str:
        return str(self.instructions)

    def execute(self):
        for instruction in self.instructions:
            pg.press(instruction[0], interval=instruction[1])
    
    @classmethod
    def from_list(cls, instructions: list[tuple[str, float]]):
        return cls(*instructions)


class InstantKeyset:

    def __init__(self, *instructions: str) -> None:
        self.instructions = instructions
    
    def __str__(self) -> str:
        return str(self.instructions)

    def execute(self):
        pg.press(self.instructions)


RESET = InstantKeyset('esc', 'r', 'enter')