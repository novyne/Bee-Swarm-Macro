import logging
import pyautogui as pg
import time

from utils import Keyset, TO_RED_CANNON, has_died


TO_ROOM = Keyset(
    ('', 0.225),
    ('space', 0),
    ('space', 0),
    ('a', 10),
    (',', 0),
    (',', 0),
    ('a', 1),
    ('w', 2.5),

    ('space', 0.01),
    ('w', 0.75),
    ('', 0.5),
    ('space', 0.01),
    ('w', 0.625),
    ('', 0.5),
    ('space', 0.01),
    ('w', 0.625),
    ('', 0.5),
    ('space', 0.01),
    ('w', 0.75),
    ('', 0.5),
    ('space', 0.01),
    ('w', 1),
    ('d', 0.5),
    ('w', 1),
)

WANDER = Keyset(
    ('w', 0.5),
    ('w', 0.5),
    ('s', 0.5),
    ('s', 0.5),
    ('space', 0.5),
    ('', 0.5),

    ('d', 0.5),
    ('d', 0.5),
    ('a', 0.5),
    ('a', 0.5),
    ('space', 0.5),
    ('', 0.5),

    ('s', 0.5),
    ('s', 0.5),
    ('w', 0.5),
    ('w', 0.5),
    ('space', 0.5),
    ('', 0.5),

    ('a', 0.5),
    ('a', 0.5),
    ('d', 0.5),
    ('d', 0.5),
    ('space', 0.5),
    ('', 0.5),
)


def move_to_room() -> None:
    logging.info("Moving to Commando room...")
    TO_RED_CANNON.execute()
    TO_ROOM.execute()
    logging.info("OK")


if __name__ == '__main__':

    print(f"""
COMMANDO CHICK MACRO
          
""")

    # Set up logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    time.sleep(2)
    # move_to_room()
    
    while True:

        for i in range(len(WANDER.instructions)):
            WANDER.execute_one(i)

            if has_died():
                logging.error("Player death detected - respawning and returning to room...")
                move_to_room()
                break