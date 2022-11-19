## Substitution functions ##
import re

from . import gfx

# Parse a rules string into a dict
def parse_rules(rules_str):
    rules_lst = rules_str.strip("{} ").split(",")

    sub_rules = {}

    for pair in rules_lst:
        pattern = pair.split(":")[0].strip()
        color = pair.split(":")[1].strip()

        sub_rules.update({pattern: color})

    return sub_rules

# Perform colorizing substitution
def substitute(s, sub_rules):
        result = s

        for pattern in sub_rules:
            for match in set(re.finditer(pattern, s)):
                    match_str = match.string[match.start():match.end()]
                    color = sub_rules[pattern]

                    if color in gfx.COLOR_NAMES:
                        result = result.replace(match_str, gfx.colorize_ansi(match_str, color))
                    elif gfx.Rgb.is_hex(color):
                        color_rgb = gfx.Rgb.from_hex(color)

                        result = result.replace(match_str, gfx.colorize(match_str, color_rgb))
                    else:
                        raise ValueError(f"Invalid color syntax: {color}")

        return result
