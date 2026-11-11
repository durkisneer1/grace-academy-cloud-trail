"""Edit this file to give the explorer its controls."""

import pykraken as kn

RUN_SPEED = 95       # pixels per second
JUMP_SPEED = 200     # upward launch speed
GRAVITY = 540        # pixels per second of speed gained downward each second


def horizontal_speed():
    speed = 0
    if kn.key.is_pressed(kn.Scancode.S_RIGHT):
        speed += RUN_SPEED
    # TODO 1: Check the left arrow too. How do you move toward smaller x?
    return speed


def vertical_speed(speed, on_ground, seconds):
    # TODO 2: When grounded and Space is first pressed, launch upward.
    # Screen y increases downward. Which sign should the jump speed have?
    return speed + GRAVITY * seconds
