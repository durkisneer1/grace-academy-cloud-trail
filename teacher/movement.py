"""Edit this file to give the explorer its controls."""

import pykraken as kn

RUN_SPEED = 95       # pixels per second
JUMP_SPEED = 200     # upward launch speed
GRAVITY = 540        # pixels per second of speed gained downward each second


def horizontal_speed():
    speed = 0
    if kn.key.is_pressed(kn.Scancode.S_RIGHT):
        speed += RUN_SPEED
    if kn.key.is_pressed(kn.Scancode.S_LEFT):
        speed -= RUN_SPEED
    return speed


def vertical_speed(speed, on_ground, seconds):
    if on_ground and kn.key.is_just_pressed(kn.Scancode.S_SPACE):
        speed = -JUMP_SPEED
    return speed + GRAVITY * seconds
