# Teaching Cloud Trail · 90 minutes

Distribute the student ZIP and have everyone extract it before class. Each machine needs a graphical desktop and a Python interpreter with kraken-engine 1.8.0 installed. Install Tiled ahead of time for the map activity. With the dependency installed, gameplay and map editing work offline.

For a completed opening demo, unzip a second copy and replace its movement.py with the movement.py in this teacher folder. Run python main.py in that copy. Keep a fresh starter for live coding. Hold Right and tap Space near each island's edge to reach the blue gem.

| Minutes | Activity | Check for understanding |
| --- | --- | --- |
| 0–10 | Demonstrate the completed route, then launch the starter. Let everyone walk right and fall. | Which part already works? Point to the line that moves the explorer right. |
| 10–25 | Add left movement in movement.py. Partners predict what happens when both arrows are held. | Left and right work independently. Holding both cancels movement. |
| 25–45 | Sketch the screen y-axis. Add a grounded Space press and keep gravity acting every frame. | The explorer lands on the next island. Tapping Space in midair gives no extra jump. |
| 45–60 | Ask each pair to change one constant, predict the effect, and measure a jump in tile widths. | Compare two attempts from the same starting point and explain the difference. |
| 60–80 | In Tiled, redesign one gap, move the gem, and trade laptops for a playtest. | A partner reaches the gem and identifies one change that helped or hindered the jump. |
| 80–90 | Make one revision after feedback and replay. | Exit ticket: What made the jump higher or longer? What observation supports that answer? |

## If a pair gets stuck

- **The editor reports a missing module.** In its terminal, run `python -c "import sys, pykraken; print(sys.executable)"`. Select the same interpreter in the editor. A fresh environment can install the pinned package from requirements.txt.
- **The explorer falls faster when Space is pressed.** Ask the student to trace the sign of vertical speed on the first frame of a jump.
- **A new platform is visible but the explorer falls through.** In Tiled, show Ground and align the collision rectangle with the tiles painted on Platforms. Save the TMX and relaunch.
- **An island becomes unreachable.** Restore the reference values (run 95, jump 200, gravity 540) and move the island one tile closer. Change one variable per attempt.

The supplied teacher movement.py contains both completed functions. main.py contains the shared game loop, CharacterBody movement, respawn, and win condition. The Ground object layer contains one rectangle per island. World.from_map_layer turns those rectangles into colliders on one static body. The explorer uses move_and_slide and is_on_floor. The Finish tile layer detects the gem.
