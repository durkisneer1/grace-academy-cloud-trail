"""Run this file to play Cloud Trail. Start your edits in movement.py."""

from pathlib import Path

import pykraken as kn
import movement

ASSETS = Path(__file__).resolve().parent / "assets"
WIDTH, HEIGHT = 432, 234


def create_explorer(world):
    player = kn.physics.CharacterBody(world)
    player.capsule_shape = kn.Capsule(0, -3, 0, 3, 6)
    reset_player(player)
    return player


def reset_player(player):
    player.pos = kn.Vec2(28, 170)
    player.velocity = kn.Vec2(0, 0)


def move_player(player, seconds):
    vx = movement.horizontal_speed()
    vy = movement.vertical_speed(player.velocity.y, player.is_on_floor(), seconds)
    player.velocity = kn.Vec2(vx, vy)
    player.move_and_slide(seconds)


def sprite_rect(player):
    return kn.Rect(player.pos.x - 8, player.pos.y - 9, 16, 18)


def play():
    kn.window.create("Cloud Trail | Grace Academy STEM", WIDTH * 2, HEIGHT * 2)
    kn.renderer.set_virtual_resolution(WIDTH, HEIGHT)
    kn.renderer.set_default_filter_mode(kn.FilterMode.NEAREST)
    kn.time.set_target(60)

    course = kn.tilemap.Map(ASSETS / "course.tmx")
    world = kn.physics.World()
    ground = world.from_map_layer(course.get_layer("Ground"))
    finish = course.get_layer("Finish")
    board = kn.Texture(ASSETS / "sky.png")
    sprite = kn.Texture(ASSETS / "explorer.png")
    controls = kn.Texture(ASSETS / "controls.png")
    victory = kn.Texture(ASSETS / "win.png")

    player = create_explorer(world)
    won = False
    while kn.window.is_open():
        kn.event.poll()
        if not kn.window.is_open():
            break
        if player.pos.y > HEIGHT or kn.key.is_just_pressed(kn.Scancode.S_r):
            reset_player(player)
            won = False

        if not won:
            seconds = min(kn.time.get_delta(), 1 / 30)
            if seconds > 0:
                move_player(player, seconds)
                world.step(seconds)
            won = bool(finish.get_from_area(sprite_rect(player)))

        kn.renderer.clear()
        kn.renderer.draw(board, kn.Rect(0, 0, WIDTH, 212))
        course.draw()
        kn.renderer.draw(sprite, sprite_rect(player))
        kn.renderer.draw(victory if won else controls, kn.Rect(0, 212, WIDTH, 22))
        kn.renderer.present()


if __name__ == "__main__":
    kn.init()
    try:
        play()
    finally:
        kn.quit()
