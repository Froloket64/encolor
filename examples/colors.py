from random import randint

from encolor import gfx

# Test coloring
print("RGB")

print(f"{gfx.colorize('red', gfx.Rgb(255, 0, 0))} {gfx.colorize('green', gfx.Rgb(0, 255, 0))} {gfx.colorize('blue', gfx.Rgb(0, 0, 255))}")

print()

# Print some random colors
print("Random colors")
for _ in range(10):
    color = gfx.Rgb(randint(0, 255), randint(0, 255), randint(0, 255))

    print(gfx.colorize(color.to_hex(), color))

print()

# ANSI colors (0-15)
print("Terminal colors")

print(f"{''.join(gfx.colorize_ansi('███', name) for name in gfx.COLOR_NAMES)}")
print(f"{''.join(gfx.colorize_ansi('███', name, bright=True) for name in gfx.COLOR_NAMES)}")
