# Cloud Trail · Grace Academy STEM

Your explorer is looking for a blue gem above the last island. The starter already draws the world, lets you walk right, and brings you back when you fall. Today you will teach the explorer to walk left and jump, then build a route for a classmate.

## Start the game

1. Unzip the whole project. Open the cloud-trail folder in your editor.
2. Select a Python environment with PyKraken installed. If setting up a fresh environment, use Python 3.11 or newer and run `python -m pip install -r requirements.txt`.
3. From the project folder run `python main.py`. Press Right to walk off the edge. Watch where you reappear. Press R whenever you want to start over.
4. Close the game before editing. Save your changes and run it again to try them.

## Build the controls in movement.py

**1 · Walk both ways.** In `horizontal_speed()`, read the working Right-arrow code. Add a second check for `kn.Scancode.S_LEFT`. Think about the sign of the speed when moving left. Check that holding both arrows leaves you standing still.

**2 · Jump once.** In `vertical_speed()`, use `kn.key.is_just_pressed(kn.Scancode.S_SPACE)` to detect the start of a press. Launch only when `on_ground` is true. Set the speed using `JUMP_SPEED`. Upward motion has a negative speed because screen y grows downward. Keep the gravity calculation. Test a standing jump, a running jump, and a second press in midair.

**3 · Measure a jump.** Each tile is 18 pixels wide. From the same takeoff point, estimate how many tiles you can cross. Change only `JUMP_SPEED` or `GRAVITY`, predict how your jump will change, then run the same test. Choose values that let you reach the gem.

## Build an island in Tiled

Open `assets/course.tmx` in Tiled. Click **Platforms**, choose a grass tile in the tileset, and use the stamp brush (B) to extend an island by one square. Use the eraser (E) to open a gap. The Platforms layer supplies the artwork. To change the solid surface too, show and select the **Ground** object layer. Use Select Objects (S) to resize the island’s rectangle to match the art. For a gap through an island, shorten the rectangle and draw a second rectangle on the far side. Each square measures 18 × 18 pixels. Hide Ground again, save, and relaunch. Try landing on top and jumping against an island’s underside.

Paint a tree or mushroom on **Scenery** to decorate the trail. To move the gem, erase its old tile on **Finish** and stamp the gem above another island on that same layer. Touching any painted tile on Finish wins the game. Keep the starting island under the explorer and leave the layer names as supplied.

If Tiled is unavailable, pair up to make a different jump challenge using the movement constants. Give your partner a takeoff point and a target island to try.

## Artwork

Terrain, explorer, gem and landscape use Kenney's CC0 Pixel Platformer pack. The full terrain sheet is included so you can choose more tiles. The bottom strip uses Kenney’s CC0 Input Prompts artwork (assets/INPUT-PROMPTS-LICENSE.txt). The Pixel Platformer license is in `assets/KENNEY-LICENSE.txt`. [Kenney · Pixel Platformer](https://kenney.nl/assets/pixel-platformer)

## Classroom materials

[Download the student ZIP](Cloud-Trail-Student.zip?raw=true) or open the [90-minute teacher guide](teacher/LESSON.md). For a finished demo, copy teacher/movement.py over the root movement.py.
