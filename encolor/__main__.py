#!/usr/bin/env python3

## Terminal program/interface to the engine ##

import argparse
import sys

from . import gfx
from . import sub

stdin_input = True

# Parse args
argparser = argparse.ArgumentParser(
    prog="termcolors",
    epilog="if input isn't specified, STDIN is used."
)

argparser.add_argument("-r", "--rule", help="substitution ruleset")
argparser.add_argument("-R", "--rule-file", metavar="FILE", help="file to read substitution ruleset from")
argparser.add_argument("mode")
argparser.add_argument("input", nargs="*")

args = vars(argparser.parse_args())

def main():
    if args["input"] != []:
        stdin_input = False

    if args["mode"] == "substitute"[:len(args["mode"])]:
        # Read sub rules
        rules_str = ""

        if args["rule"]:
            rules_str += args["rule"].strip("{} ")

        if args["rule_file"]:
            with open(args["rule_file"], "r") as file:
                contents = file.read()

            stripped = contents.strip('{} ')

            rules_str += f", {stripped}"

        # Parse sub rules
        sub_rules = sub.parse_rules(rules_str)

        # Apply substitution
        if stdin_input:
            while True:
                inp = ""

                while (stdin := sys.stdin.read(1)) != "\n":
                    inp += stdin

                if inp == "":
                    break

                print(sub.substitute(inp, sub_rules))
        else:
            inp = "".join(args["input"]).strip()

            print(sub.substitute(inp, sub_rules))

    if args["mode"] == "check"[:len(args["mode"])]:
        from tests import demo_colors # Yes, yes, PEP 8

        demo_colors()
