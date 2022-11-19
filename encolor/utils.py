## Useful functions ##

import gfx

def error(msg):
    print(f"{gfx.colorize_ansi('ERROR:', 'red')} {msg}")

    exit(1)
