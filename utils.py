import pyautogui as pg
import pytesseract as pyt
import time

class Keyset:

    def __init__(self, *instructions: tuple[str, float]) -> None:
        self.instructions = instructions
    
    def __str__(self) -> str:
        return str(self.instructions)

    def execute(self) -> None:
        for i in range(len(self.instructions)):
            self.execute_one(i)

    def execute_one(self, index: int) -> None:
        instruction = self.instructions[index]
        if instruction[0] == '':
            time.sleep(instruction[1])
            return
        if instruction[1] == 0:
            pg.press(instruction[0])
            return

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


def has_died() -> bool:
    """
    Read the bottom right corner for "You died".
    Return True if found, False otherwise.
    """

    # Clip the bottom right corner
    clip = pg.screenshot(region=(pg.size()[0] - 500, pg.size()[1] - 500, 500, 500))

    # Check for "you died"
    return 'you died' in pyt.image_to_string(clip).lower()


RESET = Keyset(('esc', 0), ('r', 0), ('enter', 0), ('', 6))

TO_RED_CANNON = Keyset(
    *RESET.instructions,
    ('o', 0),
    ('o', 0),
    ('o', 0),
    ('o', 0),
    ('w', 2.25),
    ('d', 6.5),
    ('space', 0.125),
    ('d', 0.75),
    ('', 0.5),
    ('space', 0.25),
    ('d', 0.5),
    ('', 0.5),
    ('e', 0)
)