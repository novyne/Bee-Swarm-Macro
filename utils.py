import pyautogui as pg
import time

class Keyset:

    def __init__(self, *instructions: tuple[str, float]) -> None:
        self.instructions = instructions
    
    def __str__(self) -> str:
        return str(self.instructions)

    def execute(self):
        for instruction in self.instructions:
            if instruction[0] == '':
                time.sleep(instruction[1])
                continue
            if instruction[1] == 0:
                pg.press(instruction[0])
                continue

            pg.keyDown(instruction[0])
            time.sleep(instruction[1])
            pg.keyUp(instruction[0])
    
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


RESET = Keyset(('esc', 0), ('r', 0), ('enter', 0), ('', 5))

TO_RED_CANNON = Keyset(
    *RESET.instructions,
    ('o', 0),
    ('o', 0),
    ('o', 0),
    ('o', 0),
    ('w', 2.5),
    ('d', 6),
    ('space', 0),
    ('d', 0.75),
    ('',0.5),
    ('space', 0),
    ('d', 0.5),
    ('', 0.5),
    ('e', 0)
)